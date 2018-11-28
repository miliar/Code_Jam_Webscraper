#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main()
{
     int T,i;
     char s1[100],s2[100];
     FILE *fp1,*fp2;
     fp1 = fopen ("E://input.txt", "r");
     fp2 = fopen ("E://output.txt", "w+");
     fscanf(fp1,"%d",&T);
     for(i=0;i<T;i++)
     {
           int smax,max=0,j,n;
           char arr[1010],aux_arr[1010];
           fscanf(fp1,"%d %s",&smax,&arr);
           for(j=0;arr[j]!='\0';j++)
           {
                aux_arr[j]=(int)(arr[j])-48;
           }
           n=j;           
           for(j=1;j<n;j++)aux_arr[j]=aux_arr[j]+aux_arr[j-1];
           if(smax==0)fprintf(fp2,"Case #%d: %d\n",i+1,0);
           else
           {
                for(j=1;j<n;j++)
                {
                     if(j-aux_arr[j-1] > max)max=j-aux_arr[j-1];
                }
                fprintf(fp2,"Case #%d: %d\n",i+1,max);
           }
     }
     return 0;
}
