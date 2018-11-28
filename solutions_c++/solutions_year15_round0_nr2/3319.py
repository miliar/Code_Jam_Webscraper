#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	fstream in("input.txt", ios::in);
	fstream out("output.txt", ios::out);

	int T;
	in >> T;

	for(int kase = 1; kase <= T; ++kase)
	{
		int D, P[1000];
		in >> D;
		for(int i = 0; i < D; ++i)
			in >> P[i];

		int max = 0;
		for(int i = 0; i < D; ++i)
			if(P[i] > max) max = P[i];
		
		int ans = 987654321;
		for(int i = 1; i <= max; ++i)
		{
			int tmp = 0;
			for(int j = 0; j < D; ++j)
			{
				tmp += (P[j] / i - 1);
				if(P[j] % i != 0) ++tmp;
			}
			tmp += i;
			if(ans > tmp) ans = tmp;
		}

		out << "Case #" << kase << ": " << ans << endl;
	}

	in.close();
	out.close();
	return 0;
}
