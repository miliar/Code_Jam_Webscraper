#include<stdio.h>
#include<math.h>
//#include<conio.h>
long long int a[10000010],b[100];
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

int main()
{
    long long int i,k,flag,t,n1,n2,ans,x1,x2,pt1,pt2;
     FILE *fp1,*fp2;
    fp1=fopen("C-small-attempt0.in","r");
    fp2=fopen("Goutput.txt","w");
    fscanf(fp1,"%lld",&t);
  for(i=1;i<=10000000;i++)
    {
    a[i]=i*i;
    }
    ans=0;
    for(i=1;i<=10000000;i++)
        {
            
                          if(ispalin(a[i]) && ispalin(i))
                          {
                          b[ans]=a[i];
                          ans++;
                          
                          }
                          }
  k=1;
    while(t--)
    {
        fscanf(fp1,"%lld%lld",&n1,&n2);
    
        for(i=0;i<ans;i++)
        {
    //fprintf(fp2,"%lld ",b[i]);
        if(b[i]>=n1)
        {
        pt1=i;
        break;
        }
        }
        for(i=0;i<ans;i++)
        {
         if(b[i]==n2)
         {
        pt2=i+1;
        break;
        }
        if(b[i]>n2)
        {
        pt2=i;
        break;
        }
        }
        fprintf(fp2,"Case #%d: ",k);
        fprintf(fp2,"%lld\n",pt2-pt1);
       k++; 
    }
    
    //getch();
    return 0;
}
 
