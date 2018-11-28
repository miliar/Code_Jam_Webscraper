/*-------------icalFikr's template v2.0 BETA-------------*/

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
#include <cctype>
#include <utility>
#include <ctime>

/* Abbreviations */
#define _puf push_front
#define _pof pop_front()
#define _pub push_back
#define _pob pop_back()
#define fs first
#define sc second
#define mp make_pair
#define FOR(i,a,b) for(int i=int(a),_b=int(b);i<=_b;i++)
#define FORD(i,a,b) for(int i=int(a),_b=int(b);i>=_b;i--)
#define open freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
#define close fclose(stdin); fclose(stdout);
#define set_time time_start(&tt)
#define out_time print_time(tt)
#define ALL(v) (v).begin(),(v).end()
#define sz size()
#define reset(x,N) memset(x,N,sizeof(x))
#define nl puts("")
#define gc getchar()
#define PI acos(-1)

using namespace std;
typedef double db;
typedef long long ll;
typedef pair <int,int> ii;
typedef pair <string,int> si;
typedef vector <ii> vii;
typedef vector <int> vi;
typedef vector <char> vc;
typedef vi::iterator it;

const db EPS = 0.0000001;		// epsilon 10^(-7)
const ll INF = 1LL<<36;			// infinity 2^36

/* Template function(s) */
template<typename T>
inline T getnum() {
    T num=0; char c;
    do { c=gc; } 
    while (c!=EOF && c==' ' && c=='\n' && c=='\t');
    
    int sign=(c=='-' ? -1 : 1);
    if (c!='-') num+=(c-'0');
    
    while ( (c=gc)!=EOF && c!='\n' && c!='\t' && c!=' ') {
        num*=10; num+=(c-'0');
    }
    num*=sign; return num;
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
        str._pub(k);
    return str;
}

/*-------------end of template-------------*/
const ll MAX=10000;
db c,f,x;

int main(){
	//open
	int t; scanf("%d",&t);
	FOR(tt,1,t) {
		printf("Case #%d: ",tt);
		scanf("%lf%lf%lf",&c,&f,&x);
		db ans=(db)(1e6),tm,sp;
		FOR(i,0,MAX) {
			tm=0,sp=2;
			FOR(j,1,i) {
				tm+=c/sp;
				sp+=f;
			}
			ans=fmin(ans,tm+x/sp);
		}
		printf("%.8lf\n",ans);
	}
	//close
	return 0;
}