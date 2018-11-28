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

int f[10];
int k = 0;

void check(ll x)
{
    while (x > 0)
    {
        if (f[x % 10] == 0) k++;
        f[x % 10] = 1;
        x = x / 10;
    }
}

int main() 
{ 
    ios_base::sync_with_stdio(false); cin.tie(0);  
        freopen("input.txt", "r", stdin);
          freopen("output.txt", "w", stdout);
          

          int n;
          cin >> n; 
          for (int i(1); i <= n; i++)
          {
              ll x;
              cin >> x; 
              if (x == 0)
              {
                  cout << "Case #"<< i <<": INSOMNIA\n";
                  continue;
              }
              k = 0;
              for (int i(0); i < 10; i++) f[i] = 0; 
              ll y = x;
              while(k < 10   )
              {
                  check(x); 
                  x = x + y; 
              }
              x = x - y; 

              cout << "Case #" << i << ": " << x <<"\n";

          }
          
} 