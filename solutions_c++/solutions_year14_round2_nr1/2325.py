#include <stdlib.h>
#include <stdio.h>

char w[102][102];
int v[102][102];
int n,m,answer;
char c;
int t;
bool ok;
FILE *f, *g;

int read()
{
    int mm;
    for (int i=1;i<n;i++)
        {
            mm = 0;

            fscanf(f,"%c",&c);
            w[i][0]=c;
            v[i][0] = 0;
            while(c!='\n')
            {
                if (w[i][mm]!=c) {
                    mm++;
                    w[i][mm] = c;
                    v[i][mm] = 1;
                }
                else
                {
                    v[i][mm]++;
                }
                fscanf(f,"%c",&c);
            }

            if (mm+1!=m) return 1;
        }

    return 0;
}

int main()
{
    f = fopen("Ain.txt","r");
    g = fopen("Aout.txt","w");

    fscanf(f,"%d",&t);

    for (int test=1;test<=t;test++)
    {
        fscanf(f,"%d\n",&n);

        m = 0;
        fscanf(f,"%c",&c);
        w[0][0] = c;
        v[0][0] = 0;
        while(c!='\n')
        {
            if (w[0][m]!=c) {
                m++;
                w[0][m] = c;
                v[0][m] = 1;
            }
            else
            {
                v[0][m]++;
            }
            fscanf(f,"%c",&c);
        }
        m++;

        if (read()==1)
        {
            fprintf(g,"Case #%d: Fegla Won\n",test);
            continue;
        }

        ok = true;
        for (int j=0;j<m && ok;j++)
        {
            v[n][j] = 0;
            for (int i=0;i<n-1 && ok;i++)
            {
                v[n][j]+=v[i][j];

                if (w[i][j]!=w[i+1][j]){
                    fprintf(g,"Case #%d: Fegla Won\n",test);
                    ok = false;
                }
            }
            v[n][j]+=v[n-1][j];

            v[n][j] = v[n][j]/n;
        }

        if (!ok) continue;

        answer = 0;
        for (int j=0;j<m;j++)
        {
            for (int i=0;i<n;i++)
            {
                answer+=abs(v[n][j]-v[i][j]);
            }
        }

/*
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<m;j++)
            {
                printf("-%c%d-",w[i][j],v[i][j]);
            }
            printf("\n");
        }

        for (int i=0;i<m;i++) printf("-%d-",v[n][i]);
        printf("\n------------------------------\n");
*/
        fprintf(g,"Case #%d: %d\n",test,answer);
    }

    fclose(f);
    fclose(g);
}
