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

#define set(bm,i,e) ((bm)=(bm)|((e)<<(i)))
#define index(bm,i) ( ((bm)>>(i))&1 )
char s[15];
int d[1500],n,init;

int fnbm(int bm, int i) {
	int nbm=0;
	forn(j,n) 
		if (j>i) set(nbm,j,index(bm,j));
		else set(nbm,j,!index(bm,i-j));
		
	return nbm;
}
//~ int fnbm(int bm, int i) {
	//~ int nbm=0;
	//~ forn(j,n) 
		//~ if (j>i) nbm = nbm | (bm&(1<<j));
		//~ else if ( ( bm & (1<<(i-j)) ) == 0 ) nbm = nbm | (1<<j);
		//~ 
	//~ return nbm;
//~ }

int main() {
	//~ freopen("b.in", "r", stdin);
	//~ freopen("asd.in", "r", stdin);
	//~ freopen("asd.out", "w", stdout);
    ios::sync_with_stdio(0);
    int TC; scanf("%d",&TC);
    for(int tc=1 ; tc<=TC ; tc++) {
		scanf("%s",s);
		init=0; n=strlen(s);
		forn(i,n) if (s[i]=='+') init = init | (1<<i);
		memset(d,-1,sizeof(d));
		queue<int> q;
		d[init]=0; q.push(init);
		while(sz(q)) { int bm = q.front(); q.pop();
			forn(i,n) { int nbm = fnbm(bm,i);
				if ( d[nbm]==-1 ) {
					q.push(nbm);
					d[nbm]=d[bm]+1;
				}
			}
		}
		printf("Case #%d: %d\n",tc,d[(1<<n)-1]);
	}
	return 0;
}
