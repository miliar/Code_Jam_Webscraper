#include <iostream>
#include <stdio.h>

//#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;

int main()
{
    FILE* in, *out;
    if((in=fopen("A-large.in", "rt"))==NULL)
    {
        cout<<"Input file not found."<<endl;
        getchar();
        return 1;
    }
    if((out=fopen("A-large.out", "wt"))==NULL)
    {
        cout<<"Cannot create output file."<<endl;
        getchar();
        return 2;
    }

    int T;
    fscanf(in, "%d", &T);

    for(int t=0; t!=T; ++t)
    {
        int n;
        fscanf(in, "%d", &n);

        vector<int> p(n);
        int sum=0;

        for(int i=0; i<n; ++i)
        {
            fscanf(in, "%d", &p[i]);
            sum +=p[i];
        }

        fprintf(out, "Case #%d:", t+1);

        while(sum>0)
        {
            int max = -1;
            for(int i=0; i<n; ++i)
            {
                if(max==-1 || p[i]>p[max])
                    max=i;
            }
            int nrOfMaxes = 0;
            for(int i=0; i<n; ++i)
            {
                if(p[i]==p[max])
                    ++nrOfMaxes;
            }

            if(nrOfMaxes == 1 || p[max]<=(sum-1)/2)
            {
                fprintf(out, " %c", 'A'+max);
                --p[max];
                --sum;
            }
            else
            {
                int sec = 0;
                for(int i=0; i<n; ++i)
                {
                    if(i != max && p[i] == p[max])
                    {
                        sec=i;
                        break;
                    }
                }
                fprintf(out, " %c%c", 'A'+max, 'A'+sec);
                --p[max]; --p[sec];
                sum-=2;
            }

        }

        fprintf(out, "\n");
    }


    fclose(in);
    fclose(out);
    return 0;
}
