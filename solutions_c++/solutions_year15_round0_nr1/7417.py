#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <math.h> 
#include <vector>
#include <set>
#include <map> 
#include <string.h>
#include <cstdlib> 
#include <limits.h> 
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <functional>
#include <stack>
#include <queue>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> II;
typedef vector<II> VII;

#define PB push_back
#define MP make_pair
#define ALL(a) a.begin(), a.end()
#define MSET(a, b) memset((a), b, sizeof(a))
#define REP(I, N) for(int I = 0; I < N; I++)
#define EPS 0.0000000001
#define IN(a, b) (find((a).begin(), (a).end(), b) != (a).end())
#define FS first
#define SC second
#define TCASE(T) int T; for (cin >> T; T--; )

int main()
{
  int c = 0;
  TCASE(t) {
    c++;
    int sm;
    string s;
    cin >> sm >> s;
    int standing = s[0] - '0', reqd = 0;
    for (int i = 1; i <= sm; i++) {
      if (standing < i) {
        //doesn't matter if s[i] is '0', because string won't end in 0
        reqd += i - standing;
        standing = i;
      }
      standing += s[i] - '0';
    }
    cout << "Case #" << c << ": " << reqd << endl;
  }
	return 0;
}
