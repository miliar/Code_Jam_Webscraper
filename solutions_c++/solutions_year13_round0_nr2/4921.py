#include <cstdio>
#include <algorithm>
using namespace std;

FILE *in,*out;
int N,M;
int ar[105][105];
int maxr[105],maxc[105];

int read()
{
    int t,z,v;
    fscanf(in,"%d %d",&N,&M);
    for(t=0;t<N;t++)
        for(z=0;z<M;z++)
            fscanf(in,"%d",&ar[t][z]);
    return 0;
}

int check()
{
    int t,z,v;
    for(t=0;t<N;t++)
    {
        for(z=0,v=0;z<M;z++)
            v=v>ar[t][z]?v:ar[t][z];
        maxr[t]=v;
    }
    for(t=0;t<M;t++)
    {
        for(z=0,v=0;z<N;z++)
            v=v>ar[z][t]?v:ar[z][t];
        maxc[t]=v;
    }
    for(t=0;t<N;t++)
        for(z=0;z<M;z++)
            if(ar[t][z]<maxr[t] && ar[t][z]<maxc[z])
                return 0;
    return 1;
}

int main()
{
    in = fopen("input","r");
    out= fopen("output","w");
    int t,z,v,test;
    fscanf(in,"%d",&test);
    for(t=0;t<test;t++)
    {
        fprintf(out,"Case #%d: ",t+1);
        read();
        z=check();
        if(z==0) fprintf(out,"NO\n");
        else fprintf(out,"YES\n");
    }
    return 0;
}
