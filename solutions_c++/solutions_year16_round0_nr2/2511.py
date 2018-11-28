#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define maxn 100100
#define s second
#define ll long long int
#define inf 1000000014
#define infl (ll)(1e18+1)
#define mod 1000000007
#define sz(x) (int) x.size()
#define trace1(x)  cerr << #x << ": " << x << endl;
#define trace2(x, y)  cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
using namespace  std;
char str[105];
int main(int argc, char const *argv[])
{
  int t;
  cin>>t;
  for(int test=1;test<=t;test++)
  {
      scanf("%s",str);
      int l = strlen(str);
      int done=0;
      int cnt=0;
      while(!done)
     {
      char ff = str[0];
      int pos = 1;
      while(pos<l && str[pos]==ff)
        pos++;
      if(pos==l)
      {
        done = 1;
      }
      else
      {  cnt++;
         for(int i=0;i<=pos;i++)
          str[i] = str[pos];
      }
     }
     if(str[0]=='-')
      cnt++;
    printf("Case #%d: %d\n",test,cnt);
  }
  return 0;
}