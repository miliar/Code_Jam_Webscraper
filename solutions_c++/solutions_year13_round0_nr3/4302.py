#include<iostream>
using namespace std;
int main()
{
int dp[39]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};

int T;
cin>>T;

for(int t=1;t<=T;t++)
{
    long long int a,b;
    cin>>a>>b;
    int count=0;
    for(int i=0;i<39;i++)
    {
        long long int ans;
        ans=dp[i];
        ans=ans*ans;
        if(ans>=a&&ans<=b)
        count++;
    }
    cout<<"Case #"<<t<<": ";
    cout<<count<<endl;

}

return 0;
}
