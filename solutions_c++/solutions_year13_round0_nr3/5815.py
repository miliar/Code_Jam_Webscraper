#include <stdio.h>
#include <string.h>
#include <math.h>
int checkpld(int a)
{
    int k=1,n,i;
    char s[10];
    sprintf(s,"%d",a);
    n=strlen(s);
    for(i=0;i<(n+1)/2;i++)
       if(s[i]!=s[n-i-1])
       {
          k=0;
          return k;
       } 

   return k;
}
int main()
{
    FILE *fp1,*fp2;
    fp1=fopen("sqpld.in","r");
    fp2=fopen("sqpld.out","w");
    int a,b,aa,bb,c,q,qq;
    fscanf(fp1,"%d",&qq);
    for(q=0;q<qq;q++)
    {
                     
    c=0;
    fscanf(fp1,"%d %d",&a,&b);
    int i,j;
    bb=sqrt(b);
    aa=sqrt(a);
    if(sqrt(a)*sqrt(a)!=a)
       aa++;
    //printf("=%d %d=\n",aa,bb);
    for(i=aa;i<=bb;i++)
    {
       if(checkpld(i)==1)
       if(checkpld(i*i)==1)
       {
          //printf("###%d\n",i*i);
          c++;
       }
    }
    fprintf(fp2,"Case #%d: %d\n",q+1,c);
    
    }
    fclose(fp1);
    fclose(fp2);
    scanf(" ");
    return 0;   
}
