#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int sum[1010];

int main()
{
    FILE *fp1,*fp2;
    int T,i,j,k,n,t,ans;
    fp1=fopen("A-large.in","r");
    fp2=fopen("A-large.out","w");
    fscanf(fp1,"%d",&T);
    for(int lp=1;lp<=T;lp++)
    {
        char str[1010];
        fscanf(fp1,"%d%s",&n,str);
        if(n==0)
        {
            fprintf(fp2,"Case #%d: 0\n",lp);
            continue;
        }
        sum[0]=0;
        for(i=1;i<=n;i++)
            sum[i]=sum[i-1]+str[i-1]-'0';
        ans=0;
        for(i=1;i<=n;i++)
        {
            if(str[i]=='0')continue;
            if(i>(sum[i]+ans))ans+=i-sum[i]-ans;
        }
        fprintf(fp2,"Case #%d: %d\n",lp,ans);
    }
    fclose(fp1);
    fclose(fp2);
}
