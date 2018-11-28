#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    int t;
    int n;
    int a[2000];
    cin>>t;
    for (int tt=0;tt<t;tt++)
    {
        cout<<"Case #"<<tt+1<<": ";
        cin>>n;
        for (int i=0;i<n;i++)
            cin>>a[i];
        int ans=3000;
        for (int i=1;i<=1000;i++)
        {
            int an=0;
            for (int j=0;j<n;j++)
                if (a[j]>i)
                    an+=(a[j]-1)/i;
            ans=min(ans,an+i);
        }
        cout<<ans<<endl;
    }
}
