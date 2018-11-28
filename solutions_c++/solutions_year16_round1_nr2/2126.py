#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int n;
        int a[2600]={0};
        cin>>n;
        for(int j=1;j<=2*n-1;j++)
        {
            for(int k=1;k<=n;k++)
            {
                int x;
                cin>>x;
                a[x]++;
            }
        }
        cout<<"Case #"<<i<<": ";
        int c=0;
        for(int l=1;l<=2600;l++)
        {
            if(a[l]&1)
            {
                cout<<l;
                c++;
            }
            if(c!=n)
            {
                cout<<" ";
            }
        }
        cout<<endl;
    }
}
