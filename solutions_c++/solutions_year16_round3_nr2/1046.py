#include <iostream>
#include <stdio.h>

//#include <algorithm>
#include <string.h>

using namespace std;

long Pow(long x, int p) {
  if (p == 0) return 1;
  if (p == 1) return x;
  return x * Pow(x, p-1);
}

int main()
{
    FILE* in, *out;
    if((in=fopen("B-small-attempt0.in", "rt"))==NULL)
    {
        cout<<"Input file not found."<<endl;
        getchar();
        return 1;
    }
    if((out=fopen("B-small-attempt0.out", "wt"))==NULL)
    {
        cout<<"Cannot create output file."<<endl;
        getchar();
        return 2;
    }

    int T;
    fscanf(in, "%d", &T);

    for(int t=0; t!=T; ++t)
    {
        long b, m;
        fscanf(in, "%ld", &b);
        fscanf(in, "%ld", &m);

        long maxMods = Pow(2, (b-2));

        if(maxMods<m)
        {
            fprintf(out, "Case #%d: IMPOSSIBLE\n", t+1);
            continue;
        }

        fprintf(out, "Case #%d: POSSIBLE\n", t+1);

        if(maxMods == m)
        {
            for(int i=0; i<b; ++i)
            {
                for(int j=0; j<b; ++j)
                {
                    if(i<j) fprintf(out, "1");
                    else fprintf(out, "0");
                }
                fprintf(out, "\n");
            }
            continue;
        }

        for(int i=0; i<b; ++i)
        {
            for(int j=0; j<b-1; ++j)
            {
                if(i<j) fprintf(out, "1");
                else fprintf(out, "0");
            }

            if(i==0)
            {
                fprintf(out, "0\n");
                continue;
            }

            if(m%2 == 1) fprintf(out, "1\n");
            else fprintf(out, "0\n");

            m/=2;
        }

    }


    fclose(in);
    fclose(out);
    return 0;
}
