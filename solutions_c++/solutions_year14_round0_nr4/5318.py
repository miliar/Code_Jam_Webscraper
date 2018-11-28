#include <iostream>
using namespace std;
//double a[2000],b[2000]
int main()
{
    freopen("D-small-attempt.in","r",stdin);
    freopen("D-small-attempt.out","w",stdout);
    double a[2000],b[2000],ss;
    int t,l,i,j,k,n,m,ans;
    cin>>t;
    for(l=0;l<t;l++)
    {
       cin>>n;
       for(i=0;i<n;i++)
       {
              cin>>a[i];    
       }      
       for (i=0;i<n;i++)
       {
              cin>>b[i];    
       }
       for (i=0;i<n;i++)
       {
              for(j=i+1;j<n;j++)
                if (a[i]>a[j])
                {
                    ss=a[i];
                    a[i]=a[j];
                    a[j]=ss;    
                }    
       }
       for (i=0;i<n;i++)
       {
              for(j=i+1;j<n;j++)
                if (b[i]>b[j])
                {
                    ss=b[i];
                    b[i]=b[j];
                    b[j]=ss;    
                }    
       }
       ans=0;j=0;
       for(i=0;i<n;i++)
       {
       if (a[i]>b[j])
       {
           //cout<<endl<<a[i]<<' '<<b[j]<<endl;
              ans++;
              j++;    
       }
       }
       cout<<"Case #"<<l+1<<": ";
       cout<<ans<<' ';
       ans=0;j=0;
       for(i=0;i<n;i++)
       {
           if (b[i]>a[j])
           {
               ans++;
               j++;    
           }    
       }
       cout<<n-ans<<endl;
    }    
}
