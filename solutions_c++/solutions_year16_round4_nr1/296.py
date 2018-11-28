#include<bits/stdc++.h>
using namespace std;

string ch[]={"R","P","S"};
string f[3][20];
int a[3];

string dp(int x,int d)
{
    if(d==0)return ch[x];
    if(f[x][d]!="")return f[x][d];
    string s1=dp(x,d-1),s2=dp((x+2)%3,d-1);
    return f[x][d]=min(s1+s2,s2+s1);
}

int check(string&s)
{
    int c0=0,c1=0,c2=0;
    for(auto it:s)
    {
        c0+=it=='R';
        c1+=it=='P';
        c2+=it=='S';
    }
    return c0==a[0]&&c1==a[1]&&c2==a[2];
}

int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    int T;
    scanf("%d",&T);
    //R P S
    int n;
    for(int tcnt=1;tcnt<=T;tcnt++)
    {
        scanf("%d%d%d%d",&n,a,a+1,a+2);
        printf("Case #%d: ",tcnt);
        int fg=0;
        for(int i=0;i<3;i++)for(int j=0;j<=n;j++)f[i][j]="";
        for(int i=0;i<3;i++)
            dp(i,n);
        vector<string>ansl;
        for(int i=0;i<3;i++)
        {
            if(check(f[i][n]))
                ansl.push_back(f[i][n]);
        }
        sort(ansl.begin(),ansl.end());
        if(ansl.size()==0)
            puts("IMPOSSIBLE");
        else
            printf("%s\n",ansl[0].c_str());
    }
    return 0;
}
