#include<stdio.h>
FILE *fin=fopen("input.txt","r");
FILE *fout=fopen("output.txt","w");
int main()
{
    long long i, j, k, n, chk=0, T;
    fscanf(fin, "%lld", &T);
    for(j=1; j<=T; ++j)
    {
        fscanf(fin, "%lld", &n);
        if(n==0){ fprintf(fout, "Case #%lld: INSOMNIA\n", j); continue; }
        i=0; chk=0;
        while(chk!=1023)
        {
            ++i;
            k=i*n;
            while(k)
            {
                chk = chk|(1<<(k%10));
                k/=10;
            }
        }
        fprintf(fout, "Case #%lld: %lld\n", j, i*n);
    }
    return 0;
}
