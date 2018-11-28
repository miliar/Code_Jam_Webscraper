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
int main(int argc, char const *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
   int test;
   cin>>test;
   string x;
   int arr[27];
   int s[27];
   for (int i = 1;i<=test; ++i)
   {
       for (int j = 0; j < 27; ++j)
      {
       arr[j]=0;
       s[j]=0;
      }
      cin>>x;
      int l = x.length();
      for (int j = 0; j < l; ++j)
      {
         s[x[j]-'A']++;
      }
      arr[0] = s[25];
      arr[2] = s[22];
      arr[6] = s[23];
      arr[8] = s[6];
      arr[4] = s[20];
      s[4]-=arr[0]+arr[8];
      s[5]-=arr[4];
      arr[5] = s[5];
      s[17]-=arr[4]+arr[0];
      arr[3] = s[17];
      s[8]-=arr[5]+arr[6]+arr[8];
      arr[9] = s[8];
      s[18]-=arr[6];
      arr[7] = s[18];
      arr[1] = s[14]-arr[2]-arr[4]-arr[0];
      string ans="";
      printf("Case #%d: ",i);
      for(int j=0;j<=9;j++)
      {
        for(int k=0;k<arr[j];k++)
          cout<<j;
      }
      cout<<"\n";

   }
   return 0;
}
