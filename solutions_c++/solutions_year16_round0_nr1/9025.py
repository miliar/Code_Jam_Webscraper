#include <stdio.h>
#include <stdlib.h>

int main()
{
    int T;
    int N;
    int A[10];
    int i;
    int sum=0;
    int temp;
    FILE *fin ,*fout;
    fin = fopen("input.in","r");
    fout = fopen("output.txt","w");

    fscanf(fin,"%d",&T);
    int x=T;
    while(T--)
    {

        for(i=0;i<10;i++)
        {
            A[i] = 0;
        }

        fscanf(fin,"%d",&N);
        i=1;
        if(N == 0)
        {
                fprintf(fout,"Case #%d: INSOMNIA\n",x-T);
                continue;
        }
        while(sum!=10)
        {
            temp = N*i;
            while(temp>0)
            {
                if(A[temp%10] == 0)
                {
                    A[temp%10] = 1;
                    sum = sum + 1;

                }
                //printf("%d\n",temp);
                temp = temp/10;
            }
            i++;

        }
         sum = 0;

        fprintf(fout,"Case #%d: %d\n",x-T,N*(i-1));
    }
    return 0;

}

