#include<bits/stdc++.h>
using namespace std;
int a[1001];
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        int y=0;
        for(int i=0;i<(n-1);i++)
        {
            if(a[i+1]<a[i])
                y+=a[i]-a[i+1];
        }
        int z=0;
        int r=0;
        for(int i=0;i<(n-1);i++)
        {
            if(a[i+1]<a[i])
            {
                if((a[i]-a[i+1])>r)
                {
                    r=(a[i]-a[i+1]);
                }
            }
        }
        //cout<<r<<endl;
        for(int i=0;i<(n-1);i++)
        {
            if(a[i]>r)
                z+=r;
            else
                z+=a[i];
        }
        cout<<"Case #"<<i+1<<": "<<y<<" "<<z<<endl;
    }
    return 0;
}
