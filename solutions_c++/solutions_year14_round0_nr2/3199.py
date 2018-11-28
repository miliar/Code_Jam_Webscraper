#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int t,i=1,flag,cnt;
    double c,f,x,a,m,s,y,z;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        a=2.0;
        m=x;
        s=0.0;
        flag=0;
        y=0;
        z=0;
        while(flag==0)
        {
            z=y+x/a;
            y=y+c/a;
            if(z<m)
            {
                m=z;
            }
            else{
                flag=1;
            }
            a=a+f;
        }
        printf("Case #%d: %.7f\n",i,m);
        i=i+1;
    }
}
