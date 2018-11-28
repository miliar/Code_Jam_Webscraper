#include <bits/stdc++.h>

#define ft first
#define st second
#define mp make_pair
#define pb push_back
#define sz(n) int(n.size())


using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

const int N = 1e5;
const int inf = 1e9 + 7;
const ll INF = 1e18 + 7;

string s, t;
int d = inf;
string x, y;

int get(const string &s) 
{
    int res = 0;
    for (int i = 0; i < sz(s); i ++) 
    {
        res  = res * 10 + s[i] - 48;
    }
    return res;
}

void rec(int v) 
{
	if (v == sz(s) + sz(t))
    {
        int a = get(s);
        int b = get(t);
        int cur = abs(a - b);
        if (cur < d) 
        {
            d = cur;
            x = s;
            y = t;
        }
    }
    else 
    {
        if (v < sz(s)) 
        {
            if (s[v] == '?') 
            {
                for (char ch = '0'; ch <= '9'; ch ++) 
                {                                  
                    s[v] = ch;
                    rec(v + 1);
                }
                s[v] = '?';
            } 
            else rec(v + 1);
        } 
        else 
        {
            int p = v - sz(s);
            if (t[p] == '?') 
            {
                for (char ch = '0'; ch <= '9'; ch ++) 
                {
                    t[p] = ch;
                    rec(v + 1);
                }
                t[p] = '?';
            } 
            else rec(v + 1);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tp;
    cin >> tp;
    for (int i = 1; i <= tp; i ++) 
    {
        cout << "Case #" << i << ": ";
        cin >> s >> t;
        d = inf;
        rec(0);
        cout << x << " " << y;
        cout << "\n";
    }
    return 0;
}