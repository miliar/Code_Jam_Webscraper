/*-------------icalFikr's template v2.1--------------*/

#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <bitset>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cstdlib>
#include <cmath>
#include <complex>
#include <algorithm>
#include <iomanip>
#include <cstddef>
#include <cassert>
#include <cctype>
#include <utility>
#include <ctime>

#ifndef GEDEBUG
	#define DEBUG printf(__VA_ARGS__)
	#define DEBUGS puts("gukguk")
	#define TIME() printf("\nFinished in %.3lf s\n",clock()/(double)CLOCKS_PER_SEC)
#else
	#define DEBUG
	#define DEBUGS
	#define TIME()
#endif

#ifdef __WIN32__
	char getchar_unlocked() { return getchar(); }
#endif

/* Abbreviations */
#define puf push_front
#define pof pop_front()
#define pub push_back
#define pob pop_back()
#define fs first
#define sc second
#define mp make_pair
#define FOR(i,a,b) for(int i=int(a),_b=int(b);i<=_b;i++)
#define FORD(i,a,b) for(int i=int(a),_b=int(b);i>=_b;i--)
#define FOREACH(i,a) for (__typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define OPEN freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
#define CLOSE fclose(stdin); fclose(stdout);
#define ALL(v) (v).begin(),(v).end()
#define sz size()
#define reset(x,N) memset(x,N,sizeof(x))
#define nl puts("")
#define gc getchar_unlocked()

using namespace std;
typedef double db;
typedef long long LL;
typedef pair <int,int> ii;
typedef pair <LL,LL> pll;
typedef vector <ii> vii;
typedef vector <int> vint;

const db EPS	= 0.0000001;		
const db PI 	= acos(-1);			
const LL INFLL	= 0x7FFFFFFFFFFFFFFF;
const int INF	= 0x7FFFFFFF;

template<typename T>
inline void next(T &num) {
    char c; num=0;	
    do { c=gc; } 
    while (c!=EOF && c==' ' && c=='\n' && c=='\t');
    int sign=(c=='-' ? -1 : 1);
    if (c!='-') num+=(c-'0');
    while ( (c=gc)!=EOF && c!='\n' && c!='\t' && c!=' ') {
        num*=10; num+=(c-'0');
    }
    num*=sign;
}

inline string getstr() {
    string str; char k;
    while( (k=gc)==' ' || k=='\n' )
    {
        k=gc;
        if ( k==' ' || k=='\n' ) continue;
        else break;
    }
    while((k=gc)!=EOF &&k!='\n' && k!='\t'
        && k!='\v' && k!='\0' && k!=' ')
        str.pub(k);
    return str;
}

/*-------------end of template-------------*/
#define keluar(); { puts("Fegla Won"); goto lala; }
typedef pair<char,int> ci;
const int MAX=105;
char s[MAX],t;
vector<int> amo[MAX];
vector<char> kar;
int x,cs,sumKar[MAX],res;

int main() {
	next(cs);
	FOR(i,1,cs) {
		kar.clear();
		FOR(j,0,MAX-1) amo[j].clear();
		reset(sumKar,0);
		printf("Case #%d: ",i);
		next(x);
		gets(s);
		FOR(i,0,strlen(s)-1) {
			t=s[i];
			kar.pub(t);
			int len=0;
			while (i+len<strlen(s) && s[i+len]==t) len++;
			sumKar[kar.sz-1]+=len;
			amo[kar.sz-1].pub(len);
			//printf("%c %d ",t,len);
			i+=(len-1);
		}
		FOR(j,1,x-1) {
			int ltr=0;
			gets(s);
			FOR(i,0,strlen(s)-1) 
			if (ltr<kar.sz && s[i]==kar[ltr]) {
				t=s[i];
				int len=0;
				while (i+len<strlen(s) && s[i+len]==t) len++;
				amo[ltr].pub(len);
				sumKar[ltr]+=len;
				ltr++;
				i+=(len-1);
			} else { keluar(); }
			//cout<<ltr<<kar.sz; nl;
			if (ltr < (kar.sz)) {keluar();}
		}
		
		res=0;
		FOR(i,0,kar.sz-1) {
			sort(ALL(amo[i]));
			int ans=amo[i][amo[i].sz/2];
			FOR(j,0,amo[i].sz-1) res+=abs(amo[i][j]-ans);
		}
		cout<<res; nl;
		lala: continue;
	}
	return 0;
}