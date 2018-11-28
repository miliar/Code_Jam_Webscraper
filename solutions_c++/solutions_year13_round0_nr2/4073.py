#include <cstdio>
#include <algorithm>

using namespace std;


int n,m,t;
int** inp;
int** mod;

int* b;
int* a;

int main()
{
    FILE* be=fopen("B-large.in","r");
    FILE* ki=fopen("out.txt","w");
    fscanf(be,"%d",&t);
    for(int c=0; c<t; c++)
    {
        fscanf(be,"%d %d",&n,&m);
        inp=new int*[n];
        for(int i=0; i<n; i++)
        {
            inp[i]=new int[m];
            for(int j=0; j<m; j++)
            {
                fscanf(be,"%d",&inp[i][j]);
            }
        }
      /*  for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                printf("%d ",inp[i][j]);
            }
            printf("\n");
        }


        printf("\n");*/

        b=new int[n];
        for(int i=0;i<n;i++)
        {
            b[i]=0;
            for(int j=0; j<m; j++)
            {
                if(inp[i][j]>b[i])
                {
                    b[i]=inp[i][j];
                }
            }
         //   printf("%d ",b[i]);
        }
       // printf("\n");


        a=new int[m];
        for(int j=0;j<m;j++)
        {
            a[j]=0;
            for(int i=0; i<n; i++)
            {
                if(inp[i][j]>a[j])
                {
                    a[j]=inp[i][j];
                }
            }
         //   printf("%d ",a[j]);
        }
      //  printf("\n");

        bool answ=true;
        //fprintf(ki,"Case #%d: ",c+1);
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                if (inp[i][j]!=min(b[i],a[j]))
                {
                    answ=false;
                }
            }
        }
        if (answ)
        {
            fprintf(ki,"Case #%d: YES\n",c+1);
        }
        else
        {
            fprintf(ki,"Case #%d: NO\n",c+1);
        }
        //fprintf(ki,"\n");

    }




    fclose(be);
    fclose(ki);
    return 0;
}
