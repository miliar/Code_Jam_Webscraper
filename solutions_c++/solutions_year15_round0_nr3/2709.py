#include<bits/stdc++.h>

using namespace std;

char mul[4][4]={{'1','i','j','k'},{'i','1','k','j'},
                {'j','k','1','i'},{'k','j','i','1'}};

int sign[4][4]={{0,0,0,0},{0,1,0,1},{0,1,1,0},{0,0,1,1}};
bool dp[10010][3],v[10010][3];
char str[10010],need[]={'i','j','k'};

bool pos(char c, int sgn, int i, int l, int nd)
{
    if(i==l)
    {
        if(nd==3 && c=='1' && sgn==0)
            return true;
        else
            return false;
    }

    if(v[i][nd])
        return dp[i][nd];

    v[i][nd]=true;

    int idx1,idx2;
    if(c=='1')
        idx1=0;
    else
        idx1=c-'i'+1;

    if(str[i]=='1')
        idx2=0;
    else
        idx2=str[i]-'i'+1;

    char nxt=mul[idx1][idx2];
    int nsgn=(sgn)^(sign[idx1][idx2]);

    if(nxt==need[nd] && nsgn==0)
        dp[i][nd]=pos(nxt,nsgn,i+1,l,nd)|pos('1',0,i+1,l,nd+1);
    else
        dp[i][nd]=pos(nxt,nsgn,i+1,l,nd);
    return dp[i][nd];
}


int main()
{
    freopen("C.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t,l,x,i,j,k,fl;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d %d",&l,&x);
        scanf(" %s",str);
        for(i=0;i<=l*x;i++)
            for(j=0;j<3;j++)
            {
                v[i][j]=false;
            }
        j=l;
        fl=l*x;
        while(x!=1)
        {
            x--;
            for(i=0;i<l;i++)
                str[j++]=str[i];
        }
        if(pos('1',0,0,fl,0))
            printf("Case #%d: YES\n",k);
        else
            printf("Case #%d: NO\n",k);
    }
    return 0;
}
