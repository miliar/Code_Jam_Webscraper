#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
using namespace std;

string ans[13][3];
char val[3]={'R','P','S'};

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    ans[0][0]="P";
    ans[0][1]="R";
    ans[0][2]="S";
    for (int i=1;i<=12;++i)
        for (int j=0;j<=2;++j)
        {
            int k1=j,k2=(j+1)%3;
            if (ans[i-1][k1]>ans[i-1][k2]) swap(k1,k2);
            ans[i][j]=ans[i-1][k1]+ans[i-1][k2];
        }
    int t,n,r,p,s;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        scanf("%d%d%d%d",&n,&r,&p,&s);
        string ANS="ZZ";
        for (int i=0;i<3;++i)
        {
            int rr=0,pp=0,ss=0;
            for (int j=0;j<ans[n][i].length();++j)
                if (ans[n][i][j]=='R')
                    ++rr;
                else if (ans[n][i][j]=='P')
                    ++pp;
                else ++ss;
            if (rr==r&&pp==p&&ss==s)
                ANS=min(ANS,ans[n][i]);
        }
        printf("Case #%d: ",cas);
        if (ANS=="ZZ") puts("IMPOSSIBLE");
        else cout<<ANS<<endl;
    }
    return 0;
}
