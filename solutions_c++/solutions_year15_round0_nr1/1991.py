#include <bits/stdc++.h>
using namespace std;
#define length(x) (int)x.size()
const double pi=acos(-1);
int main()
{
    freopen("input.inp","r",stdin);
    freopen("output.out","w",stdout);
    int test;   cin>>test;
    for(int t=1; t<=test; t++)
    {
        string st;  int n;
        cin>>n>>st;
        int res = 0, sum = st[0] - 48;
        for(int i=1; i<=n; i++)
        {
            if (sum<i) res += i - sum;
            sum = max(sum, i) + st[i]-48;
        }
        cout<<"Case #"<<t<<": "<<res<<endl;

    }
    return 0;
}
