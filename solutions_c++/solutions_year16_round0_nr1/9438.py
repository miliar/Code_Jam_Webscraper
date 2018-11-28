#include<bits/stdc++.h>
using namespace std;
long long int n,i;
int arr[10];
FILE *f1,*f2;
int main()
{
    f1=fopen("A-large.in","r");
    f2=fopen("shivam9.txt","w");

    int t;
    fscanf(f1,"%d",&t);
    int j;
    for(j=1;j<=t;j++)
    {
        for(i=0;i<10;i++)
        {
            arr[i]=0;
        }
       fscanf(f1,"%lld",&n);
       int count1=0;
       if(n==0)
        fprintf(f2,"Case #%d: %s\n",j,"INSOMNIA");
else
{
       i=n;
       int l=1;
       while(count1!=10)
       {
         int k;
          long long int num;
          num=i;
          while(num!=0)
          {
              k=num%10;
              num=num/10;
              if(arr[k]==0)
              {
                  arr[k]=1;
                  count1++;
              }
          }
          if(count1==10)
            break;
          l++;
          i=l*n;
       }

       if(count1==10)
       {
        fprintf(f2,"Case #%d: %lld\n",j,i);

       }
}

    }

return 0;
}
