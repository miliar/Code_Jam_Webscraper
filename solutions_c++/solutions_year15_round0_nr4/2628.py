#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int t,x,r,c;
    FILE *fp1=fopen("input.txt","r");
    FILE *fp2=fopen("output.txt","wb"); 
    fscanf(fp1,"%d\n",&t);
    for(int i=1;i<=t;i++)
    {
         fscanf(fp1,"%d %d %d\n",&x,&r,&c);
         if(x==1)
         {
             fprintf(fp2,"Case #%d: GABRIEL\n",i);
         }
         else if(x==2) 
         {
              if((r*c)%x==0)
              fprintf(fp2,"Case #%d: GABRIEL\n",i);
              else
              fprintf(fp2,"Case #%d: RICHARD\n",i);
         }        
         else
         {
              if((r*c)%x==0 && r>=x-1 && c>=x-1)
              fprintf(fp2,"Case #%d: GABRIEL\n",i);
              else
              fprintf(fp2,"Case #%d: RICHARD\n",i);
         }
    }
    fclose(fp1);
    fclose(fp2);
    return 0;
}
