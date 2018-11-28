#include <string>
#include <vector>
#include <iostream>
#include <set>
#include <cstdio>
#include <list>

using namespace std;

typedef long long int LL;

void showhist(vector <int> hist) {
  int i;

  return;

  cout << "ABCDEFGHIJKLMNOPQRSTUVWXYZ" << endl;
  for (i = 0; i < 26; i++) {
    cout << hist[i];
  }
  cout << endl;
}
  

vector < vector <int> > formtable(void) {
  vector < vector <int> > P;
  int i, j;
  string stbl[10] = {
    "ZERO", "ONE", "TWO", "THREE", "FOUR",
    "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
  };

  for (i = 0; i <= 9; i++) {
    vector <int> prof(26, 0);
    for (j = 0; j < stbl[i].length(); j++) {
      int c;
      c = stbl[i][j];
      prof[c - 'A']++;
    }
    P.push_back(prof);
    showhist(prof);
  }

  return P;
}

vector <int> makehist(string s) {
  vector <int> prof(26, 0);
  int j, c;
  for (j = 0; j < s.length(); j++) {
    c = s[j];
    prof[c - 'A']++;
  }

  showhist(prof);
  return prof;
}


vector <int> reduce( vector <int> h1, vector <int> h2, int coef) {
  vector <int> prof(26, 0);
  int i;
  for (i = 0; i < 26; i++) {
    prof[i] = h1[i] - coef * h2[i];
  }
  showhist(prof);
  return prof;
}

vector <int> decomp(vector <int> hist, vector < vector <int> > P) {
  // even count
  int x;
  int mult;
  vector <int> phoneno(10, 0);

  x = 0;
  mult = hist['Z'-'A'];
  phoneno[x] = mult;
  hist = reduce(hist, P[x], mult);

  x = 2;
  mult = hist['W'-'A'];
  phoneno[x] = mult;
  hist = reduce(hist, P[x], mult);

  x = 4;
  mult = hist['U'-'A'];
  phoneno[x] = mult;
  hist = reduce(hist, P[x], mult);

  x = 6;
  mult = hist['X'-'A'];
  phoneno[x] = mult;
  hist = reduce(hist, P[x], mult);

  x = 8;
  mult = hist['G'-'A'];
  phoneno[x] = mult;
  hist = reduce(hist, P[x], mult);

  x = 1;
  mult = hist['O'-'A'];
  phoneno[x] = mult;
  hist = reduce(hist, P[x], mult);

  x = 3;
  mult = hist['R'-'A'];
  phoneno[x] = mult;
  hist = reduce(hist, P[x], mult);

  x = 5;
  mult = hist['F'-'A'];
  phoneno[x] = mult;
  hist = reduce(hist, P[x], mult);

  x = 7;
  mult = hist['S'-'A'];
  phoneno[x] = mult;
  hist = reduce(hist, P[x], mult);

  x = 9;
  mult = hist['I'-'A'];
  phoneno[x] = mult;
  hist = reduce(hist, P[x], mult);

  return phoneno;

}


int main(void) {
  int T, t;


  vector < vector <int> > P;
  P = formtable();


  cin >> T;

  for (t = 1; t <= T; t++) {
    string S;
    vector <int> hist;
    vector <int> phoneno;
    cin >> S;
    hist = makehist(S);
    phoneno = decomp(hist, P);
    cout << "Case #" << t << ": ";

    int n;

    for (n = 0; n <= 9; n++) {
      int cnt;
      for (cnt = phoneno[n]; cnt; cnt--) {
	cout << n;
      }
    }
    cout << endl;

  }
  return 0;
}
