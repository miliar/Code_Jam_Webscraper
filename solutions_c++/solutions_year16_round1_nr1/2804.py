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
    freopen("1.out", "w", stdout);

    int t;
    sd(t);
    for(int tt = 1; tt <= t ; ++tt)
    {
        printf("Case #%d: ", tt);
        string s, r;
        cin>>s;
        char ma = s[0];
        for(char c : s)
            ma = max(c, ma);
        char cur = 'A';
        for(int i = 0; i < s.size(); ++i)
        {
            char c = s[i];
            if(cur <= c)
            {
                s[i] = -1;
                r += c;
                cur = c;
            }
        }
        reverse(r.begin(), r.end());
        for(int i = 0; i < s.size(); ++i)
            if(s[i] >= 0)
                r += s[i];
        cout<<r<<endl;
    }
    return 0;
}



