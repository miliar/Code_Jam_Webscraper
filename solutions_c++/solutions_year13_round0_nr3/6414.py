#include <cstdio>
#include <cmath>
int main()
{
    int i,j,start,stop,loop,num,check;
    num=0;
    scanf("%d",&loop);
    for (i=0;i<loop;i++)
    {
        num=0;
        scanf("%d %d",&start,&stop);
        if(start>stop)
        {
            break;
        }
        for (j=start;j<=stop;j++)
        {
            check=sqrt(j);
            if (j==1 || j==4 || j==9)
            {
                num=num+1;
            }
            else
            {
                if (j>100)
                {
                    if(j%10==j/100 && (j==(sqrt(j)*sqrt(j))))
                    {
                        if(sqrt(j)>10 && sqrt(j)<100)
                        {
                            if(check%10==check/10)
                            {
                                num=num+1;
                            }
                        }
                        else
                        {
                            printf("%d",j);
                            num=num+1;
                        }
                    }
                }
            }
        }
        freopen("output.txt","a",stdout);
        printf("Case #%d: %d\n",i+1,num);
        fclose(stdout);
    }
    return 0;
}
