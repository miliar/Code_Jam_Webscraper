#include<bits/stdc++.h>
using namespace std;
long int a[100000];
int main()
{
    freopen("kk.in","r",stdin);
    freopen("kk.out","w",stdout);

long int t,p=0;
cin>>t;
while(t--)
{
    long int i,j,k,n,ans1=0,ans2=0,mx=-99999;
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>a[i];
        if(i>0)
        {
            if(a[i-1]-a[i]>0)
                ans1+=(a[i-1]-a[i]);




        }
    }
    for(i=0;i<n-1;i++)
    {
        if(mx<a[i]-a[i+1])
            mx=a[i]-a[i+1];
    }
    //Case #1: 15 25
    mx=fabs(mx);
  //  cout<<mx<<endl;
    for(i=0;i<n-1;i++)
    {
       // if(a[i]<=mx)
            ans2+=min(mx,a[i]);

    }
    printf("Case #%d: ",++p);
    cout<<ans1;
    cout<<" ";
    cout<<ans2<<endl;
}
return 0;
}
