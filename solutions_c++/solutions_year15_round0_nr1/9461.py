#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

void solve(int q)
{
    char c;
    int n,res=0,sum=0;
    scanf("%d ",&n);
    for(int i=0;i<=n;i++)
    {
        c=getchar();
        sum+=c-'0';
        if(i>res)
        {
            res=i;
        }
        res+=c-'0';
    }
    printf("Case #%d: %d\n",q,res-sum);
}
int main()
{

    int q;
    scanf("%d\n",&q);
    for(int i=1;i<=q;i++)
        solve(i);
}
