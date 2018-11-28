#include <iostream>
#include <stdio.h>
#include <vector>
#include <string.h>
using namespace std;
int n,k;
const int N = 210;
double arr[210];

vector<int> vk;
vector<int> v2;
vector<double> vf;
vector<double> vf2;
double dp[100000];
int getdigit(int i)
{
    int ret=0;
    while(i)
    {
        ret+=i%2;
        i/=2;
    }
    return ret;
}
double cal1(int state)
{
    double ret = 1;

    for(int i=0;i<n;i++)
    {
        if((state&(1<<i))!=0)
        {
            ret *= arr[i];
        }
    }
    return ret;
}
double cal2(int state)
{
    double ret = 1;

    for(int i=0;i<n;i++)
    {
        if((state&(1<<i))!=0)
        {
            ret *= (1.0-arr[i]);
        }
    }
    return ret;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;
    for(int ti=1;ti<=t;ti++)
    {
        cout<<"Case #"<<ti<<": ";

        cin>>n>>k;

        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }

        v2.clear();
        vf.clear();
        vf2.clear();
        for(int i=0;i<(1<<n);i++)
        {
            dp[i]=0;
            if(getdigit(i)==k/2)
            {
                v2.push_back(i);
                vf.push_back(cal1(i));
                vf2.push_back(cal2(i));
            }
        }

        for(int i=0;i<v2.size();i++)
        {
            for(int j=i+1;j<v2.size();j++)
            {
                if(i!=j)
                {
                    int a=v2[i];
                    int b=v2[j];
                    if((a&b)==0)
                    {
                        dp[a|b]+=vf[i]*vf2[j]+vf2[i]*vf[j];
                    }
                }
            }
        }
        double ans = 0;
        for(int i=0;i<(1<<n);i++)
        {
            ans = max(ans,dp[i]);
        }
        cout<<ans<<endl;
    }
    return 0;
}
