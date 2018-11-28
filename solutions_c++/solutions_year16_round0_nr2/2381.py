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

bool check(const string& s)
{
    for (int i(0); i < s.size(); i++)
    {
        if (s[i] == '-') return false;
    }
    return true;
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
              string s;
              cin >> s;
              int k = 0;
              while (!check(s))
              {
                  if (s[0] == '+')
                  {
                      k++;
                      for (int j(0); j < s.size(); j++)
                          if (s[j] == '-') break;
                          else s[j] = '-';
                  }
                  int pz = 0;
                  for (int j(s.size() - 1); j >= 0;j--)
                      if (s[j] == '-')
                      {
                          pz = j; break;
                      }
                  reverse(s.begin(), s.begin() + pz + 1);
                  for (int j(0); j <= pz; j++)
                  {
                      if (s[j] == '-') s[j] = '+';
                      else s[j] = '-';
                  }
                  k++;
              }
              cout << "Case #" << i << ": " << k <<"\n";

          }
          
} 