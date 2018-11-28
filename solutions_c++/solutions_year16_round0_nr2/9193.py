#include <bits/stdc++.h>
#define fu(i, a, n) for (int i = a; i < n; i++)
#define fd(i, n, a) for (int i = n; i >= a; i--)
#define rep(i,n) fu(i,0,n)
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define pii pair<int,int>
#define vi vector<int>
#define vpii vector<pii>
#define sl(x) scanf("%lld", &x); //sl(x) is for long long int.
#define si(x) scanf("%d", &x);
#define pl(x) printf("%lld", x);  //pl(x) is for long long int.
#define pln(x) printf("%lld\n", x);  //..n(x) is for printing with New Line.
#define ps(x) printf("%lld ", x);  //..s(x) is for printing with Space.
#define pi(x) printf("%d", x);
#define pin(x) printf("%d\n", x);
#define pis(x) printf("%d ", x);
#define gc getchar_unlocked
#define ll long long
using namespace std;
int readi() {int n=0,sign=false;char c = gc();
	while (c < '0' || c > '9') { if (c == '-') sign=true; c=gc();}
	while (c>='0' && c<='9') {n=n*10+c-'0';c=gc();}
	if (sign) return -n; return n;
}
ll readl() {ll n=0,sign=false;char c = gc();
	while (c < '0' || c > '9') { if (c == '-') sign=true; c=gc();}
	while (c>='0' && c<='9') {n=n*10+c-'0';c=gc();}
	if (sign) return -n; return n;
}
int main () {
	#ifndef ONLINE_JUDGE
    freopen("/home/sherlock/deep/B-large.in", "r", stdin);
    freopen("/home/sherlock/deep/B-large.out", "w", stdout);
    #endif
    int t;
    string s;
    cin>>t;
    fu(tc,1,t+1) {
    	cin>>s;
    	int sz = s.length();
    	int ans = 0;
    	for (int i=sz-1; i >= 0; i--) {
    		if (s[i]=='-') {
    			ans++;
    			for (int j=0; j <= i; j++) {
    				if (s[j]=='-') s[j] = '+';
    				else s[j] = '-';
    			}
    		}
    	}
    	printf("Case #%d: %d\n",tc,ans);
    }
    return 0;
}