#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t,len,kl,temp,sv;
    char s[2010],ans[2010];
    int has[30];

    scanf("%d",&t);
    sv=t;

    while(t--)
    {
        scanf("%s",s);
        len=strlen(s);
        memset(has,0,sizeof(has));
        kl=0;

        for(int i=0;i<len;i++)
        {
            has[s[i]-'A']++;
        }

        temp=has[25];
        if(temp!=0)
        {
            for(int i=0;i<temp;i++,kl++)
            ans[kl]='0';
            has[25]-=temp;
            has[4]-=temp;
            has[17]-=temp;
            has[14]-=temp;
        }

        temp=has[6];
        if(temp!=0)
        {
            for(int i=0;i<temp;i++,kl++)
            ans[kl]='8';
            has[6]=0;
            has[4]-=temp;
            has[8]-=temp;
            has[7]-=temp;
            has[19]-=temp;
        }

        temp=has[22];
        if(temp!=0)
        {
            for(int i=0;i<temp;i++,kl++)
            ans[kl]='2';
            has[22]=0;
            has[19]-=temp;
            has[14]-=temp;
        }

        temp=has[23];
        if(temp!=0)
        {
            for(int i=0;i<temp;i++,kl++)
            ans[kl]='6';
            has[23]=0;
            has[18]-=temp;
            has[8]-=temp;
        }

        temp=has[18];
        if(temp!=0)
        {
            for(int i=0;i<temp;i++,kl++)
            ans[kl]='7';
            has[18]=0;
            has[4]-=(2*temp);
            has[21]-=temp;
            has[13]-=temp;
        }

        temp=has[21];
        if(temp!=0)
        {
            for(int i=0;i<temp;i++,kl++)
            ans[kl]='5';
            has[21]=0;
            has[5]-=temp;
            has[8]-=temp;
            has[4]-=temp;
        }

        temp=has[5];
        if(temp!=0)
        {
            for(int i=0;i<temp;i++,kl++)
            ans[kl]='4';
            has[5]=0;
            has[14]-=temp;
            has[20]-=temp;
            has[17]-=temp;
        }

        temp=has[17];
        if(temp!=0)
        {
            for(int i=0;i<temp;i++,kl++)
            ans[kl]='3';
            has[17]=0;
            has[19]-=temp;
            has[7]-=temp;
            has[4]-=(2*temp);
        }

        temp=has[14];
        if(temp!=0)
        {
            for(int i=0;i<temp;i++,kl++)
            ans[kl]='1';
            has[14]=0;
            has[13]-=temp;
            has[4]-=temp;
        }

        temp=has[8];
        if(temp!=0)
        {
            for(int i=0;i<temp;i++,kl++)
            ans[kl]='9';
            has[8]=0;
            has[4]-=temp;
            has[13]-=(2*temp);
        }

        ans[kl]='\0';

        sort(ans,ans+kl);

        printf("Case #%d: %s\n",sv-t,ans);
    }

    return 0;
}
