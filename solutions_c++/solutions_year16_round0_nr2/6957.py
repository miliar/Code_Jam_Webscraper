#include <iostream>
#include <string>

using namespace std;

int ComputeNbPermutations(const string& s) {
  int nb_permut = 0;
  char c = s[s.size()-1];
  for (int i = s.size()-2; i >= 0; --i) {
    char new_c = s[i];
    if (new_c != c) {
      nb_permut++;
      c = new_c;
    }
  }
  if (s[s.size()-1] == '-') {
    nb_permut++;
  }
  return nb_permut;
}


int main(int argc, char** argv) {
  int nb_test;
  cin >> nb_test;
  for (int i = 1; i <= nb_test; ++i) {
    string s;
    cin >> s;
    int res = ComputeNbPermutations(s);
    cout << "Case #" << i << ": " << res << endl;
  }
}
