#include <cstdio>
using namespace std;

void solve(int t)
{
    int x,r,c;
    scanf("%d %d %d",&x,&r,&c);
    int sol;
    if (x==1)
        sol = 1;
    if (x==2)
        sol = (r*c%2==0);
    if (x==3)
        sol = (r*c%3==0 && r*c>3);
    if (x==4)
        sol = (r*c==12) || (r*c==16);
    printf("Case #%d: %s\n",t,sol ? "GABRIEL" : "RICHARD");
}

int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1; i <= t; i++)
        solve(i);
    return 0;
}
