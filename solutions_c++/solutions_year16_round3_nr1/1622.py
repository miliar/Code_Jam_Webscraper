#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

//By:-mansigupta

#define pb(x) push_back(x)

#define ll long long int

#define mp(x,y) make_pair(x,y)

#define FOR(x,y) for(x=0;x<y;x++)

#define For(x,y) for(x=1;x<=y;x++)

#define mod 1000000007

#define f first

#define s second

#define pii pair<int,int>

typedef vector <int> vi;

#define SET(x,y) memset(x,y,sizeof(x)

#define FORI(x,l,u) for(x=l;x<=u;x++)

#define PI 3.141592653589793238462643

typedef set <int> si;

typedef map <int,int> mii;

#define IT iterator

/*bool visit[];

void dfs(int u)

{

  visit[u]=1;



  int k;

  FOR(k,gr[u].size())

  {if(!visit[gr[u][k]])

  dfs(gr[u][k]);}

}*/

/*ll power(ll base, ll p)

{

    if(p==0)

    return 1;

    if(p==1)

    return (base%mod);

    base=base%mod;

    if(p%2!=0)

    {



        return((base%mod*((power((base*base)%mod,p/2)%mod)))%mod);

    }

    else

    return((power(((base%mod)*(base%mod))%mod,p/2))%mod);

}

int gc(int a,int b)

{

    if(a==0)return b;

    return gc(b%a,a);

}

*/

/*void f()

{

    priority_queue<pii,vector<pii>,greater<pii>> Q;

    Q.push({0,s});

    while(!Q.empty())

    {

        int u=Q.top().s;

        int c=Q.top().f;

        Q.pop();

        int i;

        FOR(i,g[u].size())

        {

            pii p=g[u][i];

            int v=p.s;

            int w=p.f;

            if(dist[v]>dist[u]+w){

                dist[v]=dist[u]+w;

                Q.push({dist[v],v});

            }

        }

    }

}*/



int main()

{

  //Beauty is in relaxed hard work.

  //SSGCA :)

  //Keep doing your thing, complexity would turn into simplicity! :)
  freopen("acb.txt","w",stdout);
freopen("A-large.in.txt","r",stdin);
//cout<<"loop";
    int r=1;

    int t;

    cin>>t;

    while(t--){

        int n;
        cin>>n;
        int a[27],i,j;
        FOR(i,n)cin>>a[i];
        int curr=0;
        FOR(i,n)curr+=a[i];
        int sum=curr;
        sum-=2;
        int mx=sum/2+1;
        cout<<"Case #"<<r++<<": ";
        int y=5;
        while(curr)
        {
          if(curr==3){
            FOR(i,n){
              if(a[i]){
                a[i]--;
                cout<<(char)('A'+i)<<" ";break;
              }
            }
            FOR(i,n){
              if(a[i]){
                a[i]--;
                cout<<(char)('A'+i);
              }
            }
            break;
          }
          if(curr==2){
              FOR(i,n){
              if(a[i]){
                a[i]--;
                cout<<(char)('A'+i);
              }
            }
            break;
          }
          int c=0;
          FOR(i,n){
              if(a[i]>=mx){
                a[i]--;cout<<(char)('A'+i);c++;break;
              }
          }
          FOR(i,n){
              if(a[i]>=mx){
                a[i]--;cout<<(char)('A'+i);c++;break;
              }
          }
          while(c!=2){
              FOR(i,n){
              if(a[i]){
                a[i]--;cout<<(char)('A'+i);c++;break;
              }
          }
          }
          cout<<" ";
          curr=0;
          FOR(i,n){
            curr+=a[i];
          }
          mx=(curr-2)/2+1;

        }
        

       
        cout<<endl;

    }

  return 0;

}
