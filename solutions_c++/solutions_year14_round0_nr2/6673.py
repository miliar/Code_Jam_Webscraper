#include<stdio.h>
int main()
{
    int t;
    double c,f,x,cur,s,coins;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
           scanf("%lf%lf%lf",&c,&f,&x); 
            
            
    
 
    cur=(float)x/2;
    coins=2,s=0;
    while(1)
    {
            s+=(double)c/coins;
            coins+=f;
            s+=x/coins;
           
            if(cur>=s)
            {
            cur=s;
            s-=(double)x/coins;
            }
            else
            {
            printf("Case #%d: %.7lf\n",i,cur); 
            break;       
            }
            
    }
    
}
    
    return 0;
    
}
