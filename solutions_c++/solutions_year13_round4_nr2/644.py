#include<cstdio>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;

int n;

long long check1(long long t)
{
    long long n1=t;
    long long n2=((long long)1<<n)-1-t;
    //cout<<"~"<<t<<" "<<n1<<" "<<n2<<endl;
    long long tmp=(long long)1<<(n-1);
    long long ret=0;
    for (int i=n;i>0;i--)
    {
        if (n1) ret+=tmp;
        if (n1-1<=n2)
        {
            n2=((long long)1<<i)-n1-1;
        }
        else
        {
            n1=((long long)1<<i)-1;
        }
        tmp>>=1;
    }
    return ret;
}

long long check2(long long t)
{
    long long n1=t;
    long long n2=((long long)1<<n)-1-t;
    //cout<<"`"<<t<<" "<<n1<<" "<<n2<<endl;
    long long tmp=(long long)1<<(n-1);
    long long ret=0;
        for (int i=n;i>0;i--)
    {
        if (n2) ret+=tmp;
        if (n1-1<=n2)
        {
            n1=((long long)1<<i)-n1-1;
        }
        else
        {
            n2=((long long)1<<i)-1;
        }
        tmp>>=1;
    }
    return ret;
}

int main()
{
    //freopen("B.in","r",stdin);
    //freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;t++)
    {
        long long p;
        cin>>n>>p;

        p--;
        long long l=0,r=((long long)1<<n)-1;
        long long ans1,ans2;
        while (r-l>1)
        {
            long long mid=(l+r)>>1;
            if (check1(mid)<=p) l=mid;
            else r=mid-1;
        }
        if (check1(r)<=p) ans1=r;
        else ans1=l;
        l=0,r=((long long)1<<n)-1;
        while (r-l>1)
        {
            long long mid=(l+r)>>1;
            if (check2(mid)<=p) l=mid;
            else r=mid-1;
        }
        if (check2(r)<=p) ans2=r;
        else ans2=l;
        printf("Case #%d: %I64d %I64d\n",t,ans1,ans2);

    }
    return 0;
}
