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
int A,B,parr[5][5],narr[5][5];
void solve(int cx){
    printf("Case #%d: ",cx);
    SD(A);
    FORE(i,1,4){
        FORE(j,1,4){
            SD(parr[i][j]);
        }
    }
    vector<int>opt;
    FORE(j,1,4){
        opt.PB(parr[A][j]);
    }
    SD(B);
    FORE(i,1,4){
        FORE(j,1,4){
            SD(narr[i][j]);
        }
    }
    sort(ALL(opt));
    int poss=0;
    int ans = -1;
    FORE(j,1,4){
        if(binary_search(opt.begin(),opt.end(),narr[B][j])){
            poss++;
            ans = narr[B][j];
        }
    }
    if(poss==0){
        puts("Volunteer cheated!");
    }else if(poss==1){
        printf("%d\n",ans);
    }else{
        puts("Bad magician!");
    }
}
int main(){
#ifdef LOCAL
    _IN(in);_OUT(out);//TT t("main");//_ERR(err);
#endif
//ios_base::sync_with_stdio(false);
pre();
int T = 1;
SD(T);
FORE(i,1,T){solve(i);}
return 0;
}
