#include <math.h>

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

const int na = 100;

int
uniq(string s) {
  int m = 0;

  for(int j = 0; j < s.length(); j++) {
    m |= 1 << (s[j]-'a');
  }

  return m;
}

void
counts(string s, int* c) {
  for(int i = 0; i < na; i++) {
    c[i] = 0;
  }

  int n = 0;
  for(int i = 1; i < s.length(); i++) {
    if(s[i] == s[i-1]) {
      c[n]++;
    } else {
      n++;
    }
  }
}

int
main() {
  int T;

  cin >> T;

  for(int i = 1; i <= T; i++) {
    int N;

    cin >> N;

    int n = 0;
    int n2 = 0;
    int c[100][100];
    string t;

    for(int j = 0; (j < N) && (n == 0); j++) {
      string s;

      cin >> s;

      string tmp = s;
      string u = tmp.substr(0, unique(tmp.begin(), tmp.end())-tmp.begin());

      if(j == 0) {
	t = u;
      } else {
	if(u != t) {
	  n = -1;
	}
      }

      counts(s, c[j]);
    }

    if(n == 0) {
      int avg[100];
      for(int j = 0; j < na; j++) {
	avg[j] = 0;
	for(int k = 0; k < N; k++) {
	  avg[j] += c[k][j];
	}
	avg[j] = round(((double)avg[j])/N);
      }
      
      for(int j = 0; j < na; j++) {
	for(int k = 0; k < N; k++) {
	  n += abs(c[k][j] - avg[j]);
	}
	n2 += 2*abs(c[0][j] - c[1][j])/2;
      }
    }


    cout << "Case #" << i << ": ";
    if(n < 0) {
      cout << "Fegla Won";
    } else {
      cout << n;
    }
    
    cout << endl;
  }

  return 0;
}

