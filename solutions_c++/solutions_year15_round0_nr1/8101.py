#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string.h>
using namespace std;
int main()
{
    FILE* input;
    input = fopen("input.txt","r");
    int t,smax;
    fscanf(input,"%d\n",&t);
    for(int i=0; i<t; i++)
    {

        fscanf(input,"%d ",&smax);
        char digits[smax+1];
        int s[smax+1];

        int standing = 0;
        int needed = 0;

        fscanf(input,"%s\n",&digits);
       // scanf("%s",digits);
        for(int j=0,l=strlen(digits); j<l; j++)
        {
             s[j] = ((int) digits[j])-48;

             if(standing>=j)
                standing += s[j];
             else
              {
                 needed += j-standing;
                 standing += j - standing + s[j];
              }

        }

        printf("Case #%d: %d\n",i+1,needed);




    }

    return 0;
}
