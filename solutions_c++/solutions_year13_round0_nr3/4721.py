#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <vector>
#include <string>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) (int)a.size()
#define all(a) a.begin(), a.end()
#define ms(a,key) memset(a, key, sizeof(a))
#define setval(a,val) memset(a,val,sizeof(a));
#define forit(it,s) for (typeof(s.begin())it = s.begin(); it != s.end(); it++)

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll;

const int N = 100500;
const int inf = 1<<30;

bool pali(const ll num) {
	char s[100];
	sprintf(s, "%I64d", num);
	int len = strlen(s);
	for (int i = 0; i < len-i-1; i++)
		if (s[i] != s[len-i-1])
			return 0;
	return 1;
}

int main()
{
	#ifdef LOCAL
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	#endif

	vector<ll> s;
	for (ll i=1;i<=10000000;i++)
		if (pali(i)&&pali(i*i))
			s.pb(i*i);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		ll A, B;
		scanf("%I64d %I64d", &A, &B);
		printf("Case #%d: %d\n", t, upper_bound(all(s), B) - lower_bound(all(s), A));
	}

	return 0;
}
