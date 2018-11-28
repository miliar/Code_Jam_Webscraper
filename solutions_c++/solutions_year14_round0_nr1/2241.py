#include <iostream>
#include <cstdio>
using namespace std;

int t;
int s[20];
int e;
int aaa=0;

int main()
{
    FILE *in = fopen("a.in", "r");
    FILE *out = fopen("a.out", "w");
    fscanf(in, "%d", &t);

    while (t>0)
    {
        aaa++;
        for (int i=1;i<=17;i++) s[i]=0;
        int v;
        fscanf(in, "%d", &v);
        for (int i=1;i<v;i++)
        {
            for (int j=1;j<=4;j++)fscanf(in, "%d", &e);
        }
        for (int j=1;j<=4;j++)
        {
            fscanf(in, "%d", &e);
            s[e]++;
        }
        for (int i=v+1;i<=4;i++)
        {
            for (int j=1;j<=4;j++)fscanf(in, "%d", &e);
        }

        fscanf(in, "%d", &v);
        for (int i=1;i<v;i++)
        {
            for (int j=1;j<=4;j++)fscanf(in, "%d", &e);
        }
        for (int j=1;j<=4;j++)
        {
            fscanf(in, "%d", &e);
            s[e]++;
        }
        for (int i=v+1;i<=4;i++)
        {
            for (int j=1;j<=4;j++)fscanf(in, "%d", &e);
        }

        int bm=0;
        int ans=-1;
        for (int i=1;i<=16;i++)
        {
            if (s[i]==2)
            {
                ans=i;
                bm++;
            }
        }
        fprintf(out, "Case #%d: ", aaa);
        if (bm==0)
        {
            fprintf(out, "Volunteer cheated!\n");
        }
        if (bm>=2)
        {
            fprintf(out, "Bad magician!\n");
        }
        if (bm==1)
        {
            fprintf(out, "%d\n", ans);
        }

        t--;
    }
    fclose(out);
    return 0;
}
