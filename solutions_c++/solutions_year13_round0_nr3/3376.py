#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;

bool pal(int n)
{
    int a=n;
    int b=0;
    while(n)
    {
        b=b*10+n%10;
        n/=10;
    }
    if(a==b) return true;
    else return false;
}
bool cal(int n)
{
    if(pal(n))
    {
        int m=sqrt(n);
        if(m*m==n && pal(m)) return true;
        else return false;
    }
    else return false;
}
int main()
{
    freopen("D:\\in.txt","r",stdin);
    freopen("D:\\out.txt","w",stdout);
    int t,a,b;
    scanf("%d",&t);
    for(int cas=1;t--;cas++)
    {
        int cnt=0;
        scanf("%d%d",&a,&b);
        for(int i=a;i<=b;i++)
        {
            if(cal(i)) cnt++;
        }
        printf("Case #%d: %d\n",cas,cnt);
    }
}
