#include <stdio.h>


FILE *fi,*fo;
int main()
{
   int T,i;
    fi=fopen("in.txt","r");
    fo=fopen("out.txt","w");

    fscanf(fi,"%d",&T);
    for(i=1;i<=T;i++)
    {
        int a,b,c,N,M,arr[100][100],maxR[100],maxC[100];
        fscanf(fi,"%d %d",&N,&M);
        for(a=0;a<N;a++)
        {
            fscanf(fi,"%d",&arr[a][0]);
            maxR[a]=arr[a][0];

            for(b=1;b<M;b++)
            {
                fscanf(fi,"%d",&arr[a][b]);
                if(arr[a][b]>maxR[a])
                {
                 maxR[a]=arr[a][b];
                }
            }

        }
        for(a=0;a<M;a++)
        {

            maxC[a]=arr[0][a];

            for(b=1;b<N;b++)
            {

                if(arr[b][a]>maxC[a])
                {
                 maxC[a]=arr[b][a];
                }
            }

        }
        int flag=0;
        for(a=0;a<N;a++)
        {
            for(b=0;b<M;b++)
            {
                if(arr[a][b]!=maxR[a]&&arr[a][b]!=maxC[b])
                {
                    flag=1;
                    break;
                }

            }
        }
        if(flag)
        fprintf(fo,"Case #%d: NO\n",i);
        else
        fprintf(fo,"Case #%d: YES\n",i);


    }

    return 0;
}
