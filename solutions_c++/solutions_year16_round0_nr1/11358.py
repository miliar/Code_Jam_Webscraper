#include<stdio.h>
#include<string.h>
int main()
{
    int t,a,n,r,i,l,k,f1,f2,f3,f4,f5,f6,f7,f8,f9,f0,temp;
    l=0;
    start:
          scanf("%d",&t);
    
    scanf("%d",&a);l++;
    f1=0,f2=0,f3=0,f3=0,f4=0,f5=0,f6=0,f7=0,f8=0,f9=0,f0=0;
    printf("\nCase #%d: ",l);
    
    
    for(i=1;i<100;i++)
    {                     
                    n=a*i;
                    temp=n;
                    while(n>0)
                    {                 r=n%10;                         
                                            if(r==0)
                                            f1=1;
                                            else if(r==1)
                                            f2=1;
                                            else if(r==2)
                                            f3=1;
                                             else if(r==3)
                                            f4=1;
                                             else if(r==4)
                                            f5=1;
                                             else if(r==5)
                                            f6=1;
                                             else if(r==6)
                                            f7=1;
                                             else if(r==7)
                                            f8=1;
                                             else if(r==8)
                                            f9=1;
                                             else if(r==9)
                                            f0=1;
                                             if(f1==1&&f2==1&&f2==1&&f3==1&&f4==1&&f5==1&&f6==1&&f7==1&&f8==1&&f9==1&&f0==1)
                                             {
                                             printf("%d ",temp);goto start;
                                             }
                                             
                                             n=n/10;
                    }
                   
                    
    }
    if(f1==0||f2==0||f2==0||f3==0||f4==0||f5==0||f6==0||f7==0||f8==0||f9==0||f0==0)
    printf("INSOMNIA");goto start;
}
    
   
                                                                                   
                                            
