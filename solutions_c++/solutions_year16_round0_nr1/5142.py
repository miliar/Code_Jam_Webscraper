#include<bits/stdc++.h>
#define ii long long int

using namespace std;

int cnt[10];

bool check()
{
    for(int i=0;i<10;i++)
    {
        if(cnt[i]==0)
        {
            return 0;
        }
    }
    return 1;
}

void func(ii ans)
{
    while(ans!=0)
    {
        cnt[ans%10]=1;
        ans/=10;
    }
}

int main()
{
    //freopen("out.txt","w",stdout);
    int test;
    int cas=1;
    scanf("%d",&test);
    while(test--)
    {
        ii n;
        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",cas++);
            continue;
        }
        ii temp=1;
        ii ans;
        while(!check())
        {
            ans=n*temp;
            //cout<<"ans "<<ans<<endl;
            func(ans);
            temp++;
        }
        printf("Case #%d: %lld\n",cas++,ans);
        memset(cnt,0,sizeof cnt);
    }
    return 0;
}
