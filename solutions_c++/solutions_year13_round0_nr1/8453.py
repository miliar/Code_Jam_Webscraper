#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<cmath>
#include<cctype>
#include<cstring>
#include<string>
#include<ctime>
#include<cassert>
using namespace std;

#define TRACE(x) cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x) cerr << #x << " = " << x << endl;
#define FOR(i,a,b) for(i=(a);i< (b);i++)
char dp[4][4];
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.in","w",stdout);
    char ch;
    int tc,test_c;
    cin>>tc;
    int k;
    FOR(k,1,tc+1)
    {
       int count=0;
       int i,j;
       FOR(i,0,4)
       {
          FOR(j,0,4)
          {
             cin>>dp[i][j];
             if(dp[i][j]=='.')
               count++;
          }
       }
       FOR(i,0,4)
       {
          if(dp[i][0]=='.')
          continue;
          ch=dp[i][0];
          FOR(j,0,4)
          {
              if(dp[i][j]!=ch && dp[i][j]!='T')
              break;
          }
          if(j==4)
          break;
       }
       if(i!=4)
       {
          printf("Case #%d: %c won\n",k,ch);
            continue;
       }
       FOR(j,0,4)
       {
          if(dp[0][j]=='.')
            continue;
          ch=dp[0][j];
          FOR(i,0,4)
          {
              if(dp[i][j]!=ch && dp[i][j]!='T')
              break;
          }
          if(i==4)
            break;
       }
       if(j!=4)
       {
          printf("Case #%d: %c won\n",k,ch);
          continue;
       }
       ch=dp[0][0];
       if(ch!='.')
       {
       for(i=1,j=1;i<4;i++,j++)
       if(dp[i][j]!=ch && dp[i][j]!='T')
           break;
       if(i==4)
       {
          printf("Case #%d: %c won\n",k,ch);
          continue;
       }
       }
       ch=dp[0][3];
       if(ch!='.')
       {
       for(i=1,j=2;i<4;i++,j--) 
       if(dp[i][j]!=ch && dp[i][j]!='T')
            break;   
       if(i==4)
       {
          printf("Case #%d: %c won\n",k,ch);
          continue;
       }
       }
       if(count)
         printf("Case #%d: Game has not completed\n",k);
       else
         printf("Case #%d: Draw\n",k);
    }

    return 0;
}    
