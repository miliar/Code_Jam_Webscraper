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
   #ifndef ONLINE_JUDGE
   freopen("D-small-attempt2.in","r",stdin);
   freopen("outDs.txt","w",stdout);
   #endif
   int t,x,r,c;
   cin>>t;
   fora(i,0,t)
   {
      cin>>x>>r>>c;
      cout<<"Case #"<<i+1<<": ";
      if(x>=7)
      {
         puts("RICHARD");
         continue;
      }
      if((r*c)%x!=0)
      {
         puts("RICHARD");
         continue;
      }
      if(x>max(r,c))
      {
         puts("RICHARD");
         continue;
      }
      if((x/2)>min(r,c))
      {
         puts("RICHARD");
         continue;
      }
      if(x==1)
      {
         puts("GABRIEL");
         continue;
      }
      if(x==2)
      {
         if(r%2==1&&c%2==1)
            puts("RICHARD");
         else
            puts("GABRIEL");
         continue;
      }
      if(x==3)
      {
         if((r%3==0&&c%2==0)||((r%2==0&&c%3==0))||(r==3&&c==3))
            puts("GABRIEL");
         else
            puts("RICHARD");
         continue;
      }
      if(x==4) //only for small
      {
         if((max(r,c)==4&&min(r,c)==3)||(r==4&&c==4))
            puts("GABRIEL");
         else
            puts("RICHARD");
         continue;
      }

   }
   return 0;
}
