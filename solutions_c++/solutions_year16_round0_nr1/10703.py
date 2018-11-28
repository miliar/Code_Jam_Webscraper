#include<stdio.h>
int main()
{
    int i,j,l=0,n;
    long int p,z;
    int testcase;
    long int value [100],value2[10];
    scanf("%d",&testcase);
    for( i=0;i<testcase;i++)
    {
        scanf("%li",&value[i]);
    }
    for(i=0;i<testcase;i++)
    {
        l=0;
        
        for(j=1;j>0;j++)
        {
        
          p=(value[i])*j;
          z=p;
          
         
          if(p==0)
          {
              printf("Case #%d: INSOMNIA\n",i+1);
              break;
          }
              
             while(p!=0)
             { 
                 n=p%10;
                
                if(l==0)
                {
                    value2[l]=n;
                    l++;
                }
                if(l>0)
                {
                    int s=0;
                    int flag=0;
                    while(s<=(l-1))
                    {
                        if(value2[s]==n)
                        {
                            flag=1;
                            break;
                        }
                        s++;
                    }
                    if(flag==0)
                    {
                        
                        value2[l]=n;
                        l=l+1;
                    }
                }
                p=p/10;
             }
             
             p=z;
             int flag2=0;
             for(int m=0;m<l;m++)
             {
                 for(int t=0;t<=9;t++)
                 {
                     if(value2[m]==t)
                     {
                       flag2++;
                       break;
                     }
                     
                 }
             }
             
             
             if(flag2==10)
             {
                 printf("Case #%d: %d\n",i+1,z);
                 break;
             }
             
             
          
        }
        for(int m=0;m<=9;m++)
             {value2[m]=NULL;}
    }
    
    
}

