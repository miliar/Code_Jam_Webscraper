#include<bits/stdc++.h>
#define LL long long int

using namespace std;
int aa[12];

int digits(LL m)
{
    do{
        aa[m%10]=1;
        m=m/10;
    }
    while(m!=0);
    return 0;
}
bool checks()
{
    for(int i=0;i<10;i++)
    {
        if(aa[i]==0)return 0;
    }
    return 1;
}
int cals(int m)
{
    for(int i=0;i<11;i++)
    aa[i]=0;
    LL i=2,mm=m;
    while(true)
    {
        digits(mm);
        if(checks())
        break;
        mm=m*i;
        i++;
    }
    printf("%lld\n",mm);
    return 0;
}

int main()
{
    //ios_base::sync_with_stdio(0);
    freopen("intput.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,n,ii;
    scanf("%d",&t);
    for( ii=1;ii<=t;ii++)
    {
        scanf("%d",&n);
        printf("Case #%d: ",ii);
        if(n==0)
        printf("INSOMNIA\n");
        else
        {
            cals(n);
        }

    }
    return 0;
}
