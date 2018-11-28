#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<bitset>
#include<vector>
#include<deque>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cmath>
#include<iomanip>
#include <functional>
using namespace std;
typedef long long ll;
const int mod = 1000000007;
const int INF = 1 << 28;
//cout << fixed << std::setprecision(9)
//memset(a, 0, sizeof(a));
//--------------------------

int t;
ll n;

int main()
{
	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> n;

		if (n == 0) {
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
		}
		else {
			set<ll> st;
			ll m = n;
			while (st.size() < 10) {
				ll k = m;
				while (k) {
					st.insert(k % 10);
					k /= 10;
				}
				if (st.size() >= 10) break;
				m += n;
			}
			cout << "Case #" << i + 1 << ": " << m << endl;
		}
		
	}

	return 0;
}