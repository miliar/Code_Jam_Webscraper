#include <cstdlib>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <map>
#include <deque>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <iomanip>
#include <cctype>
#include <complex>
#include <numeric>

#define sqr(x) ((x)*(x))
#define comb2(x) ((x)*((x)-1)/2)
#define mod(x) (((x) + MOD) % MOD)
#define All(store) store.begin(), store.end()
#define Unique(store) store.resize(unique(All(store)) - store.begin())
#define Assign(a, b, s, e) for(int i = s ; i <= e ; i++) b[i] = a[i];
#define IF(condition, x, y) (condition ? x : y)
#define psb push_back
#define ppb pop_back
#define psf push_front
#define ppf pop_front
#define create make_pair
#define pii pair<int, int>
#define pll pair<ll, ll>
#define X first
#define Y second

using namespace std;

ifstream fin ("C-small-attempt1.in");
ofstream fout ("out.out");

typedef long long ll;
const int N = 10000 + 10, MOD = 1e9 + 7;
int T;
int m[][5] = { {0, 0, 0, 0, 0} ,
              {0, +1, +2, +3, +4} ,
              {0, +2, -1, +4, -3} ,
              {0, +3, -4, -1, +2} ,
              {0, +4, +3, -2, -1} };
              
inline int Int(char c)
{
    if(c == 'i') return 2;
    if(c == 'j') return 3; 
    if(c == 'k') return 4; 
}

inline int mul(int i, int j)
{
    int sgni = IF(i < 0, -1, +1);  
    int sgnj = IF(j < 0, -1, +1); 
    return sgni * sgnj * m[abs(i)][abs(j)];  
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    fin >> T;
    
    for(int t = 1 ; t <= T ; t++)
    {
        int L, n;
        string s, in;
        fin >> L >> n >> in;
        
        for(int i = 0 ; i < n ; i++)
            s += in;
            
        int res = 1;
        n *= L;
        
        for(int i = 0 ; i < n ; i++)
            res = mul(res, Int(s[i]));
                
        if(res != -1){ fout << "Case #" << t << ": NO" << endl; continue; }
        
        res = 1;
        int l = -1, r = -1;
        
        for(int i = 0 ; i < n ; i++)
        {
            res = mul(res, Int(s[i]));
            if(res == 2)
            {
                l = i;
                break;
            }    
        } 
        
        if(l == -1){ fout << "Case #" << t << ": NO" << endl; continue; }
        
        res = 1;
        
        for(int i = n-1 ; i > 1 ; i--)
        {
            res = mul(Int(s[i]), res);
            if(res == 4)
            {
                r = i;
                break;
            }    
        } 
        
        if(r <= l) fout << "Case #" << t << ": NO" << endl;
        else fout << "Case #" << t << ": YES" << endl;
    }

    return 0;
}
