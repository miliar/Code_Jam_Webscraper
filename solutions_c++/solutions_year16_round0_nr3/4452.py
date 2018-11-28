#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream 	f("in.txt");
	ofstream 	g("out.txt");
	long long 	d[9];
	int 		N = 16;
	int 		J = 50;
	int 		P = (1 << (N - 1)) + 1;

	g << "Case #1:" << endl;
	for (int r = 0; (r < (1 << (N - 2))) && J; r++)
	{
		long long 	v 			= P + (r << 1);
		string		s(N, '0');
		bool 		isCoinJam 	= true;

		for (int i = 0; i < N; i++)
			if (v & (1 << i)) s[N - i - 1] = '1';

		for (int base = 2; (base <= 10) && isCoinJam; base++)
		{
			long long 	x 		= stoll(s, 0, base);
			bool 		isPrime = true;

			if (x % 2 == 0) { isPrime = false; d[base - 2] = 2; }
			for (long long i = 3; (i * i <= x) && isPrime; i += 2)
				if (x % i == 0) { isPrime = false; d[base - 2] = i; }

			isCoinJam = !isPrime;
		}

		if (isCoinJam)
		{
			J--;
			g << s;
			for (int i = 0; i < 9; i++) g << " " << d[i];
			g << endl;
		}
	}

	return 0;
}
