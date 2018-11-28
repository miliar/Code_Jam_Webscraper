#include <iostream>
#include<cstdio>

using namespace std;

int main()
{
    FILE* in=fopen("D-small-attempt1.in","r");
    FILE* out=fopen("D-small-attempt1.out","w");
    int T;
    fscanf(in,"%d",&T);
    for(int num=1;num<=T;num++)
    {
        fprintf(out,"Case #%d: ",num);
        int k,c,s;
        fscanf(in,"%d%d%d",&k,&c,&s);
        if(s<k) fprintf(out,"IMPOSSIBLE\n");
        else{
            long long kpow=1;
            for(int i=1;i<=c;i++) kpow*=k;
            for(long long i=1;i<=kpow;i+=kpow/k) fprintf(out,"%I64d ",i);
            fprintf(out,"\n");
        }
    }
    return 0;
}
