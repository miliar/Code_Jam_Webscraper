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

int getFlipNumber(string s)
{
	//cout << s << endl;

	if (s.size() == 0) {
		return 0;
	}

	if (s.size() == 1) {
		if (s == "+") return 0;
		else return 1;
	}

	int ans = 0;

	for (int i = 0; i < s.size() - 1; i++) {
		if (s[i] != s[i + 1]) ans++;
	}

	if (s[s.size() - 2] == '+') ans--;

	return ans;
}

int main()
{
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string s;
		cin >> s;
		s += '=';
		cout << "Case #" << i << ": " << getFlipNumber(s) << endl;
	}

	return 0;
}

//int t;
//ll n;
//
//int main()
//{
//	cin >> t;
//
//	for (int i = 0; i < t; i++) {
//		cin >> n;
//
//		if (n == 0) {
//			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
//		}
//		else {
//			set<ll> st;
//			ll m = n;
//			while (st.size() < 10) {
//				ll k = m;
//				while (k) {
//					st.insert(k % 10);
//					k /= 10;
//				}
//				if (st.size() >= 10) break;
//				m += n;
//			}
//			cout << "Case #" << i + 1 << ": " << m << endl;
//		}
//		
//	}
//
//	return 0;
//}