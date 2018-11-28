#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <string>
#include <set>

using namespace std;

typedef long long ll;
typedef double ld;
typedef pair<ll , pair<ll,ll>> piii;

const ll N = 2e6;
const ll M = 11;
const ll INF = 2e9;
const ll SQ = 320;
const ll MOD = 1e9+7;

#define inf cin
#define of cout
#define mp make_pair

set<int> st;

int main()
{
	ios_base::sync_with_stdio(false);
	ifstream inf("input.txt");
	ofstream of("output.txt");
	cin.tie();

	int t;
	cin >> t;
	for (int i = 1; i<=t; i++)
	{
		ll n;
		cin >> n;
		int f = 0;
		st.clear();
		cout << "Case #" << i << ": ";
		for (int i = 1; i<=1e5; i++)
		{
			ll x = n*i;
			while (x)
			{
				st.insert(x%10);
				x /= 10;
			}
			if (st.size()==10)
			{
				cout << n*i << '\n';
				f = 1;
				break;
			}
		}
		if (!f)
			cout << "INSOMNIA\n";
	}
	return 0;
}