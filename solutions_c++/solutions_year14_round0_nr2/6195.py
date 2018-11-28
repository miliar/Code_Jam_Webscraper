#include <stdio.h>
#include <string.h>
#define INF 0x3f3f3f3f
int main()
{
    int T;
    scanf("%d",&T);
    int C=1;
    while(T--)
    {
        double c,f,x,past,tmp,speed;
        scanf("%lf%lf%lf",&c,&f,&x);
        past=INF;
        speed=2;
        tmp=0;
        while(tmp+x/speed<=past)
        {
            past=tmp+x/speed;
            tmp+=c/speed;
            speed+=f;
        }
        printf("Case #%d: ",C++);
        printf("%0.7f\n",past);
    }
    return 0;
}