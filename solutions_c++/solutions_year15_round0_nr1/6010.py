#include <iostream>
#include <cstdio>

FILE *fin = fopen("input.txt","r");
FILE *fout = fopen("output.txt","w");
using namespace std;
void proc()
{
    char ppl[2000];
    int pl=0;
    int add=0;
    int n;

    fscanf(fin,"%d %s",&n,ppl);
    n++;
    for(int i=0;i<n;i++)
    {
        if(pl>=i)
        {
            pl+=int(ppl[i]-'0');
        }
        else
        {
            if(ppl[i])
            {
                add+=(i-pl);
                pl=i+int(ppl[i]-'0');
            }
        }
    }
    fprintf(fout,"%d\n",add);
}
int main()
{
    int t;
    fscanf(fin,"%d",&t);
    for(int i=0;i<t;i++)
    {
        fprintf(fout,"Case #%d: ",i+1);
        proc();
    }
    return 0;
}
