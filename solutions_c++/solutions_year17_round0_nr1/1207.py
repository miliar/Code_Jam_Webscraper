#include<bits/stdc++.h>
#define pb push_back
#define ll long long int
#define inf 1450000090
#define fastio ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define sd(x) scanf("%d",&x)
#define sd2(x,y) scanf("%d%d",&x,&y)
#define sdl(x) scanf("%lld",&x)
#define nax 100010
#define mp make_pair
#define sz(x) (int)(x.size())
#define pi pair <int ,int >
#define pii pair < int , pair <int ,int > >
#define MOD 1000000007
using namespace std;
char str[1010];
int main(int argc, char const *argv[])
{
  freopen("input.txt","read",stdin);
  freopen("output.txt","write",stdout);
  int t,k;
  sd(t);
  for(int tt=1;tt<=t;tt++)
  {
  	 printf("Case #%d: ",tt);
  	 scanf("%s",str);
     sd(k);
     int l = strlen(str);
     int ctr = 0;
     for (int i = 0; i <= l-k ; ++i)
     {
        if(str[i] == '-')
        {
          ctr++;
          for (int j = i; j < i+k; ++j)
          {
             if(str[j] == '-')
              str[j] = '+';
            else
              str[j] = '-';
          }
        }
     }
     bool ok = true;
     for (int i = 0; i < l; ++i)
     {
       if(str[i] == '-')
       {
          ok = false;
          break;
       }
     }
     if(ok)
     {
        printf("%d\n",ctr);
     }
     else
     {
        printf("IMPOSSIBLE\n");
     }
  }
  return 0;
}