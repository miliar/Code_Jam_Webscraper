#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define sd(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define debug(X) cerr << " --> " << #X << " = " << X << endl
#define rep(i, begin, end) for(__typeof(end) i =(begin)-((begin)>(end));i!=(end)-((begin)>(end));i+=1-2*((begin)>(end)))
#define endl "\n"
typedef long long ll; typedef pair<int, int> pii;
const int N = 1123456, lgN = 15, mod = 1000000007;
const double eps = 1e-3, pi = acos(-1.0);
int d[N];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("2.out", "w", stdout);

    int t;
    sd(t);
    for(int tt = 1; tt <= t ; ++tt)
    {
        printf("Case #%d: ", tt);
        string str;
        cin>>str;
        int n = str.size();
        for(int i = 0; i < n; ++i)
        {
            if(str[i] == '+')
                d[i] = 0;
            else
                d[i] = 1;
        }
        int c = 0;
        for(int i = n - 1; i >= 0; --i)
        {
            if((d[i] + c) % 2 == 1)
            {
                c++;
            }
        }
        printf("%d\n", c);
    }
    return 0;
}


