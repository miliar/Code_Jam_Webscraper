#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define int64 unsigned long long
#define INF numeric_limits<int64>::max()
#define lsb(x) (-x)&x
using namespace std;
int64 solve(int x)
{
    bool digits[10];
    for(int i=0;i<=9;i++)
        digits[i]=false;
    if(x==0)
        return -1;
    for(int i=1;;i++)
    {
        int64 y=x*1LL*i;
        while(y!=0)
        {
            digits[y%10]=true;
            y/=10;
        }
        bool isFine=true;
        for(int i=0;i<=9;i++)
        if(digits[i]==false)
        {
            isFine=false;
            break;
        }
        if(isFine==true)
            return x*1LL*i;
    }

}
int main()
{
    int Tests;
    cin>>Tests;
    for(int t=1;t<=Tests;t++)
    {
        int x;
        cin>>x;
        x=solve(x);
        if(x==-1)
            cout<<"Case #"<<t<<": INSOMNIA\n";
        else
            cout<<"Case #"<<t<<": "<<x<<'\n';
    }
    return 0;
}
