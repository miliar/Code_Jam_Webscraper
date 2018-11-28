#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
#define sc(x) scanf("%d", &x)
#define scl(x) scanf("%I64d", &x)
#define loop(i,s,e) for(int i=s ; i<e ; i++)
#define rep(i,s,e) for(int i=s ; i>=e ; i--)
#define INF 1000000
#define MOD 1000000007
#define f first
#define s second
#define EPS 1e-7
#define Rd freopen("in.txt", "r", stdin)
#define Wr freopen("out.txt", "w", stdout)
#define PS push_back
#define M_PI           3.14159265358979323846  /* pi */

int arr[20];
bool marked(ll n) {
	if (n == 0)
		arr[0] = 1;
	else {
		while (n > 0) {
			arr[n % 10] = 1;
			n /= 10;
		}
	}
	loop(i,0,10)
	{
		if (arr[i] == 0)
			return false;
	}
	return true;
}
int main() {
	Rd;
	Wr;
	int T;
	sc(T);
	loop(t,0,T)
	{
		memset(arr, 0, sizeof arr);
		printf("Case #%d: ", t + 1);
		ll n, base;
		scl(n);
		base = n;
		if (n == 0) {
			printf("INSOMNIA\n");
		} else {
			while (!marked(n)) {
				n += base;
			}
			printf("%lld\n", n);
		}
	}
	return 0;
}
