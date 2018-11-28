
#include<iostream>
#include<stdio.h>

using namespace std;


int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);

    int t,shyMax,extra,standingCount,kase,i;
    char shy[1001];
    kase=1;
    
    scanf("%d",&t);
    
    while(t--)
    {
        scanf("%d",&shyMax);
        scanf("%s",shy);
        extra=0;
        standingCount=0;
        
        
        for(i=0;i<=shyMax;i++)
        {
            if(standingCount>=i)
            {
                standingCount+=shy[i]-48;
            }
            else
            {
                
                if((shy[i]-48)>0)
                {
                    extra+=(i-standingCount);
                    standingCount=i+(shy[i]-48);
                }
            }
        }
        
        printf("Case #%d: %d\n",kase++,extra);
        
        
        
    }
    
    return 0;
}