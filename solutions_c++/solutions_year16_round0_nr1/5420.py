#include <fstream>
#include <vector>
#include <string>
using namespace std;

string solve(int N)
{
	vector<int> 	d(10, 0);
	int 			digits 	= 0;
	long long 		x 		= 0LL;

	if (!N) return "INSOMNIA";

	while (digits < 10)
	{
		x += N;
		string s = to_string(x);

		for (char c : s)
		{
			if (!d[c - '0']) digits++;
			d[c - '0'] = 1;
		}
	}

	return to_string(x);
}

int main()
{
	ifstream	f("in.txt");
	ofstream 	g("out.txt");
	int 		T, N;

	f >> T;
	for (int test = 1; test <= T; test++)
	{
		f >> N;
		g << "Case #" << test << ": " << solve(N) << endl;
	}

	return 0;
}
