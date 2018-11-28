//#include<cs50.h>
#include<iostream>
#include<stdio.h>
#include<string>
#include<math.h>

using namespace std;

int main()
{
    int t;
    scanf("%i",&t);
    for(int j=1;j<=t;j++)
    {
        int k;
        scanf("%i",&k);
        char s[k+2];
        scanf("%s",s);
        int i;
        int ideal=0,now=s[0]-48,ans=0,diff=0;
        for(int i=1;i<k+1;i++)
        {
            ideal=i;
            //printf("ideal = %i\n",ideal);
            //printf("now = %i\n",now);
            if(now<ideal)
            {
                diff=ideal-now;
                now=now+diff;
                ans=ans+diff; 
            }
            now=now+s[i]-48;
            
        }
        printf("case #%i: %i\n",j,ans);

        
    }
}
