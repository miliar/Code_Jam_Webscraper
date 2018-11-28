#include <bits/stdc++.h>
using namespace std;
#define dprint(v) cerr << #v"=" << v << endl //;)
#define forr(i,a,b) for(int i=(a); i<(b); i++)
#define forn(i,n) forr(i,0,n)
#define dforn(i,n) for(int i=n-1; i>=0; i--)
#define forall(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define sz(c) ((int)c.size())
#define zero(v) memset(v, 0, sizeof(v))
#define fst first
#define snd second
#define mkp make_pair
#define pb push_back
typedef long long ll;
typedef pair<int,int> ii;

const int MAXN=100100;
ll n;
bool is[10];
void procdigit(ll x) {
	is[x%10]=true;
	if (x>9) procdigit(x/10);
}
int cant() {
	int c = 0;
	forn(i,10) c+=is[i];
	return c;
}

int main() {
	//~ freopen("asd.in", "r", stdin);
	//~ freopen("asd.out", "w", stdout);
    ios::sync_with_stdio(0);
    int TC; scanf("%d",&TC);
    for(int tc=1 ; tc<=TC ; tc++) {
		scanf("%lld",&n);
		if (n==0) printf("Case #%d: INSOMNIA\n",tc);
		else {
			zero(is);
			int i;
			ll sn = n;
			for(i=0 ; cant() < 10 ; i++) {
				procdigit(sn);
				sn+=n;
			}
			printf("Case #%d: %lld\n",tc,sn-n);
		}
	}
	return 0;
}
