#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;


const int MAXD = 105;
char val[MAXD];
bool check_rev(long long v)
{
    int len = 0;
    for(long long t = v; t != 0; t /= 10)
        val[len++] = t % 10;

    bool flag = true;
    for(int j = 0; len - 1 - j > j; j++)
        if (val[len - 1 - j] != val[j])
        {
            flag = false;
            break;
        }

    return flag;
}

vector<long long> vlst;
void solve_num(long long n)
{
    int c = 0;
    int r = sqrt(n);
    for(int i = 1; i <= r; i++)
    {
        long long v = (long long)i * i;
        if (check_rev(i) && check_rev(v))
        {
            //cout << v << "LL,";
            vlst.push_back(v);
        }
    }
}

int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("C.out","w",stdout);

    solve_num(1e14);

    int tnum;
    cin >> tnum;
    for(int t = 1; t <= tnum; t++)
    {
        long long a,b;
        cin >> a >> b;
        int ans = upper_bound(vlst.begin(),vlst.end(),b) - lower_bound(vlst.begin(),vlst.end(),a);
        printf("Case #%d: %d\n",t,ans);
    }

    return 0;
}
