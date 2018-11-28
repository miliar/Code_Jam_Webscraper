#include<cstdio>
using namespace std;
int ans;
long long int gcd(long long int x,long long int y)
{
    	return y==0 ? x : gcd(y,x%y);
}
void rec(long long x,long long y,int n)
{
    int tmp=1,temp=n;
    ans++;
    while(temp<y){
        tmp *=2;
        temp*=2;
    }
    if(x>=tmp)
    {
        return;
    }
    else
        rec(x,y,n*2);
    return;
}
int main (){
freopen("A-small-attempt0.in","r",stdin);
freopen("A-small-attempt0.out","w",stdout);
int cas;
scanf("%d",&cas);
for(int n=1;n<=cas;n++)
{
    long long int a,b;
    scanf("%lld/%lld",&a,&b);
    printf("Case #%d: ",n);
    long long GCD=gcd(a,b);
    b/=GCD; a/=GCD;
    int tmp=b;ans=0;
    while(tmp%2==0){
        tmp/=2;
    }
    if(tmp!=1)
    {
        puts("impossible");
        continue;
    }
    else
        rec(a,b,2);
    printf("%d\n",ans);

}
}
