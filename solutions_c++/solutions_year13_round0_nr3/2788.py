#include <cstdio>
#include<cmath>
#define ss(a) scanf("%d",&a)
#define ds(a,b) scanf("%d %d",&a,&b)
int hw[12000];
bool jchw(int x)//检查x平方是否回文
{
    long long a=x,b=0,c;
    a*=a;
    c=a;
    while(c)
    {
        b=b*10+c%10;
        c/=10;
    }
    if(a==b) return true;
    return false;
}
int main()
{
  // freopen("C-small-attempt0.in","r",stdin);
  //freopen("C-small-attempt0.out","w",stdout);
    int i,c=0,j;
    //1
    for(i=1;i<=9;i++)
    hw[c++]=i;
    //2
    for(i=11;i<=99;i+=11)
    hw[c++]=i;
    //3
    for(i=1;i<=9;i++)
    for(j=0;j<=9;j++)
    hw[c++]=i*101+j*10;
    //4
    for(i=10;i<=99;i++)
    hw[c++]=i*101;
    //5
    for(i=10;i<=99;i++)
    for(j=0;j<=9;j++)
    hw[c++]=i*1001+j*100;
    //6
    for(i=100;i<=999;i++)
    hw[c++]=i*1001;
    //7
    for(i=100;i<=999;i++)
    for(j=0;j<=9;j++)
    hw[c++]=i*10001+j*1000;
    int t,k;
    ss(t);
    for(k=1;k<=t;k++)
    {
        long long a,b;
        int ans=0;
        int low,high;
        scanf("%lld %lld",&a,&b);
        low=ceil(sqrt(a+0.0));
        high=floor(sqrt(b+0.0));
       i=0;
       while(hw[i]<low) i++;
       while(hw[i]<=high){if(jchw(hw[i]))ans++;i++;}
      printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
