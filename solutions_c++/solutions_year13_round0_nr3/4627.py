#include<stdio.h>
#include<conio.h>
#include<math.h>


int is_palin(int n)
{

    int num=n,i,k,r1,r2;
    for(i=10;num!=0;i=i*10)
    num=num/10;
    
    i=i/10;
    
    k=i/10;
    while(n!=0&&k!=0)
    {
               r1=n/k;
               r2=n%10;
               n=n%k;
               n=n/10;
               if(r1!=r2)
               return 0;
               
               k=k/100;
               
               }
               
    return 1;
}
               
               
int main()
{
    int t,k=1, a, b, c, count;
    FILE *file, *out;
    file=fopen("inputSB.txt", "r");
    out=fopen("outputSB.txt", "w");
    fscanf(file,"%d", &t);
    while(k<=t)
    {
               count=0;
               fscanf(file,"%d%d",&a,&b);
               c=(int)sqrt(a);
               if(c*c<a)
               c++;
               printf("%d\t",c);
               while(c*c<=b)
               {
                            if(is_palin(c*c))
                            {
                                             printf("yes");
                                             if(is_palin(c))
                                             count++;
                            }
                            c++;
               }
               
               fprintf(out,"Case #%d: %d\n",k,count);
               
               k++;
    }
    
    fclose(file);
    fclose(out);
   
    printf("done");
    
    
    getch();
    return 0;
}
