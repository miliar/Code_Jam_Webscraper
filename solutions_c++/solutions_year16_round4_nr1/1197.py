#include <vector>
#include <stdio.h>
#include <iostream>
#include <cmath>
#include <string.h>
#include <set>


using namespace std;

const int N=10;

int R,S,P;
int n;


string ans;

int get(char x,char y)
{
    if(x=='R')
    {
        if(y=='S') return 1;
        return 0;
    }
    else if(x=='S')
    {
        if(y=='P') return 1;
        return 0;
    }
    else
    {
        return y=='R';
    }
}

int check(string s)
{
    string ss;
    ans=s;
    for(int i=0;i<n;i++)
    {
        int m=s.size();
        ss="";
        for(int j=0;j<m;j+=2)
        {
            if(s[j]==s[j+1]) return 0;
            if(get(s[j],s[j+1])) ss+=s[j];
            else ss+=s[j+1];
        }
        s=ss;
    }
    return 1;
}

int dfs(int dep,int P,int R,int S,string str)
{
    if(dep==0) return check(str);
    if(P<0||R<0||S<0) return 0;
    if(P>0&&dfs(dep-1,P-1,R,S,str+"P")) return 1;
    if(R>0&&dfs(dep-1,P,R-1,S,str+"R")) return 1;
    if(S>0&&dfs(dep-1,P,R,S-1,str+"S")) return 1;
    return 0;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("ans","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        scanf("%d%d%d%d",&n,&R,&P,&S);
        if(dfs(1<<n,P,R,S,"")) puts(ans.c_str());
        else puts("IMPOSSIBLE");
    }
}

