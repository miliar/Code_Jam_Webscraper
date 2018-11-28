// Author : XeRoN!X

#ifdef OFFLINE_VS_EXECUTION
	#include "template_includes.hpp"
	#define FREAD fread
	#define FWRITE fwrite
#else
	#include <bits/stdc++.h>
	#define FREAD fread_unlocked
	#define FWRITE fwrite_unlocked
#endif

#define TR(c,i) for ( auto i = (c).begin(); i != (c).end(); i++ )

#define FOR(i,a,b) for( i = a; i <= int(b); i++ )
#define ROF(i,a,b) for( i = a; i >= int(b); i-- )
#define MEM(t,n) ( t * )malloc( (n)*sizeof( t ) )
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort( ALL(v) )
#define RSORT(v) sort( ALL(v), greater<int>() )
#define SET(x,a) memset(x,a,sizeof(x))
#define IN(x,a) (x.find(a) != x.end())

#define DIST(x1,y1,x2,y2) SQ(x1-x2)+SQ(y1-y2)
#define DISTS(p,q) SQ(p.x-q.x)+SQ(p.y-q.y)
#define SQ(x) ((x)*(x))
#define MP make_pair

#define DEB(x) cout << #x << " = " << x << endl;
#define DEBA(x,n) { int i; cout << "{\n"; FOR(i,0,n-1)cout << i << " " << x[i] << endl; cout << "}\n"; }
#define DEBT(x) { cout << "{\n"; TR( x,it ) cout << *it << "\n" ; cout << "}\n"; }
#define DEBM(x) { cout << "{\n"; TR( x,it ) cout << it->F << " : " << it->S << "\n"; cout << "}\n"; }

#define SYNC ios_base::sync_with_stdio(false);
#define C(format,n) scanf( "%"#format, &n )
#define CS(s) scanf( "%s", s )
#define P(format,n) printf( "%"#format, n )

//#define LIM
#ifdef LIM
	char S, *inp, *out, *ipos, *opos, DIG[30], *line;
	#define FRMI inp=( char * )malloc( LIM*sizeof( char ) );FREAD( inp,1,LIM,stdin );ipos=inp;
	#define FWM out=( char * )malloc( LIM*sizeof( char ) );opos=out;
	#define FWO FWRITE( out,opos-out,1,stdout );
	#define GETI(n) n=0;while(*ipos<33){ipos++;}if(*ipos=='-'){S=-1;ipos++;}else{S=1;}while(*ipos>='0'){n=10*n+(*ipos-'0');ipos++;}n*=S;
	#define GETS(s) while(*ipos<33){ipos++;}D=0;while(*ipos>33){s[D++]=*ipos++;}s[D]='\0';
	#define GETC(c) while(*ipos<33){ipos++;}c=*ipos++;
	#define PUTI(n) O=n;D=0;if(O<0){*opos++='-';O*=-1;}if(!O)*opos++='0';else{while(O){Y=O/10;DIG[D++]=O-Y*10+'0';O=Y;}\
	while (D--)*opos++ = DIG[D]; }
	#define PUTS(s) line=#s;while(*line)*opos++=*line++;
	#define PUTC(c) *opos++=c;
#endif

using namespace std;

template<class T1, class T2> inline T2 gcd(T1 a, T2 b){ while (!b) { T1 temp = a % b; a = b; b = temp; } }
template<class T> inline string tostring(T n){ stringstream ss; ss << n; ss.flush(); return ss.str(); }
template<class T> inline string tobinary(T n){ string s = n ? "" : "0"; while (n) { s += ((n & 1) + '0'); n >>= 1; } return s; }
template<class T> inline int digits(T n){ int cnt = n ? 0 : 1; while (n) { n /= 10; cnt++; } return cnt; }
template<class T> inline T abs(T a){ return a < 0 ? -a : a; }


#define SQRT2 1.41421356237

int main()
{
	SYNC;

#ifdef OFFLINE_VS_EXECUTION
	freopen("..\\input.txt", "r", stdin);
	freopen("..\\output.txt", "w", stdout);
#endif

	int T, t, i;
	char s[1010];
	int sl, ans, stand;

	scanf("%d", &T);

	FOR (t,1,T) {
		scanf("%d%s", &sl, s);
		ans = 0;
		stand = s[0]-'0';

		FOR(i, 1, sl) {
			if (s[i] > '0') {
				if (stand < i) {
					ans += (i-stand);
					stand = i;
				}
				stand += (s[i]-'0');
			}
		}

		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}
