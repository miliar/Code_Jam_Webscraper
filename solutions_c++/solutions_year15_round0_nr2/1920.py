#include <bits/stdc++.h>
using namespace std;
#define length(x) (int)x.size()
const double pi=acos(-1);

int b[10000], a[10000], n, f[2000][2000];

void init()
{
    for(int i=1; i<=1000; i++)
    {
        for(int j=0; j<=i; j++) f[i][j] = 0;
        for(int j=i+1; j<=1000; j++)
            f[i][j] = (j+i-1)/i - 1;
    }
}

int solve()
{
    cin>>n;
    for(int i=1; i<=n; i++) cin>>a[i];
    sort(1+a, 1+n+a);
    int res = a[n];
    for(int i=1; i<=a[n]; i++)
    {
        int sum = i;
        for(int j=1; j<=n; j++) sum += f[i][a[j]];
        res = min(res, sum);
    }
    return res;

}

int main()
{
    freopen("input.inp","r",stdin);
    freopen("output.out","w",stdout);
    init();
    int test;  cin>>test;
    for(int t=1; t<=test; t++) cout<<"Case #"<<t<<": "<<solve()<<endl;
    return 0;
}
