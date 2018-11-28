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
ll N;
bool jest[11];
int main()
{
	scanf("%d", &T);
	for (int z=1; z<=T; ++z) {
		cin >> n;
		ll N = n, wyn = -1;
		for (int i=0; i<10; ++i) jest[i] = 0;
		
		for (int i=0; i<=100000; ++i) {
			ll akt = N * i;
			while (akt > 0) {
				jest[akt % 10]++;
				akt /= 10;
			}
			bool dobrze = 1;
			for (int j=0; j<10; ++j)
			  if (!jest[j]) dobrze = 0;
			if (dobrze) {
				wyn = N * i;
				break;
			}
		}
		if (wyn != -1) printf("Case #%d: %lld\n", z, wyn);
		else printf("Case #%d: INSOMNIA\n", z);
	}
}
