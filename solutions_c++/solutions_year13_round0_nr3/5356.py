#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<string>
using namespace std;
int check(int x)
{
    double t=x,p;
    int tp;
    p=sqrt(t);
    if(ceil(p)!=floor(p))return 0;
    tp=p;
    string s,s1,s2,s3;
    while(x)
    {
        s+=(x%10+'0');
        x/=10;
    }
    s1=s;
    reverse(s.begin(),s.end());
    while(tp)
    {
        s2+=(tp%10+'0');
        tp/=10;
    }
    s3=s2;
    reverse(s2.begin(),s2.end());
    return (s==s1&&s2==s3);
}
int main()
{
    int t=0,T;
    scanf("%d",&T);
    while(t++<T)
    {
        int i,a,b,br=0;
        scanf("%d%d",&a,&b);
        for(i=a;i<=b;i++)
        {
            br+=check(i);
        }
        printf("Case #%d: %d\n",t,br);
    }
    return 0;
}