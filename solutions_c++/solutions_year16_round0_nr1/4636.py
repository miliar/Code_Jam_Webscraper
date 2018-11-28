#include<bits/stdc++.h>
using namespace std;

int m[20];
void solve(int x)
{
    memset(m,0,sizeof(m));
    printf("Case #%d: ",x);
    long long n;
    scanf("%lld",&n);
    for(int i=1;i<=10000;i++)
    {
        long long p=i*1ll*n;
        long long tmp=p;
        while(tmp)
        {
            m[tmp%10]=1;
            tmp/=10;
        }
        int num = 0;
        for(int j=0;j<10;j++)
            if(m[j])num++;
        if(num==10)
        {
            cout<<p<<endl;
            return;
        }
    }
    cout<<"INSOMNIA"<<endl;
}
int main()
{
    freopen("233.in","r",stdin);
    freopen("233.out","w",stdout);
    int t;scanf("%d",&t);
    for(int i=1;i<=t;i++)
        solve(i);
    return 0;
}
