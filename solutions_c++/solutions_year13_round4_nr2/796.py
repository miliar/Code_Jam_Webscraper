#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;
long long  T,n,p,ans1,ans2;


long long search1(int n,long long i)
{
    if (i==0) return 1;
    if (i==((1<<n)-1)) return ((1<<n));
    return (1<<(n-1))+search1(n-1,(i-1)/2);
}

long long search2(int n,long long i)
{
    if (i==0) return (1<<n);
    if (i==((1<<n)-1)) return ((1<<n));
    return search2(n-1,(i-1)/2);
}


int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    cin>>T;
    for (int tt=1; tt<=T; ++tt)
    {
        cin>>n>>p;
        long long left=0;
        long long right=(1<<n)-1;
        while (left+1<right)
        {
            long long mid=(left+right)/2;
            long long c=search1(n,mid);
            if (c<=p) left=mid;
            else right=mid;
        }
        long long  t;
        for (t=right; t>=left; t--)
        {
            long long c=search1(n,t);
            if (c<=p) break;
        }
        ans1=t;


        left=0;
        right=(1<<n)-1;
        while (left+1<right)
        {
            long long mid=(left+right)/2;
            long long c=search2(n,(1<<n)-mid-1);
            if (c<=p) left=mid;
            else right=mid;
        }
        //cout<<search2(3,2)<<endl;
        for (t=right; t>=left; t--)
        {
            long long c=search2(n,(1<<n)-t-1);
            if (c<=p) break;
        }
        ans2=t;
        if (t==-1) ans2=0;
        cout<<"Case #"<<tt<<": "<<ans1<<" "<<ans2<<endl;
    }
    return 0;
}
