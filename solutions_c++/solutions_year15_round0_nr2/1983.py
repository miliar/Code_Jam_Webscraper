#include <iostream>
#include <stdio.h>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int tt;
int A[1005];
int N;
int check(int num)
{
    int ans = 0;
    for(int i=0;i<N;i++)
    {
        if(A[i]%num==0)ans--;
        ans = ans + (A[i]/num);
    }
    return ans;
}
void solve()
{
    int temp;
    scanf("%d",&N);
    for(int i=0;i<N;i++)
        scanf("%d",&A[i]);
    int ans = 1024;
    for(int i=1;i<1024;i++)
    {
        ans = min(ans,i+check(i));
    }
    printf("Case #%d: %d\n",tt,ans);
}
int main()
{
    int t;
    scanf("%d",&t);
    for(tt = 1;tt <= t;tt++)
    {
        solve();
    }
}
