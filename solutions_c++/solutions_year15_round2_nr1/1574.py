#include <bits/stdc++.h>
using namespace std;
#define ll  long long int
#define maxi    1111111

int dp[maxi]={0};


ll make_reverse(ll num)
{
    ll temp=0,st=0;
    while(num!=0)
    {
        temp=num%10;
        st=st*10+temp;
        num/=10;
    }
    return st;
}


void precompute()
{
    ll temp=0,temp_temp=0,copy_cat=0;
    dp[0]=1;
    dp[1]=1;
    queue<ll>   Q;
    Q.push(1);

    while(!Q.empty())
    {
        temp=Q.front();
        temp_temp=temp+1;
        Q.pop();

        if(temp<=maxi)
        {
            if(!dp[temp_temp])
            {
                dp[temp_temp]=dp[temp]+1;
                Q.push(temp_temp);
            }
            copy_cat=make_reverse(temp);
            if(copy_cat<maxi && !dp[copy_cat])
            {
                dp[copy_cat]=dp[temp]+1;
                Q.push(copy_cat);
            }
        }
    }
}


int main()
{
    int t,x=1;
    scanf("%d",&t);
    precompute();
    while(t--)
    {
        ll ans=0,n;
        cin>>n;
/*
        if(n<=20)
            ans=n;
        else if(n<=100)
        {
            t2=n;
            while(t2!=0)
            {
                temp=t2%10;
                temp_sum+=temp;
                t2/=10;
            }
            if(n%10!=0)
                ans=10+temp;
            else
            {
                temp=n/10;
                ans=temp+19;
            }
        }
        else if(n<=200)
        {
            t2=n;
            int r1=t2%10;
            int r2=t2%100;
            temp=r1+r2;
            ans=29+temp;
        }
        else if(n<=1000)
        {

        }
*/

        ans=dp[n];
        cout<<"Case #"<<x<<": "<<ans<<endl;
        x++;
    }

    return 0;
}
