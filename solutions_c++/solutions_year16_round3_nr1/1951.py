#include <iostream>
#include <vector>

using namespace std;

unsigned evacuate(unsigned & c, vector<unsigned> & P) {
  unsigned max = 0, max_pos = 0, tie_pos = 99;
  for(unsigned i = 0; i < P.size(); ++i) {
    if(P[i] > max) {
      max = P[i];
      max_pos = i;
      tie_pos = 99;
    } else if(max > 0 && P[i] == max) {
      tie_pos = i;
    }
  }

  cout << char('A' + max_pos);
  P[max_pos]--;
  c--;
  if(c & 1) {
    if(tie_pos < 99) {
      cout << char('A' + tie_pos);
      P[tie_pos]--;
      c--;
    } else {
      cout << char('A' + max_pos);
      P[max_pos]--;
      c--;
    }
  }

  return c;
}

int main() {
  unsigned T;
  cin >> T;
  for(unsigned i = 1; i <= T; ++i) {
    cout << "Case #" << i << ": ";

    unsigned nP, c = 0;
    cin >> nP;
    vector<unsigned> P(nP);
    for(unsigned j = 0; j < nP; ++j) {
      cin >> P[j];
      c += P[j];
    }

    while(evacuate(c, P))
      cout << " ";
    cout << endl;
  }

  return 0;
}
