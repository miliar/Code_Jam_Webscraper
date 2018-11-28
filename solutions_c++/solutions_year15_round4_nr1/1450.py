#include<bits/stdc++.h>

#define s(a) scanf("%d",&a)
#define ss(a) scanf("%s",a)

#define MP           make_pair
#define PB           push_back
#define REP(i, n)    for(int i = 0; i < n; i++)
#define INC(i, a, b) for(int i = a; i <= b; i++)
#define DEC(i, a, b) for(int i = a; i >= b; i--)
#define CLEAR(a)     memset(a, 0, sizeof a)

using namespace std;

typedef long long          LL;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int, int>     II;
typedef vector<II>         VII;

char inp[105][105];
int dp[105][105][4];
int main()
{
      int t;
      s(t);
      REP(tt,t)
      {
            int r,c;
            s(r);s(c);
            REP(i,r)
                  ss(inp[i]);
            bool ff = true;
            REP(i,r)
            REP(j,c)
            {
                  int rcnt = 0, ccnt = 0;
                  if(inp[i][j]=='.')continue;
                  REP(rr,r) if(inp[rr][j]!='.')rcnt++;
                  REP(cc,c) if(inp[i][cc]!='.')ccnt++;
                  if(rcnt<=1 && ccnt<=1) ff = false;
                  //printf("at r = %d, c = %d, rcnt = %d, ccnt = %d\n",i,j,rcnt,ccnt);
            }
            printf("Case #%d: ",tt+1);
            if(!ff)
            {
                  printf("IMPOSSIBLE\n");
                  continue;
            }
            int ans = 0;
            // top down
            REP(i,r)
            REP(j,c)
            {
                  dp[i][j][0] =dp[i][j][1] =  -1;
                  if(i>0)
                        dp[i][j][0] = dp[i-1][j][0];
                  if(j>0)
                        dp[i][j][1] = dp[i][j-1][1];
                  if(inp[i][j]!='.') {
                        if(inp[i][j]=='^' && dp[i][j][0]==-1) ans++;
                        if(inp[i][j]=='<' && dp[i][j][1]==-1) ans++;
                        dp[i][j][0] = 1;  dp[i][j][1] = 1;
                  }
            }
            // bottom up
            DEC(i,r-1,0)
            DEC(j,c-1,0)
            {
                  dp[i][j][2] =dp[i][j][3] =  -1;
                  if(i<r-1)
                        dp[i][j][2] = dp[i+1][j][2];
                  if(j<c-1)
                        dp[i][j][3] = dp[i][j+1][3];
                  if(inp[i][j]!='.') {
                        if(inp[i][j]=='v' && dp[i][j][2]==-1) ans++;
                        if(inp[i][j]=='>' && dp[i][j][3]==-1) ans++;
                        dp[i][j][2] = 1;  dp[i][j][3] = 1;
                  }
            }
            /*REP(i,r)
            {
                  REP(j,c)
                        printf("%d ",dp[i][j][0]);
                  printf("\n");
            }
            bool f1 = false;
            REP(i,r)
            REP(j,c)
            {
                  if(inp[i][j]!='.')
                  {
                        bool f = false;
                        REP(k,4) if(dp[i][j][k]!=-1)f = true;
                        if(!f) {
                              f1 = true;
                              printf("IMPOSSIBLE\n");
                              i=r;
                              break;
                        }
                  }
            }*/
            cout<<ans<<endl;
      }
      return 0;
}
