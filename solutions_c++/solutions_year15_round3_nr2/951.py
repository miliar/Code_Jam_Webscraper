#include <algorithm>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
typedef int64_t T;
typedef double prec;

#define ALPHA_SIZE ('Z'-'A'+1)
T K, L, S;
string keyboard, target;
prec freq[ALPHA_SIZE];
vector<char> keys;

T get_max_comb() {
  T r=keys.size();
  for (unsigned int i=1; i<S; i++) {
    r *= keys.size();
  }
  //cout << "max_comb: " << r << "\n";
  return r;
}

void set_freq() {
  for (unsigned int i=0; i<K; i++) {
    if (freq[keyboard[i]-'A'] == 0) {
      keys.push_back(keyboard[i]);
    }
    freq[keyboard[i]-'A']++;
  }
  for (unsigned int i=0; i<ALPHA_SIZE; i++) {
    freq[i] /= K;
    //cout << char('A'+i) << " : " << freq[i] << "\n";
  }
}

string decode_comb(T comb) {
  string word = "";
  for (unsigned i=0; i<S; i++) {
    word += keys[comb%keys.size()];
    comb /= keys.size();
  }
  //cout << word << "\n";
  return word;
}

unsigned int count_bananas(string word) {
  //cout << "count " + word + " : "+ target + "\n";
  string::size_type pos=0;
  unsigned int b=0;

  while (pos<word.length()) {
    pos = word.find(target, pos);
    //cout << "pos " << pos << "\n";
    if (pos == string::npos) {
      break;
    }
    pos++;
    b++;
  }
  //cout << "counted " << b << "\n";
  return b;
}

prec get_probab(string word) {
  prec p=1;
  for (unsigned int i=0; i<word.length(); i++) {
    p *= freq[word[i]-'A'];
  }
  //cout << "prob " << p << "\n";
  return p;
}

prec solve() {
  prec expected = 0;
  unsigned int max_bananas = 0, bananas;
  T max_comb = get_max_comb();
  for (T comb=0; comb<max_comb; comb++) {
    string word = decode_comb(comb);
    bananas = count_bananas(word);
    max_bananas = (max_bananas < bananas ? bananas : max_bananas);
    expected += bananas*get_probab(word);
  }
  //cout << "expected " << expected;
  //cout << "max " << max_bananas << "\n";
  //cout << "max_bananas - expected: " << max_bananas - expected << "\n";
  return max_bananas - expected;
}

int main() {
  vector<prec> result;
  int tests;
  cin >> tests;
  for (int t=0; t<tests; t++) {
    cin >> K >> L >> S >> keyboard >> target;
    keys.clear();
    memset(freq, 0, sizeof(freq[0])*ALPHA_SIZE);
    set_freq();
    result.push_back(solve());
  }
  cout.precision(7);

  for (int i=0; i<int(result.size()); i++) {
    cout << "Case #" << i+1 << ": " << result[i]  << "\n";
  }
  return 0;
}
