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

int main()
{
      int t;
      s(t);
      REP(tt,t)
      {
            int ans = 0,prev;
            int n;
            char inp[1005];
            s(n);
            ss(inp);
            prev = inp[0]-'0';
            INC(i,1,n)
            {
                  if(prev < i && inp[i]>'0')
                  {
                        ans += i-prev;
                        prev += i-prev;
                  }
                  prev = prev + (inp[i]-'0');
            }
            printf("Case #%d: %d\n",tt+1,ans);
      }
      return 0;
}
