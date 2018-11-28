#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int MaxN = 10000;

int T,N,P,R,S;
int n,win[13][MaxN];

inline int Win(int a,int b)
{
    if(a<b)
    {
        if(a==0&&b==2) return 0;
        return b;
    }
    else
    {
        if(b==0&&a==2) return 0;
        return a;   
    }
}

bool Check(int x)
{
    int l = 1 , i = 1;
    while (x%(i+i)==0)
    {
        if(win[l-1][x-i]==win[l-1][x]) return false;
        win[l][x] = Win(win[l-1][x-i],win[l-1][x]);
        l++; i*=2;
    }
    return true;
}

bool DFS(int x)
{
    if(x>n) return true;
    if(P>0)
    {
        win[0][x] = 0; P--;
        if(Check(x) && DFS(x+1)) return true;
        P++;
    }
    if(R>0)
    {
        win[0][x] = 1; R--;
        if(Check(x) && DFS(x+1)) return true;
        R++;
    }
    if(S>0)
    {
        win[0][x] = 2; S--;
        if(Check(x) && DFS(x+1)) return true;
        S++;
    }
    return false;
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    for (int idx=1; idx<=T; idx++)
    {
        printf("Case #%d: ",idx);
        
        scanf("%d%d%d%d",&N,&R,&P,&S);
        n = 1<<N;
        for (int i=1; i<=n; i++) win[0][i] = 0;
        if(DFS(1))
        {
            for (int i=1; i<=n; i++)
                if(win[0][i]==0) printf("P");
                else if(win[0][i]==1) printf("R");
                else printf("S");
            printf("\n");
        }
        else
        {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
