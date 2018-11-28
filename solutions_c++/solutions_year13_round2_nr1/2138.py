#include<iostream>
#include<stdlib.h>
#define INF 150
using namespace std;

int compare(const void *a,const void *b)
{
        return (*(int *)(a))-(*(int *)(b));    
}

int getval(int a,int reqd)
{
        if(a==1)  return INF;
        int i=0;
        while(a<=reqd)
        {
              a+=(a-1);              
              i++;
        }
        return i;
}

int main()
{
     int t;
     scanf("%d",&t);
     int i=1,a,n,motes[150],j,count=0,firstop=101;
     for(i=1;i<=t;i++)
     {
              firstop=101;        
              count=0;        
              scanf("%d%d",&a,&n);  
              for(j=0;j<n;j++)
                        scanf("%d",&motes[j]);
              qsort(motes,n,sizeof(int),compare); 
              for(j=0;j<n;j++)  
              {
                     if(a>motes[j])
                              a+=motes[j];
                     else
                     {
                             int val=getval(a,motes[j]);
                             if(val<(n-j))
                             {
                                     if(firstop==101)
                                                 firstop=n-j;     
                                     for(int k=val;k>=1;k--)                          
                                     {
                                             a+=(a-1);       
                                     }
                                     a+=motes[j];
                                     count+=val;
                             }     
                             else
                             {
                                    count+=n-j;
                                    break;
                             }
                     }                           
              }
              if(firstop<count)  count=firstop;
              printf("Case #%d: %d\n",i,count);
     }    
}
