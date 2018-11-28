/**
 * Tags: set
 */
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <math.h>
#include <set>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <assert.h>
#include <map>

#include <sstream>

#include <stdexcept>

using namespace std;

typedef vector<string> vs;
typedef long long ll;
typedef long long int lli;
typedef vector<int> vi;
typedef vector<ll> vll;

int tab[105];
int N;

void flip(int n) {
  int tmp;
  if (n == 0) {
    tab[0] = !tab[0];
    return;
  }

  for (int i = 0; i < n/2+1; i++) {
    tmp = tab[n - i];
    tab[n - i] = !tab[i];
    tab[i] = !tmp;
  }
}

void flipF() {
  int tmp = tab[0];
  int i = 0;
  while(tab[i] == tmp) {
    tab[i] = !tab[i];
    i++;
  }
}



void p() {
  for (int i = 0; i < N; i++) {
    if (tab[i]) {
      cout << "+";
    } else {
      cout << "-";
    }
  }
  cout << endl;
}

bool v() {
  for (int i = 0; i < N; i++) {
    if (!tab[i]) {
      return false;
    }
  }
  return true;
}

int last() {
  int tmp = tab[N-1];
  for (int i = N - 2; i >= 0; i--) {
    if (tab[i] != tmp) {
      return i;
    }
  }
  return -1;
}

void flipL() {
  flip(last());
}

int main(int argc, const char **argv) {
  int cases;
  string tmp;
  cin >> cases;
  int total, k;
  for (int caseI = 1; caseI <= cases; caseI++) {
    cin >> tmp;
    N = tmp.size();
    for (int i = 0; i < N; i++) {
      tab[i] = tmp[i] == '+' ? 1 : 0;
    }
    total = 0;
    while (!v()) {
      // p();
      k = last();
      if (k == -1) {
        total++;
        break;
      }
      if (tab[0] != tab[k]) {
        flipF();
      } else {
        flipL();
      }
      total++;
    }
    cout << "Case #" << caseI << ": " << total << endl;
  }

  return 0;
}
