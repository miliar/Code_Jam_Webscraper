#include <algorithm>
#include <iomanip>
#include <istream>
#include <map>
#include <numeric>
#include <ostream>
#include <set>
#include <fstream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#define ll long long
using namespace std;
// Powered by caide (code generator, tester, and library code inliner)


class Solution {
public:
	void solve(std::istream& in, std::ostream& out) {
		ll t, n, k, f;
		string s;
		ofstream ttt;
		ttt.open("output.out");
		in >> t;
		for (int ii = 1; ii <= t; ii++)
		{
			ttt << "Case #" << ii << ": ";
//			out << "Case #" << ii << ": ";
			in >> s;
			f = 0;
			k = 0;
			for (int i = 0; i < s.length(); i++)
			{
				if ((i==0)&&(s[i]=='-'))
				{
					f++;
					k++;
				}
				else
				{
					if ((s[i] == '-') && (s[i-1] == '+'))
					{
						k++;
					}
				}
			}
			ttt << k * 2 - f << endl;
//			out << k * 2 - f << endl;
		}
	}
};

void solve(std::istream& in, std::ostream& out)
{
	out << std::setprecision(12);
	Solution solution;
	solution.solve(in, out);
}

#include <iostream>

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    istream& in = cin;

    ostream& out = cout;
    solve(in, out);
    return 0;
}
