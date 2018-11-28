#include<bits/stdc++.h>
using namespace std;
double c,f,x;
int flag;
double dfs(double target,double speed)
{
    double ret=target/speed;
    if((speed-2)/f*c>target)  return ret;
    double ret2=c/speed+dfs(target,speed+f);
    return min(ret,ret2);
}
int main()
{
    freopen("b.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
        flag=0;
        scanf("%lf %lf %lf",&c,&f,&x);
        printf("Case #%d: %.7lf\n",cas++,dfs(x,2));
    }
    return 0;
}
