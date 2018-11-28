#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;

void Solve(int t)
{
    int n;
    int ampus = 0;
    int depus = 0;
    char e[1002];
    scanf("%d %s",&n,e);
    for(int i = 0 ; i <= n; i++)
    {
        if(ampus >= i)
        {
            ampus = ampus + (e[i] - '0');
        }
        else
        {
            depus = depus + (i - ampus);
            ampus = i + (e[i] - '0');
        }
    }
   // printf("%d\n",ampus);
    printf("Case #%d: %d\n",t,depus);

}
int main()
{

    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin>>t;
    for(int i = 1; i <= t; i++)
    {
        Solve(i);
    }

}
