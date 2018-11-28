#include <bits/stdc++.h>

#define f(i, a, n) for (ll i = a; i < n; i++)
#define fd(i, n, a) for (ll i = n; i >= a; i--)
#define rep(i,n) f(i,0,n)

#define mkp make_pair
#define pb push_back
#define ff first
#define ss second
#define pll pair <ll, ll>
#define pii pair <int, int>
#define MOD 1000000007

#define s(x) scanf("%lld", &x); //s(x) is for long long int.
#define si(x) scanf("%d", &x);

#define p(x) printf("%lld", x);  //p(x) is for long long int.
#define pn(x) printf("%lld\n", x);  //..n(x) is for printing with New Line.
#define ps(x) printf("%lld ", x);  //..s(x) is for printing with Space.
#define pi(x) printf("%d", x);
#define pin(x) printf("%d\n", x);
#define pis(x) printf("%d ", x);

#define debug false
#define ok if(debug)
#define trace(x) ok cout << #x << ": " << x << endl;
#define trace2(x, y) ok cout << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)    ok      cout << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)  ok cout << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " \
								<< #d << ": " << d << endl;
#define trace5(a, b, c, d, e) ok cout << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " \
									 << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) ok cout << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " \
									<< #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

typedef long long ll;
using namespace std;

int vis[11];
int viscnt() {
	int ret = 0;
	for (int i = 0; i < 10; i++) {
		if (vis[i] == 1)
			ret++;
	}
	return ret;
}
void mark(int num) {
	while (num > 0) {
		vis[num%10] = 1;
		num /= 10;
	}
}
int main()
{
    #ifndef ONLINE_JUDGE
    //freopen("/home/lenovo/input.txt", "r", stdin);
   // freopen("o1large.txt","w",stdout);
    #endif
    int tc;
    cin >> tc;
    rep(i,tc) {
    	memset(vis,0,sizeof(vis));
    	int n;
    	cin >> n;
    	if (n == 0) {
    		cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
    		continue;
    	}
    	int ans = 0;
    	for (int j = 1; j <= 73; j++) {
    		int cur = j*n;
    		mark(cur);
    		if (viscnt() == 10) {
    			ans = cur;
    			break;
    		}
    	}
    	cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}