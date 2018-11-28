#include <stdio.h>

int rate_min(int mush[], int intervalo)
{
    int minimum = mush[0] - mush[1];
    for(int i = 1 ; i < intervalo - 1; i++)
    {
        if(minimum < mush[i] - mush[i+1])
            minimum = mush[i] - mush[i+1];
    }

    return minimum;

}

int main()
{
    int mush[1200];
    int num,intervalo,rate;
    long int res1,res2;

    scanf("%d",&num);
    for(int i =0 ; i < num ; i++)
    {
        res1 = res2 = 0;
        scanf("%d",&intervalo);
        for(int j =0 ; j < intervalo ; j++)
            scanf("%d ",&mush[j]);

        rate = rate_min(mush,intervalo);

        for(int j =0 ; j < intervalo - 1 ; j++)
        {
            if(mush[j+1] - mush[j] < 0)
                res1+= mush[j] - mush[j+1];


            if(rate > mush[j])
                res2 += mush[j];
            else
                res2 += rate;
        }

        //printf("%d\n",rate);
        printf("Case #%d: %ld %ld\n",i+1,res1,res2);
            //printf("%d ",mush[j]);

    }


    return 0;
}
