#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define fi first
#define prev asfansjfansjabfasjlbfa
#define se second
#define I "%d"
#define II "%d%d"
#define III "%d%d%d"
#define out_files freopen("A-large.in", "r", stdin);freopen("output.txt", "w", stdout)
#define all(x) (x).begin(), (x).end()
#define fast ios_base::sync_with_stdio(0)
#define sqr(x) (x)*(x)
#define y1 asnflainflawnfaw
#define y0 snalfklawnfasdaspqw

using namespace std;

typedef vector <int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef pair <ll, ll> pii;
typedef vector <pii> vii;
typedef long double ld;

#ifdef WIN32
    #define I64 "%I64d"
#else
    #define I64 "%lld"
#endif // WIN32

const int inf = 1000000000;
const ll INF = 1LL*inf*inf;
const double eps = 1e-9;
const int MAXN = 2500;
const int md = (int)1e9 ;
const double EPS = 1e-5;

struct node
{
    int x;
    char id;
} a[200000];

bool operator < (const node& a, const node& b)
{
    return (a.x>b.x || (a.x == b.x && a.id<b.id));
}

set <node> now;
int t, n;

int main()
{
    fast;
    out_files;
    scanf(I, &t);
    for (int test=1; test<=t; test++)
    {
        now.clear();
        cout << "Case #" << test << ": ";
        scanf(I, &n);
        for (int i=0; i<n; i++)
        {
            scanf(I, &a[i].x);
            a[i].id = char('A'+i);
            now.insert(a[i]);
        }
        while (now.begin() -> x != now.rbegin() -> x)
        {
            //cout << now.begin() -> x << " " << now.begin() -> id << "\n";
            vector <node> cur(0);
            for (set<node> :: iterator it = now.begin(); it != now.end(); it++)
            {
                if (cur.empty()) cur.pb(*it);
                    else
                    {
                        if (cur.back().x == it -> x)
                            cur.pb(*it);
                        else
                            break;
                        if (cur.size() == 3) break;
                    }
            }
            if (cur.size() == 2)
            {
                cout << cur[0].id << cur[1].id << " ";
                now.erase(cur[0]);
                now.erase(cur[1]);
                cur[0].x --;
                cur[1].x --;
                now.insert(cur[0]);
                now.insert(cur[1]);
            } else
            {
                cout << cur[0].id << " ";
                now.erase(cur[0]);
                cur[0].x --;
                now.insert(cur[0]);
            }
        }
        vector <node> q;
        int sum = 0;
        for (set <node> :: iterator it = now.begin(); it != now.end(); it++)
        {
            sum += it -> x;
            q.pb(*it);
        }
        while (sum)
        {
            if (q.size() % 2 == 0)
            {
                for (int i=0; i<q.size(); i+=2)
                    cout << q[i].id << q[i+1].id << " ";
            } else
            {
                cout << q.back().id << " ";
                for (int i=0; i<q.size()-1; i+=2)
                    cout << q[i].id << q[i+1].id << " ";
            }
            sum -= q.size();
        }
        cout << "\n";
    }
    return 0;
}
