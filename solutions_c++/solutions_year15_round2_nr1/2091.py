#include<bits/stdc++.h>
using namespace std;
typedef long long unsigned llu;

//static llu a[]={20,110,1010,10010,100010,1000010,10000010,100000010,1000000010,10000000010,100000000010,1000000000010,10000000000010,100000000000010,1000000000000010,10000000000000010,100000000000000010};
llu dp[100000000]={0};
llu MAX=10000000;

llu rev(llu num)
{
    llu rev_num = 0;
    while(num > 0)
    {
        rev_num = rev_num*10 + num%10;
        num = num/10;
    }
    return rev_num;
}


int main()
{
    int t;
    cin >> t;
    memset(dp,INT_MAX,sizeof dp);
    for(llu i=0;i<MAX;i++)
        {
            dp[i+1]=min(dp[i+1],dp[i]+1);
            dp[rev(i)]=min(dp[rev(i)],dp[i]+1);

        }
    for(int tt=0;tt<t;tt++)
    {
        cout << "Case #" << (tt+1) << ": ";
        llu n;
        cin>>n;


        cout<<dp[n]+1<<endl;
    }
    return 0;
}
