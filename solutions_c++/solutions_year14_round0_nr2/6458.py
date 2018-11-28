/*Cookie Clicker Alpha
    By Sonali Saxena
*/


#include <stdio.h>
#include<iostream>
#include<math.h>
int main()
{
FILE *file_read,*file_write;
   double c,f,x,temp=2.00000;
file_read = fopen("input.in", "r");
   file_write = fopen("output.in", "w");
int t;
   fscanf(file_read ,"%d",&t);
   int n=t;
        while(!feof(file_read)&& t--)
        {double sum= 0.00;temp=2.00000;fscanf(file_read ,"%lf %lf %lf",&c,&f,&x);while((x/(temp))>(c/temp + x/(f+temp))){sum+=c/temp;temp+=f;}
            sum+=x/(temp);fprintf(file_write,"Case #%d: %0.7lf\n",n-t,sum);}
   fclose(file_read);
   fclose(file_write);
   return 0;
}

