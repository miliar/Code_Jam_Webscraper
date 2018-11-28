#include<stdio.h>
#include<algorithm>
#include<string.h>
#define rep(ii,a,b) for (int ii=(a);ii<=(b);ii++)
#define rek(ii,a,b) for (int ii=(a);ii>=(b);ii--)
using namespace std;
int test,n,j;
int ans[100];
long long my_power(long long a,long long b)
{
    long long ans=1;
    rep(i,1,b) ans=ans*a;
    return ans;
}
long long change(int t){
    return 1+my_power(t,16);
}
void output_a()
{
    rep(i,1,32) printf("%d",ans[i]);
    rep(i,2,10){
        printf(" ");
        printf("%I64d",change(i));
    }
    printf("\n");
}
int main()
{
    //freopen("ainput.in","r",stdin);
    //freopen("coutput.out","w",stdout);
    scanf("%d%d%d",&test,&n,&j);
    printf("Case #1:\n");
    ans[1]=1;
    ans[16]=1;
    ans[32]=1;
    ans[17]=1;
    rep(i,1,j)
    {
        output_a();
        ans[16]+=2;
        ans[32]+=2;
        int t=16;
        while (ans[t]>1){
            ans[t-1]+=ans[t]/2;
            ans[t]=ans[t]%2;
            t--;
        }
        t=32;
        while (ans[t]>1){
            ans[t-1]+=ans[t]/2;
            ans[t]=ans[t]%2;
            t--;
        }
    }
    return 0;
}
