#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define NL '\n'
#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define mem(a,b) memset(a,b,sizeof(a))
#define FOR(i,j,k) for(i=j;i<=k;i++)
#define REV(i,j,k) for(i=j;i>=k;i--)
#define READ(f) freopen(f,"r",stdin)
#define WRITE(f) freopen(f,"w",stdout)
#define pi 2.0*acos(0.0)
#define MOD 1000000007
#define MAX 100005

int main()
{
    //READ("D-small-attempt0.in");
    //WRITE("D-small-attempt0.out");
    std::ios_base::sync_with_stdio(0);
    int cases, caseno=0, n, i, j, k, cnt, sum;

    cin >> cases;

    while(cases--)
    {
        cin >> n >> j >> k;

        cout << "Case #" << ++caseno << ":";

        for(i = 1; i <= k; i++) cout << " " << i;
        cout << NL;
    }

    return 0;
}

