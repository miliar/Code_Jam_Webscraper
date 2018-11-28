#include <stdio.h>
int main()
{
    int ts,cs=1;
    double c,f,t,last,ans,now,lf;
    //freopen("B-small-attempt7.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    scanf("%d",&ts);
    while(ts--)
    {
        scanf("%lf%lf%lf",&c,&f,&t);
        lf=2;

        int co=0;
        double ttime=0,div=f+lf;
        last=0;
        now=0;

        while(1)
        {
            co++;
            //if(co==5) break;
            last=ttime+(t/lf);
            now=ttime+(c/lf)+(t/div);
            //printf("%lf %lf: %lf(%.2lf %.2lf)\n",last,now,c/lf,c,lf);
            if(now>last)
            {
                ans=last;
                break;
            }
            if(now<=last)
            {
                last=now;
                ttime+=(c/lf);
               //printf("\nttime = %lf\n",ttime);
            }
            div=lf+f;
            lf=div;
            div=lf+f;
            //co++;
            //if(co==7) break;

        }
        //printf("%lf\n",ttime);
        printf("Case #%d: %.10lf\n",cs++,ans);
    }
    return 0;
}

