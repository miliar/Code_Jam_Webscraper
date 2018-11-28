#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

const int MAXN = 10000;

bool visited[10];
long long T;
long long N;

void split(long long x)
{
    long long tmp = x;
    while( tmp != 0 )
    {
        visited[tmp%10] = true;
        tmp /= 10;
    }
}
bool judge()
{
    for(int i=0;i<10;i++)
        if( visited[i] == false )
            return false;
    return true;
}
void solve(int x)
{
    if( N == 0 )
    {
        printf("Case #%d: INSOMNIA\n",x);
        return;
    }

    for(int i=1;i<=MAXN;i++)
    {
//        cout << N * (long long)i << endl;
        split(N*(long long)i);
        if( judge() == true )
        {
            printf("Case #%d: %lld\n",x,N*(long long)i);
            return;
        }
    }
    printf("Case #%d: INSOMNIA\n",x);
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output-large.txt","w",stdout);

    scanf("%lld",&T);
    for(int i=1;i<=T;i++)
    {
        memset(visited, false, sizeof(visited));
        scanf("%lld",&N);
        solve(i);
    }

    return 0;
}
