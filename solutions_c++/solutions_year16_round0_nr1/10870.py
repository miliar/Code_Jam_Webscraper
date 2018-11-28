#include<stdio.h>

int check[10];

int check_fill()
{
    int counter=0,i;
    for(i=0; i<10; i++)
    {
        if(check[i]>0)
        {
            counter++;
        }
    }

    return counter;
}

void dig(long long in)
{
    long long r;
    while(1)
    {
        r=in%10;
        check[r]=1;
        in=in/10;
        if(in==0) break;
    }
    return;
}


int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("out_large.txt","w",stdout);

    int CASE, C,i;
    long long input,input_sum;

    scanf("%d",&CASE);

    for(C=1; C<=CASE; C++)
    {
        scanf("%lld",&input);

        if(input==0)
        {
            printf("Case #%d: INSOMNIA\n",C);
        }
        else
        {
            //initial all by zero
            for(i=0; i<10; i++)
            {
                check[i]=0;
            }

            input_sum=0;
            while(1)
            {
                //printf("%lld\n",input_sum);

                input_sum=input_sum+input;
                dig(input_sum);

                if(check_fill()==10)
                {
                    break;
                }
            }

            printf("Case #%d: %lld\n",C,input_sum);

        }
    }
}

