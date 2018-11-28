/*
   Mayank Pratap Singh
   MNNIT, 2nd year IT

   AC ho.
*/
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define vi vector<ll>
#define pp pair<ll,ll>
#define mp make_pair
#define pb push_back
#define s1(x) scanf("%lld",&x)
#define s2(x,y) scanf("%lld",&x,&y)
#define s3(x,y,z) scanf("%lld",&x,&y,&z)
#define pf(x) printf("%lld\n",x)
#define FOR(x,y) for(x=0;x<y;x++)
#define M 1000000007
#define MAX 100000
vector<pair<ll,ll> > tree(4*MAX+6);
bool compare (int a , int b)
{

}
int main()
{
  long long t,i,j,k,n;
  int a[2000+4];

  scanf("%lld",&t);

  for(k=0;k<t;k++)
  {
    scanf("%lld",&n);
    int s=0;
     for(i=1;i<=n;i++)
     {
       scanf("%d",&a[i]);
      s+=a[i];
     }

    int maxx = -1;
    int index;
    int total=0;
    printf("Case #%lld: ",k+1);
     while(1)
     {
       for(j=1;j<=n;j++)
       {
         if(a[j])
          total++;
         if(a[j]>maxx && a[j])
         {
           maxx=max(maxx,a[j]);
           index=j;
         }

       }
       if(total<=2 || maxx==-1)
       {

         break;
       }
       a[index]-=1;
       printf("%c ",64+index);
       maxx=-1;
       total=0;
     }
      int flag=1;
    while(flag)
    {

     flag=0;
     for(i=1;i<=n;i++)
     {
        if(a[i])
        {
          flag=1;
          a[i]-=1;
          printf("%c",64+i);
          i++;
          break;
        }
     }
     for(;i<=n;i++)
     {
        if(a[i])
        {
          printf("%c ",64+i);
          a[i]-=1;
        }
     }
   }

  printf("\n");

  }
  return 0;
}
