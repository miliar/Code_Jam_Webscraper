#include<iostream>
#include<stdio.h>
int main()
{
    int test;
    char input[1002];
    int sMax;
    scanf("%d",&test);
    int running,res;
    int j=1;
    while(test--)
    {
        running=0;
        res=0;
        scanf("%d",&sMax);
        scanf("%s",input);
        for(int i=0;i<=sMax;i++)
        {
            if(running<i)
            {
                res+=(i-running);
                running+=(i-running)+input[i]-48;
            }
            else
            {
                running+=(input[i]-48);
            }
        }
        printf("Case #%d: %d\n",j++,res);
    }

}
