#define _CRT_SECURE_NO_WARNINGS

#pragma comment(linker, "/STACK:167777216")
#include <cmath>
#include <math.h>
#include <complex>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>

#include <unordered_map> 
#include <stack> 
#include <time.h> 
#include <fstream> 
#include <queue> 
using namespace std; 
 
#define pb push_back  
#define mp(a,b) make_pair(a,b)   
#define F first  
#define S second  
 
#define all(x) x.begin(), x.end() 
#define sqr(x) ((x)*(x)) 
#define eps 1e-8 
#define inf (int)(1e9+7) 
#define infll (ll)(1e18+3) 
#define sz(x) ((int)x.size()) 
#define M_PI       3.14159265358979323846  
#define PI       3.14159265358979323846   
typedef long long ll; 
typedef  unsigned long long ull; 
typedef  long double ld; 
typedef vector < ll > vll; 
typedef vector < int > vi; 
typedef pair < ll, ll > pll; 
typedef pair < int, int > pii; 
typedef int huint; 
  
const ll mod = 1e9 + 7;

ll n = 16;
int zap = 50;
int cnt = 0;

ll prove(ll x)
{
    if (x % 2 == 0)
    {
        if (x == 2) return -1;
        return 2;
    }
    ll d = 3;
    while (d * d <= x )
    {
        if (x % d == 0) return d;
        d += 2;
    }
    if (d * d > x)return -1;
}

void check(ll x)
{
    vector<ll> st(11);
    vector<ll> sm(11);

    for (int i(2); i <= 10; i++)
        st[i] = 1, sm[i] = 0;
    sm[10] = x;
    while (x > 0)
    {
        ll y = x % 10;
        x = x / 10;
        for (ll i(2); i < 10; i++)
        {
            sm[i] += y * st[i];
            st[i] = st[i] * i;
        } 
    }
    for (int i(2); i <= 10; i++)
    {
        st[i] = prove(sm[i]);
        if (st[i] == -1) return;
    }
    cnt++;
    cout << sm[10] << " ";
    for (int i(2); i <= 10; i++)
    {
        cout << st[i] << " ";
    }
    cout << "\n";
    if (cnt == zap) exit(0);
    
}

int ko, ke;
string s;
void dfs(ll sz)
{  

    if (n == sz)
    {
        if (s.back() == '0') return;
        if (ko == ke)
        {
            cnt++;
            cout << s << " ";
            for (int i(2); i <= 10; i++)
            {
                if (i % 2 == 1) cout << "2 ";
                else cout << i + 1 << " ";
            }
            cout << "\n";
            if (cnt == zap) exit(0);

        }
        return;
    }

    
    s = s + '0';
    dfs(sz + 1);
    s.pop_back();

    if (sz % 2 == 0)
        ke++;
    else
        ko++;

    s = s + '1';
    dfs(sz + 1);
    s.pop_back();

    if (sz % 2 == 0)
        ke--;
    else
        ko--;

}


int main() 
{ 
    ios_base::sync_with_stdio(false); cin.tie(0);  
        freopen("input.txt", "r", stdin);
          freopen("output.txt", "w", stdout);
          
          cout << "Case #1:\n";

          cin >> n >> n >> zap;
           
    
          ke = 1;
          ko = 0;
          s = '1';
          dfs(1);
          
} 