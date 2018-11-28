#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

int st,en;
bool judge(long long x)
{
    if (x<10) return true;
    long long tmp=10;
    while (x/tmp>=10) tmp*=10;
    if (x/tmp != x%10) return false;
    else return judge((x-(x/tmp)*tmp-x%10)/10);
}

int main()
{
    int T;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int cases=1;cases<=T;cases++)
    {
        int ans=0;
        long long t1,t2;
        scanf("%lld%lld",&t1,&t2);
        if (t1>t2) swap(t1,t2);
        st=(int)(sqrt((double)t1));
        if (st*st<t1) st++;
        en=(int)(sqrt((double)t2));

        //printf("%d %d\n",st,en);
        for (int i=st;i<=en;i++)
            if (judge(i))
            if (judge((long long)i*(long long)i))
                {ans++;}
        printf("Case #%d: %d\n",cases,ans);
    }
    return 0;
}
