#include <bits/stdc++.h>
#define f(i,x,y) for (int i = x; i < y; i++)
#define fd(i,x,y) for(int i = x; i>= y; i--)
#define FOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define vint vector<int>
#define ll long long
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define pii pair<int,int>
#define fst first
#define snd second
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define eps (1e-9)
#define oo (1<<30)
#define SZ(a) (int)a.size()
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; f(i,0,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; f(i,0,m)f(j,0,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define N 1
using namespace std;
template<class T> inline void mini(T &a,T b){if(b<a) a=b;}
template<class T> inline void maxi(T &a,T b){if(b>a) a=b;}

int tc, caso;
int n;
ll g(ll i) {
	int t = 0;
	ll p = 1;
	while(p-1 <= i) {
		p <<= 1;
		t++;
	}
	t--;
	return (1LL<<n) - (1LL<<n-t);
}
ll h(ll i) {
	ll todo = (1LL<<n) - 1;
	return todo - g(todo-i);
}
ll best(ll p) {
	ll lo = 0, hi = 1LL<<n;
	while(lo < hi) {
		ll i = (lo + hi) >> 1;
		if (g(i) >= p) hi = i;
		else lo = i+1;
	}
	return lo-1;
}
ll worst(ll p) {
	ll lo = 0, hi = 1LL << n;
	while(lo < hi) {
		ll i = (lo + hi) >> 1;
		if (h(i) >= p) hi = i;
		else lo = i+1;
	}
	return lo-1;
}

int main(){
//	n = 3;
//	f(i,0,8) cout << g(i) << endl;
	cin >> tc;
	while(tc--) {
		ll p;
		cin >> n >> p;
		printf("Case #%d: ", ++caso);
		cout << best(p) << " " << worst(p) << endl;
	}
}

