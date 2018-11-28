#include <stdio.h>

int main()
{
    int T,i,num;
    long long int sum,r,t;
    FILE* iptr;
    FILE* optr;
    iptr = fopen("A-small-attempt0.in","r");
    optr = fopen("out.txt","w");
    fscanf(iptr,"%d",&T);
    for(i = 1; i <= T; i++) {
        sum = 0; num = 0;
        fscanf(iptr,"%I64d%I64d",&r,&t); 
        while( sum < t ) {
            sum = sum + ( (r+1)*(r+1) - r*r );
            if( sum <= t )
                ++num;
            r = r + 2;
        }
        fprintf(optr,"Case #%d: %d\n",i,num);
    }
    fclose(iptr);
    fclose(optr);
}
