#include<stdio.h>
#include<math.h>
int pali(int);
int caset=0,t=0,s,i,count=0,a=0,temp=0,b=0,r=0;
int main()
{
    
    scanf("%d",&t);
     while(t--)
     {  caset++;
        count=0;
        temp=0;
        s=0;
        r=0;
         scanf("%d%d",&a,&b);
         for(i=a;i<=b;i++)
         {  s=sqrt(i);
             if(s*s==i)
             {
                if(pali(i))
                { if(pali(s))
                  {    
                        count++;
                        //printf("i:%d\n",i);
                   }     
                }
             }
            
         }
          printf("Case #%d: %d\n",caset,count);
     }
return 0;
}
int pali(int i)
{   r=0;
    temp=i;
    while(temp!=0)
    {
        r = r*10;
        r = r+temp%10;
        temp=temp/10;
    }
    if(r==i)
        return 1;
    else
        return 0;
}