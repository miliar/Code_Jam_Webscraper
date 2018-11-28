#include<stdio.h>
#include<iostream>
#include<cstring>
#include<string>
#include<vector>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<map>
#include<sstream>
#include<set>
#include <queue>
#include<stack>
using namespace std;

#define pb push_back
#define ms(a,v) memset(a,v,sizeof a)
#define forstl(i,n) for(__typeof(n.begin())i = n.begin();i!=n.end();i++)

#define rep(i,n) for( __typeof(n)i = 0 ; i < n ; i++)
#define For(i,n) for( __typeof(n)i = 1 ; i <= n ; i++)
typedef long long ll;

string toString(ll number){ stringstream ss;ss << number; return ss.str(); }
vector<int>ways[25];
int n , k;
int cK[207];
int topen[25];
int keys[205];
int dp[1<<20 + 5 ];
stack<int >s;
int app(int opp){

    if(opp == (1<<n)-1 ) return 1;
    if(dp[opp]!=-1) return dp[opp];
    rep(i,n){
        if(opp&1<<i) continue;
        if(keys[ topen[i] ]){
            keys[ topen[i] ]--;
            rep(j,(int)ways[i].size())
                keys[ways[i][j]]++;

            if(app(opp|1<<i))
               {
                   s.push(i+1);
                   return 1;
               }

            keys[topen[i]]++;
            rep(j,(int)ways[i].size())
                keys[ways[i][j]]--;
        }
    }
    return dp[opp]=0;
}

int main()
{
  /* freopen("in.txt", "r", stdin);
   freopen("out.txt", "w", stdout);*/
    int test , cs = 1 ;
    cin>>test;

    while(test--)
    {
        ms(dp,-1);
            ms(keys,0);
            while(!s.empty()) s.pop();

            scanf("%d %d",&k,&n);
            rep(i,k){
                scanf("%d",cK+i);
                keys[cK[i]]++;
            }
            rep(i,n)
            {
                scanf("%d",topen+i);
                int x ,y;
                scanf("%d",&x);
                rep(z,x){
                    scanf("%d",&y);
                    ways[i].pb(y);
                }
            }
            printf("Case #%d:",cs++);
            if(app(0))
            {

                while(!s.empty()){
                      printf(" %d",s.top());
                      s.pop();

                }
                puts("");
            }
            else printf(" IMPOSSIBLE\n");
            rep(i,22)ways[i].clear();
    }
}
