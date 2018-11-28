#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<set>
#include<assert.h>
using namespace std;
#define FOR(i,a,b) for(int i = a; i <= b; ++i)
#define FORD(i,a,b) for(int i = a; i >= b; --i)
#define REP(i,n) FOR(i,0,(n)-1)
#define RI(i,n) FOR(i,1,n)
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
bool debug;
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const int nax = 200;

int testy,n,m;
char t[nax][nax];
int ilosc[nax][nax];

int main(int argc, char * argv[]) {
	debug = argc > 1;
	scanf("%d",&testy);
	FOR(g,1,testy) {
		int res = 0;
		scanf("%d%d",&n,&m);
		FOR(i,1,n) scanf(" %s",t[i]+1);
		FOR(i,0,n) FOR(j,0,m) ilosc[i][j] = 0;
		
		//w lewo
		FOR(i,1,n) {
			int kt = 0;
			FORD(j,m,1) if (t[i][j] != '.') 
				kt = j;
			
			++ilosc[i][kt];
			if (t[i][kt] == '<')
				++res;
		}
		
		//w prawo
		FOR(i,1,n) {
			int kt = 0;
			FOR(j,1,m) if (t[i][j] != '.') 
				kt = j;
			
			++ilosc[i][kt];
			if (t[i][kt] == '>')
				++res;
		}
		
		//w gora
		FOR(j,1,m) {
			int kt = 0;
			FORD(i,n,1) if (t[i][j] != '.') 
				kt = i;
			
			++ilosc[kt][j];
			if (t[kt][j] == '^')
				++res;
		}
		
		//w dol
		FOR(j,1,m) {
			int kt = 0;
			FOR(i,1,n) if (t[i][j] != '.') 
				kt = i;
			
			++ilosc[kt][j];
			if (t[kt][j] == 'v')
				++res;
		}
		
		bool zle = false;
		FOR(i,1,n) FOR(j,1,m) 
			zle |= (ilosc[i][j] == 4);
		
		if (zle)
			printf("Case #%d: IMPOSSIBLE\n",g);
		else
			printf("Case #%d: %d\n",g,res);
	}
	return 0;
}
