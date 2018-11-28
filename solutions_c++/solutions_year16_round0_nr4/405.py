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

const int MAXN = 100000;

long long T;
long long K, C, S;
long long ans[1000];

void solve()
{
    int part = ceil((double)K/(double)C);
    if( S < part )
    {
        cout << " IMPOSSIBLE" << endl;
        return;
    }
    for(int i=1;i<=part;i++)
    {
        ans[i] = (long long)(i-1)*C+1;
        for(int j=2;j<=C;j++)
            ans[i] = (ans[i]-1)*K+(long long)min(((i-1)*C+j),K);
    }
    for(int i=1;i<=part;i++)
        cout << " " << ans[i];
    cout << endl;
}
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("output-large.txt","w",stdout);
    cin >> T;
    for(int i=1;i<=T;i++)
    {
        cin >> K >> C >> S;
        cout << "Case #" << i << ":";
        solve();
    }

    return 0;
}
