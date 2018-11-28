#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    long long int a[101],i,j,n,t,l,k,ans,count,size,in;
     FILE *fp1,*fp2;
    fp1=fopen("A-small-attempt3.in","r");
    fp2=fopen("Goutput.txt","w");
    fscanf(fp1,"%lld",&t);
    l=1;
    while(t--)
    {
        fscanf(fp1,"%lld%lld",&in,&n);
        for(i=0;i<n;i++)
        fscanf(fp1,"%lld",&a[i]);
        sort(a,a+n);
        size=in;
        i=0;
        count=0;
        int flag=1,flag1=1;
        
         if(size==1)
        {
             fprintf(fp2,"Case #%lld: %lld\n",l,n);
        l++;
        continue;
        }
        while(flag==1)
        {
          while(a[i]<size && i<n)
          {
              size+=a[i];
              i++;
          }
          if(a[i]>=size && i<n)
          {
              int count1=0;
              int size1=size;
              
              while(a[i]>=size1)
              {
                  size1+=size1-1;
                  count1++;
              }
              if(count1>=n-i)
              {
                  count+=n-i;
                  flag=0;
              }
              else
              {
              size=size1;
              count+=count1;
              size+=a[i];
              }
              i++;
          }
          if(i>n-1)
          flag=0;
        }
        fprintf(fp2,"Case #%lld: %lld\n",l,count);
        l++;
    }
}
