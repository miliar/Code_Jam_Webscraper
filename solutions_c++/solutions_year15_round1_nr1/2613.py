/*Code jam 15 q3*/
#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<fstream>
using namespace std;
int mul(int,int);
int table[4][4];
int main()
{
    int loop,term,a[10000],random=0,rateeat=0;
    FILE *out;
    FILE *in;
    int t;
    in=freopen("A-large.in","r",stdin);
    out=freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(loop=0;loop<t;loop++)
    {
        random=0;
        rateeat=0;
        scanf("%d",&term);
        for(register int k=0;k<term;k++)
            scanf("%d ",&a[k]);
        for(register int i=0;i<term-1;i++)
            if(a[i]>a[i+1])
            {
                random+=(a[i]-a[i+1]);
            }

        int rate=0;
        int bigdiff=0;
        for(register int i=0;i<term-1;i++)
        {
            if(a[i]-a[i+1]>bigdiff)
                bigdiff=a[i]-a[i+1];
        }
        rate=bigdiff;
        for(register int i=0;i<term-1;i++)
        {
            if(a[i]>=bigdiff)
                rateeat+=bigdiff;
            else
                rateeat+=a[i];
        }

        printf("Case #%d: %d %d\n",loop+1,random,rateeat);
    }
    return 0;
}
