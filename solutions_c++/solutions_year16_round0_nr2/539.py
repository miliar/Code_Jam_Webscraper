#include <iostream>
#include <stdio.h>

#include <string.h>
#include <vector>

using namespace std;

int main()
{
    FILE* in, *out;
    if((in=fopen("B-large.in", "rt"))==NULL)
    {
        cout<<"Input file not found."<<endl;
        getchar();
        return 1;
    }
    if((out=fopen("B-large.out", "wt"))==NULL)
    {
        cout<<"Cannot create output file."<<endl;
        getchar();
        return 2;
    }

    int T;
    char line[200];
    fscanf(in, "%d", &T);
    fgets(line, sizeof(line), in);

    for(int t=0; t!=T; ++t)
    {
        fgets(line, sizeof(line), in);

        int n=strlen(line);
        vector<bool> vals(n+1, false);
        for(int i=0; i<n; ++i)
        {
            if(line[i]=='+')
                vals[i]=true;
            else if(line[i]=='-')
                vals[i]=false;
            else
            {
                n=i;
                break;
            }
        }
        vals[n]=true;
        int c=0;
        for(int i=n-1; i>=0; --i)
        {
            if(vals[i]!=vals[i+1])
                ++c;
        }

        fprintf(out, "Case #%d: %d\n", t+1, c);
    }


    fclose(in);
    fclose(out);
    return 0;
}
