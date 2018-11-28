// @author peter50216
// #includes {{{
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<functional>
#include<math.h>
#include<assert.h>
#include<stdarg.h>
#include<time.h>
#include<limits.h>
#include<ctype.h>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<vector>
#include<iostream>
#include<sstream>
using namespace std;
// }}}
// #defines {{{
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define REP(i,n) for(int i=0;i<(n);i++)
#define REP1(i,a,b) for(int i=(a);i<=(b);i++)
#define REPL(i,x) for(int i=0;x[i];i++)
#define PER(i,n) for(int i=(n)-1;i>=0;i--)
#define PER1(i,a,b) for(int i=(a);i>=(b);i--)
#define RI(x) scanf("%d",&x)
#define DRI(x) int x;RI(x)
#define RII(x,y) scanf("%d%d",&x,&y)
#define DRII(x,y) int x,y;RII(x,y)
#define RIII(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define DRIII(x,y,z) int x,y,z;RIII(x,y,z)
#define RS(x) scanf("%s",x)
#define PI(x) printf("%d\n",x)
#define PIS(x) printf("%d ",x)
#define CASET int ___T,cas=1;scanf("%d ",&___T);while(___T--)
#define CASEN0(n) int cas=1;while(scanf("%d",&n)!=EOF&&n)
#define CASEN(n) int cas=1;while(scanf("%d",&n)!=EOF)
#define MP make_pair
#define PB push_back
#define MS0(x) memset(x,0,sizeof(x))
#define MS1(x) memset(x,-1,sizeof(x))
#define SEP(x) ((x)?'\n':' ')
#define F first
#define S second
#ifdef ONLINE_JUDGE
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILEIO(x) ;
#define FILEIOS ;
#endif
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;
// }}}

int n;
int id[11];
struct XD{
    int x,y;
    void get(){
        scanf("%d%d",&x,&y);
    }
    XD(int xx,int yy):x(xx),y(yy){}
    XD(){}
    XD operator-(const XD& b)const{
        return XD(x-b.x,y-b.y);
    }
    int operator^(const XD& b)const{
        return x*b.y-y*b.x;
    }
    int operator*(const XD& b)const{
        return x*b.x+y*b.y;
    }
}in[11];
int ans[11];
int SG(int x){
    if(x==0)return 0;
    return x>0?1:-1;
}
int tri(const XD& a,const XD& b,const XD& c){
    return (b-a)^(c-a);
}
int ins(const XD& a,const XD& b,const XD& c){// b -- a -- c
    return (b-a)*(c-a)<=0;
}
bool sect(const XD& a,const XD& b,const XD& c,const XD& d){
    int tc=tri(a,b,c);
    int td=tri(a,b,d);
    int ta=tri(c,d,a);
    int tb=tri(c,d,b);
    if(SG(tc)==0&&SG(td)==0){
        return ins(a,c,d)||ins(b,c,d)||ins(c,a,b)||ins(d,a,b);
    }else{
        return SG(tc)*SG(td)<=0&&SG(ta)*SG(tb)<=0;
    }
}
int main(){
    CASET{
        RI(n);
        REP(i,n)in[i].get();
        REP(i,n)id[i]=i;
        fprintf(stderr,"%d\t",cas);
        fflush(stderr);
        printf("Case #%d:",cas++);
        int ma=0;
        do{
            id[n]=id[0];
            bool f=1;
            REP(i,n){
                REP1(j,i+2,n-1){
                    if(j==n-1&&i==0)continue;
                    if(sect(in[id[i]],in[id[i+1]],in[id[j]],in[id[j+1]])){
                        //printf("%d %d - %d %d\n",id[i],id[i+1],id[j],id[j+1]);
                        f=0;
                        break;
                    }
                }
                if(!f)break;
            }
            if(!f)continue;
            int a=0;
            REP(i,n)a+=(in[id[i]].y+in[id[i+1]].y)*(in[id[i]].x-in[id[i+1]].x);
            if(a<0)a=-a;
            if(a>ma){
                ma=a;
                REP(i,n)ans[i]=id[i];
            }
        }while(next_permutation(id,id+n));
        REP(i,n)printf(" %d",ans[i]);puts("");
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread

