#pragma comment(linker, â��/STACK:36777216â��)
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <ctime>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <cmath>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ldb;
#define mp make_pair
#define pb push_back
int _buf;
inline int in(){
   scanf("%d", &_buf);
   return _buf;
}
const int INF=~(1<<31);

vector<vector<pair<int,int> > >g;
vector<vector<int> > par, mi;
vector<int> tin, tout;
int timer=1;
int nn;
bool upper(int a, int b){
   if(tin[a]<=tin[b] && tout[a]>=tout[b]) return true;
   else return false;
}
void dfs(int v, int p, int cost){
   par[v][0]=p;
   mi[v][0]=cost;
   tin[v]=timer++;
   for(int i=1;i<=nn;++i){
       par[v][i]=par[par[v][i-1]][i-1];
       mi[v][i]=max(mi[v][i-1], mi[par[v][i-1]][i-1]);
   }
   for(int i=0;i<g[v].size();++i){
       int to=g[v][i].first;
       if(to==p) continue;
       dfs(to, v, g[v][i].second);
   }
   tout[v]=timer++;
}
int getres(int a, int b){
   int res=-INF;
   int aa=a, bb=b;
   for(int i=nn;i>=0;--i){
       if(!upper(par[a][i], b)){
           res=max(res, mi[a][i]);
           a=par[a][i];
       }
   }
   if(!upper(aa,bb))
       res=max(res, mi[a][0]);
   a=aa;
   b=bb;
   for(int i=nn;i>=0;--i){
       if(!upper(par[b][i], a)){
           res=max(res, mi[b][i]);
           b=par[b][i];
       }
   }
   if(!upper(bb,aa))
   res=max(res, mi[b][0]);
   return res;
}
vector<int> h;
int get(int a){
   if(h[a]==a) return a;
   return h[a]=get(h[a]);
}
void link(int a, int b){
   a=get(a);
   b=get(b);
   if(rand()&1) swap(a,b);
   h[a]=b;
}
int mas[50000];
int cou[100000], digs[100000];
int main(){

   iostream::sync_with_stdio(0);
   int n=in();
   int m=in();
   for(int i=0;i<n;++i){
       digs[i]=in();
   }
   int digc=n-1;
   for(int i=0;i<m;++i){
       char c;
       int a,b;
       scanf("\n%c %d %d", &c, &a, &b);
       if(c=='c') digs[++digc]=b;
   }
   rewind(stdin);
   n=in();
   m=in();
   sort(digs, digs+digc+1);
   digc=unique(digs, digs+digc+1)-digs;
   for(int i=0;i<n;++i){
       mas[i]=lower_bound(digs, digs+digc, in())-digs;
   }
   map<int,int> tor;
   vector<int> rp(n+1,n);
   vector<int> invrp(n+1,n);
   for(int i=n-1;i>=0;--i){
       if(tor.count(mas[i])!=0){
           rp[i]=tor[mas[i]];
           invrp[tor[mas[i]]]=i;
       }
           tor[mas[i]]=i;

   }
   int sq=sqrt(n+0.)+1;
   vector<vector<int> > g(sq, vector<int>()), gr(sq, vector<int>());
   for(int i=0;i<n;++i){
       g[i/sq].pb(rp[i]);
   }
   for(int i=0;i<n;++i){
       gr[i/sq].pb(mas[i]);
   }
   for(int i=0;i<sq;++i){
       sort(g[i].begin(), g[i].end());
   }
   for(int i=0;i<sq;++i){
       sort(gr[i].begin(), gr[i].end());
   }
   for(int i=0;i<m;++i){
       char c;
       int a,b;
       scanf("\n%c %d %d", &c, &a, &b);
       if(c=='c'){
           b=lower_bound(digs, digs+digc, b)-digs;
           if(mas[a]==b) continue;
           rp[invrp[a]]=rp[a];
           invrp[rp[a]]=invrp[a];
           rp[a]=n;
            int need=0;
           for(int j=a/sq;j>=0;--j){
               if(binary_search(gr[j].begin(), gr[j].end(), b)){
                   for(int k=min(a, (j+1)*sq-1);k>=sq*j;--k){
                       if(mas[k]==b){
                            need=j;                       
                            rp[k]=a;
                           invrp[a]=k;
                           break;
                       }
                   }
                   break;
               }
           }
           for(int j=a/sq;j<sq;++j){
               if(binary_search(gr[j].begin(), gr[j].end(), b)){
                   for(int k=max(j*sq,a);k<sq*(j+1) && k<n;++k){
                       if(mas[k]==b){
                           rp[a]=k;
                           invrp[k]=a;
                           break;
                       }
                   }
                   break;
               }
           }
           g[a/sq].clear();
           gr[a/sq].clear();
           int t=a/sq;
           mas[a]=b;
g[need].clear();
           gr[need].clear();
           for(int k=t*sq;k<(t+1)*sq && k<n;++k){
               g[t].pb(rp[k]);
               gr[t].pb(mas[k]);
           }
           sort(g[t].begin(), g[t].end());
           sort(gr[t].begin(), gr[t].end());
t=need;
   for(int k=t*sq;k<(t+1)*sq && k<n;++k){
               g[t].pb(rp[k]);
               gr[t].pb(mas[k]);
           }
           sort(g[t].begin(), g[t].end());
           sort(gr[t].begin(), gr[t].end());

       }else{

           int res=0;
           for(int j=a;j<=b;++j){
               if(j%sq==0 && j+sq<b){
                   res+=upper_bound(g[j/sq].begin(), g[j/sq].end(), b)-g[j/sq].begin();
                   j+=(sq-1);
               }else{
                   if(rp[j]>b) ++res;
               }
           }
           printf("%d\n", res);
       }
   }
return 0;
}
