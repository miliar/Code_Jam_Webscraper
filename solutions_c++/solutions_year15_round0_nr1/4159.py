#include<iostream>
#include<cstdio>
#include<cstring>
#include<climits>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<queue>
#include<string>
#include<map>
#include<set>
#include<bitset>
#include<stack>
#include<algorithm>
#include<typeinfo>

#define mp make_pair
#define pb push_back
#define fi first
#define se second

#define setBit(n,i) (n|=(1<<i))
#define clearBit(n,i) (n&=(~(1<<i)))
#define checkBit(n,i) (n&(1<<i))
#define lsBit(n) ((n)&(-n))

#define s(n) scanf("%d",&n)
#define fora(i,a,b) for(int i=a;i<b;i++)
#define fore(i,a) for(__typeof((a).begin())i=(a).begin();i!=(a).end();i++)
#define ms(a,b) memset(a,b,sizeof(a))
#define all(a) (a).begin(),(a).end()

#define INF 1e9

using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef long long int ll;

int main()
{
   freopen("temp.txt","r",stdin);
   freopen("outA.txt","w",stdout);
   int t,n;
   string str;
   cin>>t;
   fora(j,0,t)
   {
      cin>>n;
      cin>>str;
      int prev=str[0]-'0';
      int ans=0;
      fora(i,1,n+1)
      {
         if(i>prev)
         {
            int temp=i-prev;
            prev+=str[i]-'0'+temp;
            ans+=temp;
         }
         else
            prev+=str[i]-'0';
      }
      cout<<"Case #"<<j+1<<": "<<ans<<"\n";
   }
   return 0;
}
