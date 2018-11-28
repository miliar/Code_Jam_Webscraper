#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int t,hh=0;
    cin>>t;
    double arr[1111],brr[1111];
    while(t--)
    {
        hh++;
        printf("Case #%d: ",hh);
        
        int n;cin>>n;
        for(int i=0;i<n;i++)cin>>arr[i];
        for(int i=0;i<n;i++)cin>>brr[i];
        sort(arr,arr+n);
        sort(brr,brr+n);
        int ans=0;
        int k=n-1;
        for(int i=n-1;i>=0;i--)
        {
            if(arr[i]>brr[k]){ans++;}
            else k--;
        }
        int ans2=0;
        int x=0,y=0;
        for(int i=0;i<n;i++)
        {
            if(arr[x]<brr[y])x++;
            else
            {
                x++;y++;ans2++;
            }
        }
        cout<<ans2<<" "<<ans<<endl;

        
        
    }
    
}


