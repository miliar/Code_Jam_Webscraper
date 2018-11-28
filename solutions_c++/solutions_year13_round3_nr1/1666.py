#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <limits> 
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

using namespace std;
#define for0(i, l) for(int i=0; i<(l); ++i)
#define ll long long
#define pb push_back
#define sz size()
#define maxt(t) numeric_limits<t>::max()
#define mint(t) numeric_limits<t>::min()
#define GRAPH vector < vector <int> >
#define PATH vector <int>
#define BIT(n, x) (((n)>>(x))&1)
#define DEB(n) if(1) cout << "r" << (n) << endl 


int main () {
  int T;
  cin >> T;
  for0(t,T) {
    string s;
    int N;
    cin >> s >> N;

    int sum = 0;
    int prev_first = -1;
    for0(i,s.length()-N+1) {
      bool all_cons = true;
      for0(n,N) {
        if (s[i+n] == 'a' ||
            s[i+n] == 'e' ||
            s[i+n] == 'o' ||
            s[i+n] == 'u' ||
            s[i+n] == 'i') {
          all_cons = false;
        }
      }

      if (all_cons) {
        sum += i + s.length() - (i + N) + 1 - (prev_first + 1) +
               (i - prev_first - 1)*(s.length()-(i+N));
        prev_first = i;
      }
    }

    cout << "Case #" << t+1 << ": " << sum << endl;
  }
}
