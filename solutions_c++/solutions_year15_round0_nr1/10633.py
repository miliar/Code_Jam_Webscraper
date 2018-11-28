#include<iostream>
#include<stdio.h>
int main()
{
    //freopen ("A-small-attempt2.in","r",stdin);
    //freopen ("output.out","w",stdout);
    int T;
    char input[1002];
    int Smax;
    scanf("%d",&T);
    int running,res;
    int j=1;
    while(T--)
    {
        running=0;
        res=0;
        scanf("%d",&Smax);
        scanf("%s",input);
        for(int i=0;i<=Smax;i++)
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
