#include <fstream>
#include <string>
using namespace std;

int solve(string &s, int p, int target)
{
	if (p < 0) return 0;
	return (s[p] == target) ? solve(s, p-1, target) : (1 + solve(s, p-1, -target + '+' + '-'));
}

int main()
{
	ifstream 	f("in.txt");
	ofstream 	g("out.txt");
	int 		T;

	f >> T;
	for (int test = 1; test <= T; test++)
	{
		string s;
		f >> s;
		g << "Case #" << test << ": " << solve(s, s.length() - 1, '+') << endl;
	}

	return 0;
}
