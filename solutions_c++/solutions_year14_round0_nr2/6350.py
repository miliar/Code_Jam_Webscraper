/* theCodeGame */

//AB KI BAAR MODI SARKAR


#include<bits/stdc++.h>
//#undef DEBUG
#ifdef DEBUG
    #include<debug.h>
#else
    #define db(...) {}
    #define dbt(...) {}
	#define pprintf(...) {}
#endif
using namespace std;
#define ASSERT(f)       if(!(f)){fprintf(stdout,"Line-->%d  Assertion failed: %s\n",__LINE__,#f);exit(1);}
#define MOD 	        1000000007LL
#define ABS(x)          ((x)<0?-(x):(x))
#define SQR(x) 	        ((x)*(x))
#define CUBE(x)         ((x)*(x)*(x))
#define pnl             printf("\n");
#define REP(i,n)        for(__typeof(n) i=0;i<(n);i++)
#define FOR(i,a,b)      for(__typeof(b) i=(a);i<(b);++i)
#define FORE(i,a,b)     for(__typeof(b) i=(a);i<=(b);++i)
#define FORD(i,a,b,d)   for(__typeof(b) i=(a);i<(b);i+=(d))
#define FORR(i,n,e)     for(__typeof(n) i=(n);i>=(e);--i)
#define FORRD(i,n,e,d)  for(__typeof(n) i=(n);i>=(e);i-=(d))
#define FOREACH(i,s) 	for(__typeof((s).begin()) i=(s).begin();i!=(s).end();i++)
#define UNIQUE(v)       sort(ALL(v)),v.erase(unique(ALL(v)),v.end())
#define FILL(a,b)       memset(a,b,sizeof(a))
#define ALL(v)          (v).begin(), (v).end()
#define RALL(v)         (v).rbegin(), (v).rend()
#define checkbit(n,b)   (((n)>>(b))&1)
#define PB push_back
#define MP make_pair
#define XX first
#define YY second
template<typename T>inline void SD(T &n){
    #define g getchar_unlocked()
    n=0;int c=g,s=1;while(c<'0'||c>'9'){if(c=='-')s=-1;c=g;}while(c>='0'&&c<='9'){n=(n<<3)+(n<<1)+c-'0',c=g;}n=n*s;
    #undef g
}
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
#define SIZE 1000001
void pre(){
}
double C,F,X;
void solve(int cx){
    printf("Case #%d: ",cx);
    scanf("%lf %lf %lf",&C,&F,&X);
    double CR = 2;//rate
    double ttime = 0;//current time
    double cookies = 0;//current cookies
    while(true){
        double thisRateFinishTime = ttime + (X-cookies)/CR;
        double timeToNextRate = ttime + (C-cookies)/CR;
        double timeToFinishNow = timeToNextRate + (X)/(CR+F);
        if(thisRateFinishTime>timeToFinishNow){
            ttime = timeToNextRate;
            cookies=0.0;
            CR = CR+F;
        }else{
            ttime = thisRateFinishTime;
            break;
        }
    }
    printf("%.7lf\n",ttime);
}
int main(){
#ifdef LOCAL
    _IN(in);_OUT(out);TE t("main");//_ERR(err);
#endif
//ios_base::sync_with_stdio(false);
pre();
int T = 1;
//SD(T);
scanf("%d\n",&T);
FORE(i,1,T){solve(i);}
return 0;
}
