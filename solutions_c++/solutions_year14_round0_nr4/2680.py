#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    freopen("D1.in","r",stdin);
    freopen("D1.out","w",stdout);
    int t,i,j,ii,n,res1,res2;
    double fir[1005],sec[1005];
    cin>>t;
    for(ii=1;ii<=t;ii++)
    {
          res1=0;
          res2=0;
          cin>>n;
          for(i=0;i<n;i++)
              cin>>fir[i];
          for(i=0;i<n;i++)
              cin>>sec[i];
          sort(fir,fir+n);
          sort(sec,sec+n);
          for(i=0,j=0;i<n;i++)
          {
               if(fir[i]>sec[j])
               {
                    res1++;
                    j++;
               }
          }
          for(i=n-1,j=n-1;i>=0;i--)
          {
                if(fir[i]>sec[j])
                {
                     res2++;
                }
                else
                   j--;
          }
          cout<<"Case #"<<ii<<": "<<res1<<" "<<res2<<"\n";
    }
}
