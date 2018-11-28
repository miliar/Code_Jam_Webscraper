#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#pragma comment(linker, "/STACK:102400000,102400000")

using namespace std;
#define   MAX           100005
#define   MAXN          6005
#define   maxnode       15
#define   sigma_size    30
#define   lson          l,m,rt<<1
#define   rson          m+1,r,rt<<1|1
#define   lrt           rt<<1
#define   rrt           rt<<1|1
#define   middle        int m=(r+l)>>1
#define   LL            long long
#define   ull           unsigned long long
#define   mem(x,v)      memset(x,v,sizeof(x))
#define   lowbit(x)     (x&-x)
#define   pii           pair<int,int>
#define   bits(a)       __builtin_popcount(a)
#define   mk            make_pair
#define   limit         10000

//const int    prime = 999983;
const int    INF   = 0x3f3f3f3f;
const LL     INFF  = 0x3f3f;
const double pi    = acos(-1.0);
//const double inf   = 1e18;
const double eps   = 1e-8;
const LL    mod    = 1e9+7;
const ull    mx    = 133333331;

/*****************************************************/
inline void RI(int &x) {
      char c;
      while((c=getchar())<'0' || c>'9');
      x=c-'0';
      while((c=getchar())>='0' && c<='9') x=(x<<3)+(x<<1)+c-'0';
 }
/*****************************************************/

int n,r,p,s;
int x[100];
int y[100];
int flag=0;
char cc[10]="aRPS";
int bb[100];
string ans;

bool da(int a,int b){
    if(a==1&&b==3) return true;
    if(a==2&&b==1) return true;
    if(a==3&&b==2) return true;
    return false;
}
void dfs(int a,int b,int c){
    if(a==r&&b==p&&c==s){
        for(int i=0;i<(1<<n);i++) bb[i]=x[i],y[i]=x[i];
        for(int j=0;j<n;j++){
            int tot=0;
            for(int i=0;i<(1<<(n-j));i+=2){
                if(da(y[i],y[i+1])){
                    y[tot++]=y[i];
                }
                else if(da(y[i+1],y[i])){
                    y[tot++]=y[i+1];
                }
                else return;
            }
        }
        flag=1;
        string bx="";
        for(int i=0;i<(1<<n);i++) bx=bx+cc[bb[i]];
        if(ans=="") ans=bx;
        else if(ans>bx) ans=bx;
        return ;
    }
    //if(flag) return;
    if(a<r){
        x[a+b+c]=1;
        dfs(a+1,b,c);
        x[a+b+c]=0;
    }
    //if(flag) return;
    if(b<p){
        x[a+b+c]=2;
        dfs(a,b+1,c);
        x[a+b+c]=0;
    }//if(flag) return;
    if(c<s){
        x[a+b+c]=3;
        dfs(a,b,c+1);
        x[a+b+c]=0;
    }
    //if(flag) return;
}
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,kase=0;
    cin>>t;
    while(t--){
        scanf("%d%d%d%d",&n,&r,&p,&s);
        kase++;
        mem(x,0);
        flag=0;
        ans="";
        dfs(0,0,0);
        printf("Case #%d: ",kase);
        if(!flag) printf("IMPOSSIBLE\n");
        else{
            cout<<ans<<endl;
        }
    }
    return 0;
}
