/* theCodeGame */
//{{{
#include<iostream>
#include<algorithm>
#include<cmath>
#include<climits>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<stack>
#include<bitset>
#include<set>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<map>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<cctype>
//#undef thecodegame
#ifdef thecodegame
    #include<debug.h>
#else
    #define DBG_ARR(a,b,c) {}
    #define DBG_MAT(a,s,b,c) {}
    #define DBG_VECT(a) {}
    #define db(...) {}
    #define dbt(x, ...) {}
#endif

using namespace std;

#define assert(f) {if(!(f)){fprintf(stderr,"Line-->%d  Assertion failed: %s \n",__LINE__,#f);exit(1);}}
#define MOD 	 1000000007LL
#define LL 		 long long
#define ULL      unsigned long long
#define ABS(x)   ((x)<0?-(x):(x))
#define SQR(x) 	 ((x)*(x))
#define CUBE(x)  ((x)*(x)*(x))
#define SD(n)    scanf("%d",&n)
#define SD2(n,m) scanf("%d %d",&n,&m)
#define SLL(n)   scanf("%LLd",&n)
#define SLU(n)   scanf("%LLu",&n)
#define SS(n)    scanf("%s",n)
#define pnl      printf("\n")
#define REP(i,n)        for(__typeof(n) i=0;i<(n);i++)
#define FOR(i,a,b)      for(__typeof(b) i=(a);i<(b);++i)
#define FORE(i,a,b)     for(__typeof(b) i=(a);i<=(b);++i)
#define FORD(i,a,b,d)   for(__typeof(b) i=(a);i<(b);i+=(d))
#define FORR(i,n,e)     for(__typeof(n) i=(n);i>=(e);--i)
#define FORRD(i,n,e,d)  for(__typeof(n) i=(n);i>=(e);i-=(d))
#define REP_IT(it,m)    for(it=m.begin();it!=m.end();it++)
#define FORI(it,s) 	    for(__typeof((s).begin()) (it)=(s).begin();(it)!=(s).end();(it)++)
#define FOREACH(it, X)  for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define UNIQUE(v)       sort(aLL(v)),v.erase(unique(aLL(v)),v.end())
#define FILL(a,b)       memset(a,b,sizeof(a))
#define ALL(v)          (v).begin(), (v).end()
#define RALL(v)         (v).rbegin(), (v).rend()
#define checkbit(n,b)    ( ((n) >> (b)) & 1)
#define pb push_back
#define mp make_pair
#define XX first
#define YY second

const double PI=acos(-1.0);
const double EPS=1e-11;
template<typename T>inline T mod(T N,T M){return (N%M+M)%M;}
template<typename T>inline void checkmin(T &a,T b){if(b<a)a=b;}
template<typename T>inline void checkmax(T &a,T b){if(b>a)a=b;}
class minHeap{public:bool operator()(int& c1,int& c2){return c1>c2;}};
class maxHeap{public:bool operator()(int& c1,int& c2){return c1<c2;}};


//}}}
#define SIZE 20
#define MAXX 100000009
char s[6][7];
char temp[6][7];
int tc,cs=1,c,k1,k;
char ch;
bool flagX,flag0;
void precompute(){
    REP(i,6){
        s[i][0]='Z';
        s[i][5]='Z';
    }
    REP(j,6){
        s[0][j]='Z';
        s[5][j]='Z';
    }

}//end precompute

void doThis(int cs){
    flagX=false;
        flag0=false;
        for(int i=0;i<4;i++)
            scanf("%s",temp[i]);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                s[i+1][j+1]=temp[i][j];
        int dot=0;
        for(int i=1;i<5;i++){
            for(int j=1;j<5;j++){
                //cout<<"Xizzt\n";
                ch=s[i][j];
                if(ch=='.'){
                    dot++;
                    continue;
                }

                k=i+1;
                c=0;
                while(k<5){
                    if(s[k][j]==ch || s[k][j]=='T')
                        c++;
                    k++;
                }
                k=i-1;
                while(k>0){
                    if(s[k][j]==ch || s[k][j]=='T')
                        c++;
                    k--;
                }
                //cout<<c<<endl;
                if(c==3){
                    if(ch=='X')
                        flagX=true;
                    else
                        flag0=true;
                    break;
                }
                c=0;
                k=j+1;
                while(k<5){
                    if(s[i][k]==ch || s[i][k]=='T')
                        c++;
                    k++;
                }
                k=j-1;
                while(k>0){
                    if(s[i][k]==ch || s[i][k]=='T')
                        c++;
                    k--;
                }
                //cout<<c<<endl;
                if(c==3){
                    if(ch=='X')
                        flagX=true;
                    else
                        flag0=true;
                    break;
                }
                k=i+1;
                k1=j+1;
                c=0;
                while(k<5 && k1<5){
                    if(s[k][k1]==ch || s[k][k1]=='T')
                        c++;
                    k++;
                    k1++;
                }
                k=i-1;
                k1=i-1;
                while(k>0 && k1>0){
                    if(s[k][k1]==ch || s[k][k1]=='T')
                        c++;
                    k--;
                    k1--;
                }
                //cout<<c<<endl;
                if(c==3){
                    if(ch=='X')
                        flagX=true;
                    else
                        flag0=true;
                    break;
                }

                k=i-1;
                k1=j+1;
                c=0;
                while(k>0 && k1<5){
                    if(s[k][k1]==ch || s[k][k1]=='T')
                        c++;
                    k--;
                    k1++;
                }
                k=i+1;
                k1=j-1;
                while(k<5 && k1>0){
                    if(s[k][k1]==ch || s[k][k1]=='T')
                        c++;
                    k++;
                    k1--;
                }
                //cout<<c<<endl;
                if(c==3){
                    if(ch=='X')
                        flagX=true;
                    else
                        flag0=true;
                    break;
                }

            }
            if(flagX || flag0)
                break;
        }
        if(flagX)
            printf("Case #%d: X won\n",cs++);
        else if(flag0)
            printf("Case #%d: O won\n",cs++);
        else if(dot)
            printf("Case #%d: Game has not completed\n",cs++);
        else
            printf("Case #%d: Draw\n",cs++);
        getchar();

}//end solve

int main(){
#ifdef amy
	freopen("C:\\A\\in.txt","r",stdin);freopen("C:\\A\\out.txt","w",stdout);freopen("C:\\A\\out.txt","w",stderr);
#endif
precompute();
int cases = 1;
scanf("%d",&cases);
FORE(i,1,cases){doThis(i);}
return 0;
}//end main
