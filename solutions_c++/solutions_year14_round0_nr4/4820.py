#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
struct node
{
     double val;
};
bool compasc(node a ,node b)
{
     if(a.val<=b.val)
     return true;
     else
     return false;
}
bool compdesc(node a ,node b)
{
     if(a.val>=b.val)
     return true;
     else
     return false;
}
double cr[2005];
double dr[2005];
int main()
{
     ll t,n,c=0,i,c1=0,j,k=1;
     scanf("%lld",&t);
     while(t--)
     {
          c=0;
          scanf("%lld",&n);
           node ar[n];
           node br[n];
          for(i=0;i<n;i++)
          {
                scanf("%lf",&ar[i].val);
                cr[i]=ar[i].val;
          }
          for(i=0;i<n;i++)
          {
                scanf("%lf",&br[i].val);
                dr[i]=br[i].val;
          }
          sort(ar,ar+n,compasc);
          sort(br,br+n,compasc);
          sort(cr,cr+n);
          sort(dr,dr+n);
         //for(i=0;i<n;i++)
         //cout<<cr[i]<<" "<<dr[i]<<endl;
         for(i=0;i<n;i++)
         {
              for(j=0;j<n;j++)
              {
                   if(br[j].val!=0&&br[j].val>ar[i].val)
                   {
                        br[j].val=0;
                        ar[i].val=0;
                        break;
                   }
              }
         }
         for(i=0;i<n;i++)
         {
              for(j=0;j<n;j++)
              {
                   if(dr[j]!=0&&cr[i]>dr[j])
                   {
                        cr[i]=0;
                        dr[j]=0;
                        //c1++;
                        break;
                   }
              }
         }
         for(i=0;i<n;i++)
         {

              if(ar[i].val!=0)
              c++;
              if(dr[i]==0)
              c1++;
              //if(ar[i].val!=0)
              //c1++;
         }
          printf("%lld %lld\n",c1,c);
          c=0;c1=0;
     }
     return 0;
}
