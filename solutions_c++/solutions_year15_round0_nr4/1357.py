#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#define prt(k) cout<<#k" = "<<k<<endl;
using namespace std;
typedef long long ll;
int X, R, C;
char yes[45] = "GABRIEL";
char no[45] = "RICHARD";
/// R <= C
char* solve3()
{
    if (R==1)
    {
        if (C==3)
            return no;
        else
            return no;
    }
    if (R==2)
    {
        if (C==3)
            return yes;
        if (C==4)
            return no;
        return no;
    }
    if (R==3)
    {
        if (C==3)
            return yes;
        if (C==4)
            return yes;
    }
    if (R==4)
    {
        if (C==4)
            return no;
    }
}
/// R <= C
char *solve4()
{
    if (R > C) swap(R, C);
    if (R*C % 4)
        return no;
    if (R==1)
        return no;
    if (R==2)
    {
        if (C==2) return no;
        if (C==3) return no;
        if (C==4) return no;
    }
    if (R==3)
    {
        if (C==3) return no;
        if (C==4) return yes;
    }
    if (R==4)
        if (C==4) return yes;
}
int main()
{
    freopen("D.in","r",stdin); freopen("D.out","w",stdout);
    int re; int ca=1; cin>>re;
    while (re--)
    {
        cin>>X>>R>>C;
        printf("Case #%d: ", ca++);
        if (X==1)
        {
            puts(yes);
            continue;
        }
        if (R*C % X != 0)
        {
            puts(no);
            continue;
        }
        if (X==2)
        {
            puts(yes);
            continue;
        }
        if (R > C) swap(R, C); /// R <= C
        if (X==3) puts(solve3());
        else puts(solve4());
    }
}
