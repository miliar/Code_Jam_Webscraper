#include <iostream>
#include <stdio.h>

//#include <algorithm>
#include <vector>

using namespace std;

long long Pow(long long x, int p) {
  if (p == 0) return 1;
  if (p == 1) return x;
  return x * Pow(x, p-1);
}

int main()
{
    FILE* in, *out;
    if((in=fopen("D-large.in", "rt"))==NULL)
    {
        cout<<"Input file not found."<<endl;
        getchar();
        return 1;
    }
    if((out=fopen("D-large.out", "wt"))==NULL)
    {
        cout<<"Cannot create output file."<<endl;
        getchar();
        return 2;
    }

    int T;
    fscanf(in, "%d", &T);

    for(int t=0; t!=T; ++t)
    {
        int k, c, s;
        fscanf(in, "%d", &k);
        fscanf(in, "%d", &c);
        fscanf(in, "%d", &s);

        fprintf(out, "Case #%d: ", t+1);

        if(c*s<k)
        {
            fprintf(out, "IMPOSSIBLE\n");
            continue;
        }

        long long code=0;

        for(long long i=0; i<s; ++i)
        {
            bool fin=false;
            long long pos=1;
            for(long long j=0; j<c; ++j)
            {
                pos+=(long long)code*Pow((long long)k, j);
                if(code<k-1)
                    ++code;
                else
                    fin=true;
            }

            fprintf(out, "%lld ", pos);
            if(fin) break;
        }

        fprintf(out, "\n");

    }


    fclose(in);
    fclose(out);
    return 0;
}
