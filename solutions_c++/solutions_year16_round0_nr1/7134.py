#include<iostream>
#include<cstdio>
#include<fstream>

using namespace std;

int a[16];
int l,br=10;
long long k;

void clr()
{
    for(int i=0;i<16;i++)
    {
        a[i]=0;
    }
    br=10;
}

void solve()
{
    if(k==0)
    {
        printf("Case #%d: INSOMNIA\n",l+1);
        return;
    }

    clr();
    int num,p=1;
    while(1)
    {
        num=k*p;
        while(num)
        {
            if(a[num%10]==0)
            {
                a[num%10]=1;
                br--;
            }
            if(br==0)
            {
                printf("Case #%d: %d\n",l+1,k*p);
                return;
            }
            num/=10;
        }
        p++;
    }
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(l=0;l<t;l++)
    {
        scanf("%d",&k);
        solve();
    }
    return 0;
}
