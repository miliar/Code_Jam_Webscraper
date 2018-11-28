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

ll solut(ll x){
	if (x==0)
	{
		return -1;
	}
	ll count = 0, w, l;
	vector<int> used(10);
	for (int i = 1; i < 10000; i++)
	{
		w = x*i;
		while (w>0)
		{
			l = w % 10;
			w /= 10;
			if (used[l]==0)
			{
				used[l]++;
				count++;
			}
		}
		if (count==10)
		{
			return x*i;
		}
	}
	return -1;
}

class Solution {
public:
    void solve(std::istream& in, std::ostream& out) {
		ll t, n, k, f;
		ofstream ttt;
		ttt.open("output.out");
		in >> t;
		for (int ii = 1; ii <= t; ii++)
		{
			ttt << "Case #"<<ii<<": ";
			in >> k;
			f = solut(k);
			if (f > 0)ttt << f << endl; else ttt << "INSOMNIA" << endl;
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
