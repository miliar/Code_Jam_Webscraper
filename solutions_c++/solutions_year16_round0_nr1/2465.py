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
int arr[10];
typedef pair< int,int > pp;
int main()
{
   int t;
   cin>>t;
   ll n;ll num,cpy;
   for(int test=1;test<=t;test++)
   {
       cin>>n;
       for(int i=0;i<=9;i++)
        arr[i]=0;int done=0;
       for(int i=1;i<=100;i++)
       {
           num = n*1ll*i;
           cpy = num;
           while(cpy!=0)
           {
               int d = cpy%10;
               cpy/=10;
               if(arr[d]==0)
               {
                   done++;
                   arr[d]=1;
               }
           }
           if(done==10)
            break;
       }
       int cnt=0;
       for(int i=0;i<=9;i++)
       {
           if(arr[i]==1)cnt++;
       }
       if(cnt==10)
        printf("Case #%d: %lld\n",test,num);
       else
        printf("Case #%d: INSOMNIA\n",test);
   }
}
