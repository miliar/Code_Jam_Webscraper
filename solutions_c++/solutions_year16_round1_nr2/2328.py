#include<iostream>
#include<algorithm>
using namespace std;
main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int height[5000]={0};
        int n;
        cin>>n;
        for(int j=0;j<2*n-1;j++)
        {
            for(int k=0;k<n;k++)
            {
                int x;
                cin>>x;
                height[x]++;
            }
        }
    int arr[100]={0},l=0;
    for(int u=1;u<=3000;u++)
    {
        if(height[u]%2==0) continue;
        arr[l++]=u;
    }
    sort(arr,arr+l);
    cout<<"Case #"<<i<<": ";
    for(int u=0;u<l;u++) cout<<arr[u]<<" ";
    cout<<"\n";
    }
    return 0;
}
