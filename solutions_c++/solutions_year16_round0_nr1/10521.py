#pragma comment(linker, "/STACK:16777216")
#include <vector>
#include <limits.h>
#include <string>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <queue>
#include <set>
#include <memory.h>
#include <string.h>
#include <deque>
#include <assert.h>
#include <stack>
using namespace std;

#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define inf 2000000000
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;

int t;
long long n;

set<int> have;

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> t;
  for(int tt = 1; tt <= t; tt++){
    have.clear(); 
    cin >> n;
    if (n == 0){
      cout << "Case #" << tt << ": " << "INSOMNIA" << endl;
      continue;
    }
    long long i = 1;
    while(true){
      long long x = i*n;
      while(x){
        have.insert(x%10);
        x /= 10;
      }

      if (have.size() == 10)
        break;

      i++;
    }
    cout << "Case #" << tt << ": " << i*n << endl;
  }

  return 0;
}
