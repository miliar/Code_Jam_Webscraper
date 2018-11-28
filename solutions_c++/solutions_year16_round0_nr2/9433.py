#include <bits/stdc++.h>
using namespace std;
#define e1 first
#define e2 second
#define pb push_back
#define mp make_pair
#define boost ios_base::sync_with_stdio(false)
#define eb emplace_back
#define OUT(x) {cout << x; exit(0); }
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> PII;
typedef pair <ll, ll> PLL;
typedef pair <PLL, PLL> PP;
typedef unsigned int ui;
const int mod = 1e9+7;
const int inf = 1e9+9;
const ll MOD = 1e9+696969;
const ll INF = 1e18;
#define maxn 1010
int n, T, a;
string s;
int t[maxn], help[maxn];
void flip(int x) {
	for (int i=1; i<=x; ++i) help[x - i + 1] = t[i];
	for (int i=1; i<=x; ++i) t[i] = (help[i] ^ 1);
}

int main()
{
	scanf("%d", &T);
	for (int z=1; z<=T; ++z) {
		cin >> s;
		n = s.length();
		int wyn = 0;
		char last = '+';
		for (int i=n-1; i>=0; --i)
		  if (s[i] != last) {
		  ++wyn;
		  last = s[i];
		}
		printf("Case #%d: %d\n", z, wyn);
	}
}
