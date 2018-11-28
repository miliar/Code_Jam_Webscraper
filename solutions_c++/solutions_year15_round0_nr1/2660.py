#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define inf 1000000000
#define maxn 5000

#define ll long long
#define pii pair<int, int>
#define pb push_back
#define sin scanint
#define bitcount(x) __builtin_popcount(x)
#define fill(s, p) memset(s, p, sizeof(s));

#ifdef ONLINE_JUDGE
#define gc getchar_unlocked
#endif

#ifndef ONLINE_JUDGE
#define gc getchar
//freopen("input.txt", "r", stdin)
//freopen("output.txt", "w", stdout)
#endif

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

ll modpow(ll a, ll b)
{
	ll x=1ll, y=a;
	while(b){
		if(b%2)
			x=(x*y)%MOD;
		y=(y*y)%MOD;
		b/=2;
	}
	return x;
}

ll gcd(ll a, ll b)
{
	if(a%b==0)
		return b;
	else
		return gcd(b, a%b);
}

char str[maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, n, i, j, ctn, req, case_num=1;
	sin(t);
	while(t--){
		sin(n);
		scanf("%s", str);
		ctn = req = 0;
		for(i=0; i<=n; i++){
			if(str[i]>'0'){
				if(ctn<i){
					req+=(i-ctn);
					ctn+=(i-ctn);
				}
			}
			ctn+=(str[i]-'0');
			//cout << ctn << " " << req << endl;			
		}
		printf("Case #%d: %d\n", case_num++, req);
	}
	return 0;
}