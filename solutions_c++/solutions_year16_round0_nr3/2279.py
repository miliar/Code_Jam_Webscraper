#include<bits/stdc++.h>
using namespace std;
int n;
int ok(long long x,int k)
{
    vector<long long>lis(32);
    long long y=x,t=0;
    for(int p=n-1;y;y/=2)lis[p--]=y&1;
    lis[0]=1;

    for(int i=2,_t;i<20000;i++)
    {
        _t=0;
        for(int j=0;j<n;j++)
            _t=(_t*k+lis[j])%i;
        if(_t%i==0)
            return i;
    }
    return 0;
}

int main()
{
    freopen("max.txt","w",stdout);
    scanf("%d",&n);
    int J;
    scanf("%d%d",&n,&J);
    vector<int>ans;
    int cc[11];
    long long tt=1ll<<(n-1);
    puts("Case #1:");
    for(long long i=1,fg;i<tt;i+=2)
    {
        if(ans.size()>=J)break;
        fg=1;
        for(int j=2;j<=10;j++)
        {
            cc[j]=ok(i,j);
            if(!cc[j])
            {
                fg=0;
                break;
            }
        }
        if(fg)
        {
            ans.push_back(i);
            //printf("%d ",i);
            vector<long long>lis(32);
            for(int p=n-1,y=i;y;y/=2)lis[p--]=y&1;
            lis[0]=1;
            for(int j=0;j<n;j++)printf("%d",lis[j]);putchar(' ');
            for(int j=2;j<=10;j++)printf("%d%c",cc[j],j==10?'\n':' ');
        }
    }
    return 0;
}
