#include<bits/stdc++.h>

using namespace std;

#define ll long long int

ll arr[2501]={0};



int main()
{
    ll t,n,i,val;
    cin>>t;
    ll count=0;
    while(t--)
    {
        count++;
        cin>>n;
        for(i=0;i<2*n-1;i++)
        {
            for(int j=0;j<n;j++)
            {
                cin>>val;
                arr[val]++;
            }
        }
        cout<<"Case #"<<count<<": ";
        for(i=1;i<=2500;i++)
        {
            if(arr[i]%2==1)
                cout<<i<<" ";
        }
        for(i=1;i<=2500;i++)
            arr[i]=0;
        cout<<"\n";
    }
    return 0;
}
