#include<cstdio>
#include<vector>
using namespace std;

long long pow(long long a, long long b)
{
    int ret = 1;
    for(int i=0;i<b;i++)
        ret *= a;
    return ret;
}

long long fun(long long n)
{
    vector<int>use;
    long long ret = 0;
    if(n%10 == 0)
    {
        n --;
        ret ++;
    }
    while(n)
    {
        use.push_back(n%10);
        n/=10;
    }
    long long ans1 = 1;
    use[use.size()-1] --;
    for(int i=0;i<use.size();i++)
    {
        ans1 += use[i] * pow(10,min(i,(int)use.size()-i-1) );
    }
    long long ans2 = 0;
    for(int i=0;i<use.size();i++)
    {
        ans2 += use[i] * pow(10,i);
    }
    ret = ret + min(ans1,ans2);
    return ret;
}

long long add[17];

int main()
{
    for(long long i=0,now=1;i<17;i++,now*=10)
    {
        add[i] = fun(now-1) + 1;
        //printf("%lld ",add[i]);
    }
    add[0] = 1;
    int ti;
    scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        long long n;scanf("%lld",&n);
        long long ret = 0;
        for(long long i=0,now=1;i<17;i++,now*=10)
        {
            if(n-1 >= now)
                ret += add[i];
            else
                break;
        }
        //printf("%lld ",ret);
        ret += fun(n);
        if(n == 1)
            ret = 1;
        printf("Case #%d: %lld\n",ca, ret);
    }
}

/*
7
3
2
1
19
23
10
100
*/
