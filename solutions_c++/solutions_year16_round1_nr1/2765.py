#include <bits/stdc++.h>
using namespace std;

#define INF 0X3F3F3F3F
#define INFL 0x3F3F3F3F3F3F3F3FLL
#define MOD 1000000007
#define st first
#define nd second
#define pb push_back
#define mp make_pair
#define sz(X) int((X).size())
#define all(X) (X).begin(), (X).end()
#define rall(X) (X).rbegin(), (X).rend()
#define pow2(X) ((X)*(X))

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

int main(int argc, char const *argv[]) {
	int n;
	scanf("%d", &n);
	for (int t = 1; t <= n; ++t) {
		string str;
		cin >> str;
		string ans = ""; ans += str[0];
		for (int i = 1; i < sz(str); i++) {
			if (str[i] < ans[0]) {
				ans += str[i];
			} else {
				ans = str[i] + ans;
			}
		}
		printf("Case #%d: %s\n", t, ans.c_str());
	}
	return 0;
}