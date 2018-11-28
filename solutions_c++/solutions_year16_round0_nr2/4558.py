#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
using namespace std;

const int MAXN=105;
const int MAXNUM=-1;

int main()
{
    FILE* fin=fopen("b.in","r");
    FILE* fout=fopen("b.out","w");
    int t=0,tt=1;
    int len = 0, ans = 0;
    char s[MAXN];
    //int dp[MAXN][MAXN];
    char ts[MAXN];

    fscanf(fin,"%d",&t);
    //fscanf(fin,"%s",s);

    while (t--)
    {
        fscanf(fin,"%s",s);

        len = strlen(s);

        int i=0;

        ans=0;

        for (i=0;i<len-1;i++)
            if (s[i]!=s[i+1]) ans++;

        if (s[len-1]=='-') ans++;

        /*int i=0,j=0,k=0,l=0;

        for (i=0; i<len; i++)
            dp[i][i]=(s[i]=='+'?0:1);

        for (l=1;i<len;l++)
        {
            for (i=0;i<len-1;l++)
            {
                j=i+l;
                dp[i][j]=MAXNUM;

                if (s[i+1]==s[i]) dp[i][j]=max(dp[i][j],dp[i+1][j]);
                if (s[j-1]==s[j]) dp[i][j]=max(dp[i][j],dp[i][j-1]);
                if (s[i+1]!=s[i]) dp[i][j]=max(dp[i][j],dp[i+1][j]+1);
                if (s[j-1]!=s[j]) dp[i][j]=max(dp[i][j],dp[i][j-1]+1);
            }
        }
        fprintf(fout,"Case #%d: %d\n",tt++,dp[0][len-1]);*/

        //int neg=0;
        //int i=0;
/*
        memset(ts,0,sizeof(ts));

        for (i=0;i<len;i++)
        {
            if (s[i]=='-') neg++;
            else neg--;
        }

        if (neg>0)
        {
           for (i=0;i<len;i++)
            {
                printf("OH%d ",len-i-1);
                if (s[i]=='-') ts[len-1-i]='+';
                else ts[len-1-i]='-';
            }
            memcpy(s,ts,len);
            ans=1;
        }
        else ans=0;

       //for (i=0;i<len;i++)
       //     s[i]=ts[i];

printf("%d %d %s %s %d\n",tt,len,s,ts, ans);
        neg=len-1;

        while (neg != -1)
        {
            if (s[neg]=='+')
            {
                neg--;
                continue;
            }

            for (i=0;i<=neg;i++)
            {
                if (s[i]=='-') ts[neg-i]='+';
                else ts[neg-i]='-';
            }
            memcpy(s,ts,neg+1);
printf("%d %s\n",tt,s);
            neg--;
            ans++;
        }*/

        fprintf(fout,"Case #%d: %d\n",tt++,ans);
    }

    return 0;
}
