#include<stdio.h>
#include<algorithm>
using namespace std;

FILE *out;

int a[4][4];
int hash[18] = {0};

int main()
{
    int t,i,j,k,ans,res,count = 0;
    FILE *fp = fopen("A-small-attempt0.in", "r");
    out = fopen("A-small-attempt0.out", "w");
    fscanf(fp, "%d", &t);
    for (k = 1; (k <= t) && !feof(fp) ; k++)
    {
        fscanf(fp, "%d", &ans);

        for(i = 0; i < 17; i++)
        hash[i] = 0;

        for(i = 0; i < 4; i++)
        {
            for(j = 0; j < 4; j++)
            {
                fscanf(fp, "%d", &a[i][j]);
                if(i == (ans - 1))
                {
                    hash[a[i][j]] = hash[a[i][j]] + 1;
                }
            }
        }

        fscanf(fp, "%d", &ans);
        for(i = 0; i < 4; i++)
        {
            for(j = 0; j < 4; j++)
            {
                fscanf(fp, "%d", &a[i][j]);
                if(i == (ans - 1))
                {
                    hash[a[i][j]] = hash[a[i][j]] + 1;
                }
            }
        }

        count = 0;


        for(i = 0; i < 17; i++)
        {
            if(hash[i] == 2)
            {
                count++;
                res = i;
            }
        }

        fprintf(out,"Case #%d: ",k);
        if(count == 1)
        fprintf(out,"%d\n",res);
        if(count > 1)
        fprintf(out,"Bad magician!\n");
        if(count == 0)
        fprintf(out,"Volunteer cheated!\n");

    }

    return 0;
}
