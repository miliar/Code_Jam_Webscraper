#include <iostream>
#include <stdio.h>

//#include <algorithm>
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

        vector<bool> dig(10, false);
        int trues=0;

        int val=0;
        for(int i=0; i<100; ++i)
        {
            val+=n;
            int h=val;
            while(h>0)
            {
                int g=h%10;
                if(dig[g]==false) ++trues;
                dig[g]=true;
                h=h/10;
            }
            if(trues==10)
                break;
        }

        if(trues==10)
            fprintf(out, "Case #%d: %d\n", t+1, val);
        else
            fprintf(out, "Case #%d: INSOMNIA\n", t+1);
    }


    fclose(in);
    fclose(out);
    return 0;
}
