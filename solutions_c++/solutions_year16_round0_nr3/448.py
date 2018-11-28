#include <iostream>
#include <stdio.h>

//#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

long long Pow(long long x, int p) {
  if (p == 0) return 1;
  if (p == 1) return x;
  return x * Pow(x, p-1);
}

int main()
{
    FILE* in, *out;
    if((in=fopen("test.in", "rt"))==NULL)
    {
        cout<<"Input file not found."<<endl;
        getchar();
        return 1;
    }
    if((out=fopen("test.out", "wt"))==NULL)
    {
        cout<<"Cannot create output file."<<endl;
        getchar();
        return 2;
    }

    int T;
    fscanf(in, "%d", &T);

    for(int t=0; t!=T; ++t)
    {
        int n, j;
        fscanf(in, "%d", &n);
        fscanf(in, "%d", &j);
        int f=0;
        fprintf(out, "Case #%d: \n", t+1);

        for(long long i=0; i<=Pow(2, n-2); ++i)
        {
            vector<bool> bits(n, false);
            bits[0]=true;
            bits[n-1]=true;

            int temp=i;
            for(int h=1; h<n-1; ++h)
            {
                if(temp%2==1) bits[h]=true;
                temp/=2;
            }

            bool good=true;
            vector<long> div(11, 0);

            int sum=0;
            for(int h=0; h<n; ++h)
                if(bits[h])
                {
                    if(h%2==0)
                        ++sum;
                    else
                        --sum;
                }
            if(sum!=0)
                continue;

            for(int b=2; b<11; ++b)
                div[b]=b+1;


            if(good)
            {
                for(int h=n-1; h>=0; --h)
                {
                    if(bits[h]) fprintf(out, "1");
                    else fprintf(out, "0");
                }
                for(int b=2; b<11; ++b)
                    fprintf(out, " %ld", div[b]);

                fprintf(out, "\n");

                ++f;
                if(f==j) break;
            }

        }
    }


    fclose(in);
    fclose(out);
    return 0;
}
