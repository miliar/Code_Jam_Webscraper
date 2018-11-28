#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main()
{
    FILE *fin,*fout;
    int t,smax;
    char str[1001]="\0";
    int sum,ans;

    fin = fopen("input.txt","r");
    fout = fopen("output.txt","w");

    fscanf(fin,"%d",&t);
//    printf("%d\n",t);
    for(int i =0;i<t;i++)
    {
        fscanf(fin,"%d %s",&smax,str);
//        printf("%d %s\n",smax,str);
        sum = 0;
        ans = 0;
        for(int j = 0;j<=smax;j++)
        {
            if(sum >= j)
            {
                sum += (int)str[j]-48;
            }
            else
            {
                ans += j - sum;
                sum += j - sum + (int)str[j]-48;
            }
        }
        fprintf(fout,"Case #%d: %d\n",i+1,ans);

    }
    return 0;
}
