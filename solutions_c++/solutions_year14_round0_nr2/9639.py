#include<iostream>
#include<cstdio>
using namespace std;
int main(void)
{
    int i,j,k,t,inp=0;
    double c,f,x,s,time1,time2,time3;
    scanf("%d",&t);
    while(t--)
    {
        inp++;
        time1=0;
        time2=0;
        time3=0;
        scanf("%lf%lf%lf",&c,&f,&x);
        s=2;
        while(1)
        {
            time1=time3+x/s;
            time2=time3+(c/s)+(x/(f+s));
            time3+=(c/s);
            s+=f;
            if(time1<=time2)
                break;
        }
        printf("Case #%d: %lf\n",inp,time1);
    }
    return 0;
}
