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
		ll z = 0, t, n = 100000000, k, f;
		vector<int> a(17, 0);
		vector<ll>pr;
		vector<char> prime(n + 1, true);
		prime[0] = prime[1] = false;
		for (int i = 2; i*i <= n; ++i)
		if (prime[i]){
			pr.push_back(i);
			for (int j = 2; j <= n / i; j++)
			if (prime[i*j]) prime[i*j] = false;
		
		}
		ll prl = pr.size();
		ofstream ttt;
		ttt.open("output.out");
		ttt << "Case #1:" << endl;
		a[0] = 1;
		a[2] = 1;
		a[4] = 1;
		a[5] = 1;
		a[7] = 1;
		a[15] = 1;
		while ((a[16]==0)&&(z<50))
		{
			vector<ll>divideby(11,0);
			int count=0;
			for (int ii = 2; ii <= 10; ii++)
			{
				ll q=0;
				for (int i = 15; i >= 0 ; i--)
				{
					q = q*ii + a[i];
				}
				for (int i = 0; i < prl; i++)
				{
					if (pr[i]>sqrt(q))
					{
						break;
					}
					if (q%pr[i]==0)
					{
						divideby[ii] = pr[i];
						count++;
						break;
					}
				}
				if (divideby[ii]==0)
				{
					break;
				}
			}
			if (count==9)
			{
				for (int i = 15; i >= 0; i--)
				{
					out << a[i];
					ttt << a[i];
				}
				for (int i = 2; i <11; i++)
				{
					out <<" "<< divideby[i];
					ttt << " " << divideby[i];
				}
				out << endl;
				ttt << endl;
				z++;
			}
			a[1]++;
			int p = 1;
			while (a[p] == 2)
			{
				a[p]=0;
				a[p + 1]++;
				p++;
			}
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
