#include<bits/stdc++.h>
using namespace std;
int buck[30],ans[10];
char in[2005];
int main()
{
    //freopen("A small input.in","r",stdin);
    //freopen("A small output.out","w",stdout);
    freopen("A large input.in","r",stdin);
    freopen("A large output.out","w",stdout);
    int t,ti,m,n,i,j,k;
    scanf("%d",&t);
    for(ti=1;ti<=t;ti++)
    {
        printf("Case #%d: ",ti);
        for(i=0;i<10;i++)
            ans[i]=0;
        for(i=0;i<30;i++)
            buck[i]=0;
        for(i=0;i<=2000;i++)
            in[i]=0;
        scanf("%s",in);
        for(i=0;in[i];i++)
            buck[in[i]-'A']++;
        ans[0]+=buck['Z'-'A'];
        buck['Z'-'A']-=ans[0];
        buck['E'-'A']-=ans[0];
        buck['R'-'A']-=ans[0];
        buck['O'-'A']-=ans[0];
        ans[2]+=buck['W'-'A'];
        buck['T'-'A']-=ans[2];
        buck['W'-'A']-=ans[2];
        buck['O'-'A']-=ans[2];
        ans[4]+=buck['U'-'A'];
        buck['F'-'A']-=ans[4];
        buck['O'-'A']-=ans[4];
        buck['U'-'A']-=ans[4];
        buck['R'-'A']-=ans[4];
        ans[1]+=buck['O'-'A'];
        buck['O'-'A']-=ans[1];
        buck['N'-'A']-=ans[1];
        buck['E'-'A']-=ans[1];
        ans[5]+=buck['F'-'A'];
        buck['F'-'A']-=ans[5];
        buck['I'-'A']-=ans[5];
        buck['V'-'A']-=ans[5];
        buck['E'-'A']-=ans[5];
        ans[7]+=buck['V'-'A'];
        buck['S'-'A']-=ans[7];
        buck['E'-'A']-=ans[7];
        buck['V'-'A']-=ans[7];
        buck['E'-'A']-=ans[7];
        buck['N'-'A']-=ans[7];
        ans[6]+=buck['X'-'A'];
        buck['S'-'A']-=ans[6];
        buck['I'-'A']-=ans[6];
        buck['X'-'A']-=ans[6];
        ans[8]+=buck['G'-'A'];
        buck['E'-'A']-=ans[8];
        buck['I'-'A']-=ans[8];
        buck['G'-'A']-=ans[8];
        buck['H'-'A']-=ans[8];
        buck['T'-'A']-=ans[8];
        ans[3]+=buck['H'-'A'];
        buck['T'-'A']-=ans[3];
        buck['H'-'A']-=ans[3];
        buck['R'-'A']-=ans[3];
        buck['E'-'A']-=ans[3];
        buck['E'-'A']-=ans[3];
        ans[9]+=buck['N'-'A']/2;
        buck['N'-'A']-=ans[9];
        buck['I'-'A']-=ans[9];
        buck['N'-'A']-=ans[9];
        buck['E'-'A']-=ans[9];
        for(i=0;i<10;i++)
            for(j=0;j<ans[i];j++)
                printf("%d",i);
        printf("\n");
    }
}
