#include<stdio.h>
int main()
{
    int t,a,b,arr[6]={1,4,9,121,484,10201},i,m,n,h=1;
    FILE *fp1,*fp2;
    fp1=fopen("C-small.in","r");
    fp2=fopen("output.txt","w");
    fscanf(fp1,"%d\n",&t);
    //scanf("%d",&t);
    while(t--)
    {
         fscanf(fp1,"%d%d\n",&a,&b);
         //scanf("%d%d",&a,&b);
         for(i=0;i<6;i++)
         if(a<=arr[i])
         {m=i;
         break;}
         
         for(i=0;i<6;i++)
         if(b==arr[i])
         {n=i+1;break;}
         else if(b<arr[i])
         {n=i;break;}
         
         fprintf(fp2,"Case #%d: %d\n",h,n-m);
         //printf("%d",n-m);
         h++;
    }
    return 0;
}
