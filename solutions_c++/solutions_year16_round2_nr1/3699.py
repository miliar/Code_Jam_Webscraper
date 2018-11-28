#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

#define AL 'Z'-'A'+1

using namespace std;
static string literals[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int counts[10][AL];
int counta[AL];
bool done = false;
vector<int> result;

void tdig(int cas) {
  bool allz = 1;
  for (int i = 0; i < AL; ++i) {
    if (counta[i] != 0) allz = 0;
  }
  if (allz) {
    sort(result.begin(), result.end());
    cout << "Case #" << cas+1 << ": ";
    for (int a : result) cout << a;
    cout << endl;
    done = true;
    return;
  }
  int tcnt[AL];
  for(int i = 0; i < AL; ++i) tcnt[i] = counta[i];
  for (int ci = 0; ci < 10; ci++) {
    bool allpresent = true;
    for (int c = 0; c < AL; c++) {
      if (counta[c] < counts[ci][c]) { allpresent = false; break; }
    }
    //cout << ci << " " << allpresent<< endl;
    if (allpresent) {
      for (int c = 0; c < AL; c++) {
        counta[c] -= counts[ci][c];
      }
      result.push_back(ci);
      tdig(cas);
      result.pop_back();
      if(done) return;
      for (int i = 0; i < AL; ++i) counta[i] = tcnt[i];
    }
  }
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  for (int i = 0; i < 10; ++i) {
    for (char c : literals[i]) {
      c-='A';
      counts[i][c]++;
    }
  }
  for(int cas = 0; cas < T; ++cas) {
    string input;
    cin >> input;
    for(int i = 0; i < AL; ++i) counta[i] = 0;
    for (char c : input) {
      c-='A';
      counta[c]++;
    }
    done = false;
    result.clear();
    tdig(cas);
  }
}
