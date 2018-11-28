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

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    sd(t);
    for(int tt = 1; tt <= t ; ++tt)
    {
        printf("Case #%d: ", tt);
        ll n;
        sl(n);
        if(n == 0)
        {
            printf("INSOMNIA\n");
        }
        else
        {
            set<int> s;
            ll c = n;
            while(s.size() < 10)
            {
                ll z = c;
                while(z > 0)
                    s.insert(z % 10), z /= 10;
                c += n;
            }
            cerr<<c - n<<endl;
            printf("%lld\n", c - n);
        }
    }
    return 0;
}


