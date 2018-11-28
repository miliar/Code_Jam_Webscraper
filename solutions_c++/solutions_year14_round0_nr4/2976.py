#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
int main()
{

    int t,k,i,j;
    cin>>t;
    for(k=1;k<=t;k++)
    {
       int n;
       cin>>n;
       double a[n],b[n];
       int c[n];
       for(i=0;i<n;i++)
        cin>>a[i];
       for(i=0;i<n;i++)
        cin>>b[i];
       for(i=0;i<n;i++)
        c[i]=0;
       sort(a,a+n);
       sort(b,b+n);
       cout<<"Case #"<<k<<": ";
       int count=0,f=0;
        for(i=0;i<n;i++)
        {
            f=0;
            for(j=0;j<n;j++)
            {
                if(c[j]==0 && b[j]<a[i])
                {
                    f=1;
                    c[j]=1;
                    count++;
                    break;
                }
            }
            if(f==0)
            {
                for(j=n-1;j>=0;j--)
                    if(c[j]==0)
                {
                    c[j]=1;
                    break;
                }
            }
        }
      cout<<count<<" ";
       count=0;
       for(i=0;i<n;i++)
        c[i]=0;
       for(i=0;i<n;i++)
       {
           for(j=0;j<n;j++)
           {
               if(c[j]==0 && b[j]>a[i])
                {
                    c[j]=1;
                    count++;
                    break;
                }
           }
       }
cout<<n-count<<endl;
    }
   return 0;
}
