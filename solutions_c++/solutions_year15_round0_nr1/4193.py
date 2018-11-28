#include<stdio.h>
using namespace std;

main()
{
    int t=0;

    scanf("%d",&t);

    int i=0,smax,j;

    char a[1005]="\0";


    for(i=0;i<t;i++)
    {
        scanf("%d %s",&smax,&a);
        int s=0,c=0;

       // printf("\n\nsmax=%d,a=%s",smax,a);
        for(int k=0;k<=smax;k++)

            {
                int x=a[k]-48;


               // printf("\nx=%d,s=%d,c=%d\n",x,s,c);
                if(s<k)
                {
                    c=c+(k-s);
                    s=k;
                    s=s+x;
                }

                else
                s=s+x;
            }


        printf("Case #%d: %d\n",i+1,c);

    }



}


