/**
 * Problem: A
 */
#include <algorithm>
#include <assert.h>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#include <stdexcept>

using namespace std;

typedef vector<string> vs;
typedef long long ll;
typedef long long int lli;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<ll> vll;

int c(char c) {
  return c-48;
}

int letters[200];
int totalOcc[20];

void calc() {
  int nb, total;
  nb = letters[c('Z')];
  letters[c('Z')] -= nb;
  letters[c('E')] -= nb;
  letters[c('R')] -= nb;
  letters[c('O')] -= nb;
  totalOcc[0] += nb;

  nb = letters[c('W')];
  letters[c('T')] -= nb;
  letters[c('W')] -= nb;
  letters[c('O')] -= nb;
  totalOcc[2] += nb;

  nb = letters[c('U')];
  letters[c('F')] -= nb;
  letters[c('O')] -= nb;
  letters[c('U')] -= nb;
  letters[c('R')] -= nb;
  totalOcc[4] += nb;

  nb = letters[c('X')];
  letters[c('S')] -= nb;
  letters[c('I')] -= nb;
  letters[c('X')] -= nb;
  totalOcc[6] += nb;

  nb = letters[c('G')];
  letters[c('E')] -= nb;
  letters[c('I')] -= nb;
  letters[c('G')] -= nb;
  letters[c('H')] -= nb;
  letters[c('T')] -= nb;
  totalOcc[8] += nb;

  nb = letters[c('H')];
  letters[c('T')] -= nb;
  letters[c('H')] -= nb;
  letters[c('R')] -= nb;
  letters[c('E')] -= nb;
  letters[c('E')] -= nb;
  totalOcc[3] += nb;

  nb = letters[c('O')];
  letters[c('O')] -= nb;
  letters[c('N')] -= nb;
  letters[c('E')] -= nb;
  totalOcc[1] += nb;

  nb = letters[c('S')];
  letters[c('S')] -= nb;
  letters[c('E')] -= nb;
  letters[c('V')] -= nb;
  letters[c('E')] -= nb;
  letters[c('N')] -= nb;
  totalOcc[7] += nb;

  nb = letters[c('V')];
  letters[c('F')] -= nb;
  letters[c('I')] -= nb;
  letters[c('V')] -= nb;
  letters[c('E')] -= nb;
  totalOcc[5] += nb;

  nb = letters[c('I')];
  letters[c('N')] -= nb;
  letters[c('I')] -= nb;
  letters[c('N')] -= nb;
  letters[c('E')] -= nb;
  totalOcc[9] += nb;
}

int main(int argc, const char **argv) {
  int cases;
  cin >> cases;
  string str;
  int N;

  for (int caseI = 1; caseI <= cases; caseI++) {
    cin >> str;
    memset(letters, 0, sizeof(letters));
    memset(totalOcc, 0, sizeof(totalOcc));
    for (int i = 0; i < (int)str.size(); i++) {
      letters[c(str[i])]++;
    }
    calc();
    cout << "Case #" << caseI << ": ";
    for (int i = 0; i < 10; i++) {
      for (int j = 0; j < totalOcc[i]; j++) {
        cout << i;
      }
    }
    cout << endl;
  }

  return 0;
}
