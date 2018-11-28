#include<stdio.h>

int libn;
long long int* lib;

int n,t;

int main()
{
    FILE* belib=fopen("lib.txt","r");
    fscanf(belib,"%d",&libn);
    lib=new long long int[libn];
    for(int i=0; i<libn;i++)
    {
        fscanf(belib,"%lld",&lib[i]);
    }

   /* for(int i=0; i<libn;i++)
    {
        printf("%lld\n",lib[i]);
    }*/

    FILE* be=fopen("C-small-attempt0.in","r");
    FILE* ki=fopen("out.txt","w");

    fscanf(be,"%d",&t);
    //printf("t: %d\n",t);
    for(int c=0; c<t; c++)
    {
        long long int startn,endn;
        fscanf(be,"%lld %lld",&startn, &endn);
      //  printf("%lld %lld\n",startn,endn);

        int answ=0;
        for(int i=0; i<libn;i++)
        {
            if ((lib[i]>=startn) && (lib[i]<=endn))
               answ++;

        }
        fprintf(ki,"Case #%d: %d\n",c+1,answ);
    }


    fclose(be);
    fclose(ki);
    return 0;
}


/* creating lib.txt
#include<stdio.h>

long long int* lib;

//const long long int maxn=1000;
//const long long int maxi=32;

const long long int maxn=100000000000000;
const long long int maxi=10000000;

int pal=0;
int Palindrome(int num)
{
    if(num>0)
    {
        pal=(pal*10)+ (num %10);
        Palindrome(num / 10); //recursion.
    }
    return pal;
}
int main()
{
    FILE* ki=fopen("lib.txt","w");
    lib=new long long int[50];
    int libn=0;
    for (long long int i=0; i<maxi; i++)
    {

        pal=0;
        if(i==Palindrome(i))
        {
            long long int num=i*i;
            pal=0;
            if(num==Palindrome(num))
            {
                lib[libn]=num;
                libn++;
            }
        }
    }

    fprintf(ki,"%d\n",libn);
    for(int i=0; i<libn;i++)
    {
        fprintf(ki,"%lld\n",lib[i]);
    }

    fclose(ki);
    return 0;
}

*/
