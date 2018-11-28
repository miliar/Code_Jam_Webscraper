#include <bits/stdc++.h>
using namespace std;
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define cnt(x , n) count(x.begin(),x.end(),n)
#define so(x) sort(x.begin(),x.end())
#define rso(x) sort(x.rbegin(),x.rend())
#define mx(x) *max_element(x.begin(),x.end())
#define mn(x) *min_element(x.begin(),x.end())
#define rev(x) reverse(x.begin(),x.end())
#define pb push_back
#define al(n) (n).begin(),(n).end()
#define ral(n) (n).rbegin(),(n).rend()
#define mp make_pair
#define sz size()
#define F first
#define S second
#define rFoR(i,x,n) for(int i=x;i>n;--i)
#define FoR(i,x,n) for(int i = x; i < n; i++)
#define RE(s) freopen(s, "r", stdin)
#define WR(s) freopen(s, "w", stdout)

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int main() {
#ifndef ONLINE_JUDGE
	RE("text.txt");
	WR("out.txt");
#endif
	int n, sMax, res = 0, currSum = 0;
	string s;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> sMax >> s;
		if (s[0] == '0') {
			s[0] = '1';
			++res;
		}
		for (int j = 0; j < s.sz; ++j) {
			if (currSum < j) {
				++res;
				++currSum;
			}
			currSum += (s[j] - '0');
		}
		if (currSum < sMax) {
			res = sMax - currSum;
		}
		printf("Case #%d: %d\n", i + 1, res);
		currSum = res = 0;
	}

	return 0;
}
