// ==========================================================================
//
//                   Bismillahir-Rahmanir-Rahim
//
// ==========================================================================
#include <bits/stdc++.h>
#define        ll                              long long
#define        f(x,y,z)                        for(int x=y;x<z;x++)
#define        take1(a);                       scanf("%d",&a);
#define        take2(a,b);                     scanf("%d%d",&a,&b);
#define        take3(a,b,c);                   scanf("%d%d%d",&a,&b,&c);
#define        take4(a,b,c,d);                 scanf("%d%d%d%d",&a,&b,&c,&d);
#define        pii                             pair<int,char>
#define        mem(a,x)                        memset(a,x,sizeof(a))
#define        N                               1000010
#define        M                               1000000007
#define        pi                              acos(-1.0)
#define        ff                              first
#define        ss                              second
#define        pb                              push_back
#define        inf                             (int)1e9
using namespace std;
int dx[]={0,0,1,-1,-1,-1,1,1};
int dy[]={1,-1,0,0,-1,1,1,-1};
template < class T> inline T gcd(T a, T b){while(b){a%=b;swap(a,b);}return a;}
template <typename T> string NumberToString ( T Number ) { ostringstream ss; ss << Number; return ss.str(); }
inline int nxt(){int aaa;scanf("%d",&aaa);return aaa;}
inline ll lxt(){ll aaa;scanf("%lld",&aaa);return aaa;}
template <class T> inline T bigmod(T p,T e,T m){T ret = 1;
for(; e > 0; e >>= 1){
    if(e & 1) ret = (ret * p) % m;p = (p * p) % m;
} return (T)ret;}
#define sayed
#ifdef sayed
     #define debug(args...) {cerr<<"Debug: "; dbg,args; cerr<<endl;}
#else
    #define debug(args...)  // Just strip off all debug tokens
#endif
struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;
///******************************************START******************************************
char a[150], b[150];
char neg = '-';
char pos = '+';
vector<pii> v;
int main()
{
	 //freopen("out.txt","w",stdout);
	int n = nxt(); int cs = 1;
	getchar();
	while (n--){
		cin >> a;
		int pls = 0; int step = 0;
		int len = strlen(a);
		for (int i = 0; i<len; i++){
			if (a[i] == '-'){
				int c = 0;
				while (a[i] == '-'){
					c++; i++;
				}
				i--;
				v.pb(pii(c, '-'));
			}
			else {
				int c = 0;
				while (a[i] == '+'){
					c++; i++;
				}
				i--;
				v.pb(pii(c, '+'));

			}
		}
		while (!v.empty()){
			if (v[0].ss == '-'){
				v.erase(v.begin(), v.begin() + 1);
				step++;
			}
			else {
				pii x = v[0];
				v.erase(v.begin(), v.begin() + 1);
				if (v.empty()){
					break;
				}
				else {
					int in; int mx = 0;
					for (int i = 0; i<v.size(); i++){
						if (v[i].ss == '-'){
							if (v[i].ff>mx){

								mx = v[i].ss;
								in = i;
							}
						}
					}
					v[in].ff += x.ff;
					step++;
				}
			}


		}
		printf("Case #%d: %d\n", cs++, step);
		v.clear();
	}

	return 0;
}

