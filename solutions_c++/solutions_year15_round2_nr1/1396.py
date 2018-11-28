#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define SZ(a) (int)a.size()
#define dd double
#define maxx 1001000

int dp[maxx];

int rev(int now)
{
    int ret = 0;
    int cur = now;
    while(cur)
    {
        ret = ret*10;
        ret += cur%10;
        cur /= 10;
    }

    return ret;
}

int rec(int now)
{
    if(now==1)
    {
        return 1;
    }

    int &ret = dp[now];
    if(ret!=-1) return ret;

    ret = (1<<30);

    ret = rec(now-1)+1;

    int val = rev(now);
    int val3 = rev(val);

    if(val3==now && val<now)
    {
        ret = min(ret , rec(val)+1);
    }
    return ret;
}


int main()
{
    freopen("A-small-attempt0.in" , "r" , stdin);
    freopen("A-small-attempt0.out" , "w+" , stdout);

    int tcase,cas=1;

    cin>>tcase;
    memset(dp , -1, sizeof dp);

    for(int i = 1 ; i<=1000000 ; i++)
        rec(i);

//    for(int i = 1 ; i<=100 ; i+=10)
//    {
//        cout<<i<<" - "<<rec(i)<<endl;
//    }
//
//    for(int i = 101 ; i<=1000 ; i+=100)
//    {
//        cout<<i<<" - "<<rec(i)<<endl;
//    }
//
//    for(int i = 1001 ; i<=10000 ; i+=1000)
//    {
//        cout<<i<<" - "<<rec(i)<<endl;
//    }

    while(tcase--)
    {
        int n;

        cin>>n;
//        cout<<n<<endl;

        cout<<"Case #"<<cas++<<": "<<rec(n)<<endl;
    }
    return 0;
}

