#include<stdio.h>
#include<math.h>
//#include<conio.h>
long long int a[10000010];
int ispalin(long long int n)
{
    int a[16],i=0;
    long long int temp=n;
    while(temp>0)
    {
        a[i]=temp%10;
      
        temp/=10;
        i++;
    }
    temp=0;
    long long int ten=1;
    for(int k=i-1;k>=0;k--)
    {
       // printf("%d",a[i]);
    temp+=a[k]*ten;
    ten*=10;
    }
    //printf("%lld ",temp);
    if(temp==n)
    return 1;
    else 
    return 0;
}
long long int binary(long long int n)
{
     long long int front=1,mid,end=10000000;
     mid=(front+end)/2;
     while(front<end)
     {
                     if(n==a[mid]||(n>a[mid-1] && n<a[mid]))
                     return mid;
                     else if(n>a[mid])
                     front=mid+1;
                     else if(n<a[mid])
                     end=mid-1;
                     mid=(front+end)/2;
                     }
                    return 0;
                     }
     
int main()
{
    long long int i,k,flag,t,n1,n2,ans,x1,x2;
     FILE *fp1,*fp2;
    fp1=fopen("C-small-attempt0.in","r");
    fp2=fopen("Goutput.txt","w");
    fscanf(fp1,"%lld",&t);
  for(i=1;i<=10000000;i++)
    {
    a[i]=i*i;
    }
    
  k=1;
    while(t--)
    {
        fscanf(fp1,"%lld%lld",&n1,&n2);
        x1=sqrt(n1);
        x2=sqrt(n2);
       if((double)x1<sqrt(n1))
       x1+=1;
       //printf("%lld",x1);
        ans=0;
        for(i=x1;i<=x2;i++)
        {
            
                          if(ispalin(a[i]) && ispalin(i))
                          {
                          ans++;
                          
                          }
                          }
        fprintf(fp2,"Case #%d: ",k);
        fprintf(fp2,"%lld\n",ans);
       k++; 
    }
    
    //getch();
    return 0;
}
 
