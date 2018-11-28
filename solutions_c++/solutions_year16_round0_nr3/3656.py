#include <bits/stdc++.h>
using namespace std;

bool isPrime(long long n)
{
    for (long long i=2;i*i<=n;i++)
    {
        if (n%i) continue;
        return false;
    }
    return true;
}

long long getDivisor(long long n)
{
    for (long long i=2;i*i<=n;i++)
    {
        if (n%i) continue;
        return i;
    }
}

long long f(long long n,long long newBase)
{
    long long ans,cur;
    cur = 1;
    ans = 0;
    while (n>0)
    {
        ans+=(n%10)*cur;
        n/=10;
        cur*=newBase;
    }
    return ans;
}

long long from10to2(long long n)
{
    long long ans,cur;
    ans = 0;
    cur = 1;
    while (n>0)
    {
        ans = ans+(n%2)*cur;
        n/=2;
        cur*=10;
    }
    return ans;
}

int main()
{

    long long ans[57][11],cnt;
    cnt = 0;
    for (int i=32769;i<=65535;i+=2)
    {
        bool flag = false;
        for (int j=2;j<=10;j++)
        {
            if (isPrime(f(from10to2(i),j))) flag = true;

        }
        if (!flag)
        {
            cnt++;
            ans[cnt][0] = from10to2(i);
            for (int j=2;j<=10;j++) ans[cnt][j] = getDivisor(f(from10to2(i),j));
        }

        if (cnt>=50) break;
    }
    freopen("output.out","w",stdout);
    cout<<"Case #1:"<<endl;
    for (int i=1;i<=50;i++)
    {
        cout<<ans[i][0];
        for (int j=2;j<=10;j++) cout<<" "<<ans[i][j];
        cout<<endl;
    }

    return 0;
}
