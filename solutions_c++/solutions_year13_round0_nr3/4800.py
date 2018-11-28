#include<conio.h>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

unsigned long long is_square(unsigned long long n)
{
    unsigned long long i=0;
    for(i=1;i<=n;i++)
    {
        if((i*i)==n)
            return i;
    }

    return 0;
}

int is_palindrome(   unsigned long long n)
{
    char *s=(char *)malloc(sizeof(char)*100000000000);


    sprintf(s, "%llu", n);

    for(int i=0;i<strlen(s)/2;i++)
    {
        if(s[i]!=s[strlen(s)-i-1])
        {
            delete(s);
            return -1;

        }


    }
    delete(s);
    return 1;
}

int main(int argc, char *argv[])
{


FILE* fichier1 = NULL;
fichier1 = fopen("C-small-attempt0.in", "r+");

FILE* fichier2 = NULL;
fichier2 = fopen("C-small-attempt0.out", "w+");

int test=0;
unsigned long long m=0;
unsigned long long n=0;
unsigned long long d=0;
unsigned long long  c=0;
unsigned long long i=0;
unsigned long long j=0 ;
int r;





       fscanf(fichier1,"%d",&test);


       fgetc(fichier1);




for( r=0;r<test;r++)
       {
         c=0;
       fscanf(fichier1,"%llu",&m);

       fgetc(fichier1);

       fscanf(fichier1,"%llu",&n);


        fgetc(fichier1);



        for(i=m;i<=n;i++)
        {


                    if(is_square(i)!=0 && is_palindrome(i)==1 )
                    {

                        if(is_palindrome(is_square(i))==1 )
                            {
                                c++;
                            }
                    }





        }



        fprintf(fichier2,"Case #%d: %d\n",r+1,c);






         }


return 0;
}
