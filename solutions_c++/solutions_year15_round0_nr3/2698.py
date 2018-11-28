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
int mat[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int main()
{
   #ifndef ONLINE_JUDGE
   freopen("C-small-attempt1.in","r",stdin);
   freopen("outCss.txt","w",stdout);
   #endif
   int t,l,x;
   string str;
   int arr[10010];
   int DP[10010];
   int rDP[10010];
   cin>>t;
   fora(k,0,t)
   {
      cin>>l>>x;
      cin>>str;
      int u=0;
      fora(j,0,x)
         fora(i,0,l)
            switch(str[i])
            {
               case '1':arr[u++]=1;
                     break;

               case 'i':arr[u++]=2;
                     break;


               case 'j':arr[u++]=3;
                     break;


               case 'k':arr[u++]=4;
                     break;
            }
      DP[0]=arr[0];
      fora(i,1,u)
      {
         if(DP[i-1]<0)
            DP[i]=-1*mat[-1*DP[i-1]][arr[i]];
         else
            DP[i]=mat[DP[i-1]][arr[i]];
      }
      rDP[u-1]=arr[u-1];
      for(int i=u-2;i>=0;i--)
      {
          if(rDP[i+1]<0)
            rDP[i]=-1*mat[arr[i]][-1*rDP[i+1]];
         else
            rDP[i]=mat[arr[i]][rDP[i+1]];
      }
      bool flag=false;
      fora(i,0,u-1)
      {
         if(flag) break;
         if(DP[i]!=2)   continue;
         int b=1;
         fora(j,i+1,u)
         {
            if(b<0)
               b=-1*mat[-1*b][arr[j]];
            else
               b=mat[b][arr[j]];
            if(b==3&&rDP[j+1]==4)
               flag=true;
         }
      }
      if(flag)
         cout<<"Case #"<<k+1<<": YES\n";
      else
         cout<<"Case #"<<k+1<<": NO\n";
   }
   return 0;
}
