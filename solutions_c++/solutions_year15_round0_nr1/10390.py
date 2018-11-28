#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

int main()
{
    int test=0,x=1;
    scanf("%d",&test);
    while(test--)
    {
        int n=0;
        scanf("%d",&n);
        char s[n+1];
        scanf("%s",&s);

            int stnd=(s[0]-'0');
            int sum=0;
        for(int i=1;i<n+1;i++)
       {  if((s[i]-'0')>0)
       {
           if(stnd>=i)
           {
               stnd=stnd+(s[i]-'0');
           }
           else
           {
               sum=sum+(i-stnd);
               stnd=(i-stnd)+stnd+(s[i]-'0');
           }
       }

       }
       printf("Case #%d: %d\n",x,sum);
       x+=1;
    }

    return 0;
}
