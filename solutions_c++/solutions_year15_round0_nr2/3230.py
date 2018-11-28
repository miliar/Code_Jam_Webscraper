#include<stdio.h>
#include<math.h>

#define MAXN 1000

#define MIN(x,y) (x<y?x:y)
#define MAX(x,y) (x>y?x:y)

int main()
{
    int plates[MAXN];
    int test,tcase;
    int d,maxpie;
    int stoppage;
    int i,j;
    int answer;

    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

    scanf("%d",&test);

    for(tcase=1;tcase<=test;tcase++)
    {
        scanf("%d",&d);

        maxpie=0;

        for(i=0;i<d;i++)
        {
            scanf("%d",&plates[i]);
            maxpie=MAX(maxpie,plates[i]);
        }

        answer=maxpie;

        for(i=1;i<=maxpie;i++)
        {
            stoppage=0;

            for(j=0;j<d;j++)
            {
                if(plates[j]<=i)
                    continue;

                stoppage+=(ceil((double)plates[j]/i)-1);
            }

            answer=MIN(answer,stoppage+i);
        }

        printf("Case #%d: %d\n",tcase,answer);
    }

    return 0;
}
