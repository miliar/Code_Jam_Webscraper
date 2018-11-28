#include <iostream>
#include <stdio.h>
#define maxs 1000
using namespace std;
int t,smax;
int s[maxs+5];
int main()
{
    /*FILE *in=fopen("A-small-attempt2.in","r");
    FILE *out=fopen("A-small-attempt0.out","w");*/
    int iCase=0;
    //fscanf(in,"%d",&t);
    scanf("%d",&t);
    while(t--)
    {
        //fscanf(in,"%d ",&smax);
        scanf("%d ",&smax);
        int i=0;
        char chr;
        while(i<=smax)
        {
            //fscanf(in,"%c",&chr);
            scanf("%c",&chr);
            s[i]=chr-48;
            i++;
        }
        int sum=s[0],ans=0;
        for (i=1;i<=smax;i++)
        if (i<=sum)
        {
            sum+=s[i];
        }else
        {
            ans+=i-sum;
            sum+=s[i]+i-sum;
        }
        //fprintf(out,"Case #%d: %d\n",++iCase,ans);
        printf("Case #%d: %d\n",++iCase,ans);
    }
    return 0;
}
