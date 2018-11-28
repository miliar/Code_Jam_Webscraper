#include <iostream>
#include <algorithm>
#include <vector>

const int MAXL = 10000;
const int MAXX = 10000;
const int INF  = 10009;

using namespace std;

char mul_tab[][8] = {
  {'1', 'i', 'j', 'k', '!', 'I', 'J', 'K'},
  {'i', '!', 'k', 'J', 'I', '1', 'K', 'j'},
  {'j', 'K', '!', 'i', 'J', 'k', '1', 'I'},
  {'k', 'j', 'I', '!', 'K', 'J', 'i', '1'},
  {'!', 'I', 'J', 'K', '1', 'i', 'j', 'k'},
  {'I', '1', 'K', 'j', 'i', '!', 'k', 'J'},
  {'j', 'k', '1', 'I', 'j', 'K', '!', 'i'},
  {'k', 'J', 'i', '1', 'k', 'j', 'I', '!'},
};

char div_tab[8][8];

int char_map[256];
char rchar_map[8] = {'1', 'i', 'j', 'k', '!', 'I', 'J', 'K'};

void init() {
  for (int i = 0; i < 8; ++i)
    char_map[rchar_map[i]] = i;
  for (int i = 0; i < 8; ++i)
    for (int j = 0; j < 8; ++j)
      div_tab[char_map[mul_tab[i][j]]][j] = rchar_map[i];
}

char mul(char a, char b) {
  return mul_tab[char_map[a]][char_map[b]];
}

char div(char a, char b) {
  return div_tab[char_map[a]][char_map[b]];
}

bool solve() {
  int L, X;
  cin >> L >> X;
  string s;
  cin >> s;
  char LM[MAXL];
  LM[0] = '1';
  char RM[MAXL];
  RM[0] = '1';
  vector<int> lis;
  vector<int> ris;
  int mink = INF;
  bool first = true;
  for (int i = 1; i <= L*X; ++i) {
    LM[i] = mul(LM[i-1], s[(i-1)%L]);
    RM[i] = mul(s[(L-i%L)%L], RM[i-1]);
    if (first && RM[i] == 'k') {
      first = false;
      mink = i;
    }
  }
  for (int i = 0; i < L*X; ++i) {
    if (LM[i] == 'i' && RM[L*X-i] == 'i' && mink < L*X-i)
	return true;
  }
  return false;
}

/*
 i from:
  1*i
  i*1
  !*I
  I*!
  K*j
  k*J
  j*k
  J*K
 j from:
  1*j
  j*1
  !*J
  J*!
  k*i
  K*I
  I*k
  i*K
 k from:
  
*/

int main() {
  init();
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
    cout << "Case #" << i << ": " << (solve() ? "YES" : "NO") << endl;
  return 0;
}

