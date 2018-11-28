#include<iostream>
using namespace std;
int main()
{
    long t;
    cin>>t;
    for(long i=1;i<=t;i++)
    {
        long long a,b,c;
        cin>>a>>b>>c;
        cout<<"Case #"<<i<<": ";
        for(long long j=1;j<=c;j++)
        cout<<j<<" ";
        cout<<endl;
    }
    return 0;
}