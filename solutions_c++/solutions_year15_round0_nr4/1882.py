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

ifstream fin ("D-small-attempt1.in");
ofstream fout ("out.out");

typedef long long ll;
const int N = 1000+10;
int T;


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    fin >> T;
    
    for(int t = 1 ; t <= T ; t++)
    {
        int n, r, c;
        fin >> n >> r >> c;
      
        if(n == 1)
            fout << "Case #" << t << ": GABRIEL" << endl;
           
        else if(n == 2)
        {
            if(r*c % 2) fout << "Case #" << t << ": RICHARD" << endl;  
            else fout << "Case #" << t << ": GABRIEL" << endl;
        }
        
        else if(n == 3)
        {
            if(min(r, c) == 1 || r*c % 3) fout << "Case #" << t << ": RICHARD" << endl;  
            else fout << "Case #" << t << ": GABRIEL" << endl; 
        }
        
        else
        {
            if(r*c < 12) fout << "Case #" << t << ": RICHARD" << endl;  
            else fout << "Case #" << t << ": GABRIEL" << endl; 
        }
    }

    return 0;
}
