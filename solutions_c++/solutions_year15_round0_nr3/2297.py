#include <iostream>
#include <string>
using namespace std;

char mul_map[1 << 16];
char typo[10000 * 12];
char result[10000 * 12];

inline int hash_pair(int fst, int snd) {
  return (fst << 8) + snd;
}

void init_mul() {
  mul_map[hash_pair('1', '1')] = '1';
  mul_map[hash_pair('1', 'i')] = 'i';
  mul_map[hash_pair('1', 'j')] = 'j';
  mul_map[hash_pair('1', 'k')] = 'k';
  mul_map[hash_pair('i', '1')] = 'i';
  mul_map[hash_pair('i', 'i')] = -'1';
  mul_map[hash_pair('i', 'j')] = 'k';
  mul_map[hash_pair('i', 'k')] = -'j';
  mul_map[hash_pair('j', '1')] = 'j';
  mul_map[hash_pair('j', 'i')] = -'k';
  mul_map[hash_pair('j', 'j')] = -'1';
  mul_map[hash_pair('j', 'k')] = 'i';
  mul_map[hash_pair('k', '1')] = 'k';
  mul_map[hash_pair('k', 'i')] = 'j';
  mul_map[hash_pair('k', 'j')] = -'i';
  mul_map[hash_pair('k', 'k')] = -'1';
}

inline char mul(char lhs, char rhs) {
  static bool inited = false;
  if (!inited) {
    init_mul();
    inited = true;
  }
  
  char sign = 1;
  if (lhs < 0) {
    lhs = -lhs;
    sign = -sign;
  }
  if (rhs < 0) {
    rhs = -rhs;
    sign = -sign;
  }

  return sign * mul_map[hash_pair(lhs, rhs)];
}

bool is_identical(int len) {
  bool has_i = false, has_j = false, has_k = false;

  result[0] = typo[0];
  if (result[0] == 'i')
    has_i = true;
  for (int i = 1; i < len; i++) {
    result[i] = mul(result[i - 1], typo[i]);
    if (!has_i && result[i] == 'i')
      has_i = true;
    else if (!has_j && result[i] == mul('i', 'j'))
      has_j = true;
  }
  has_k = (result[len - 1] == mul(mul('i', 'j'), 'k'));

  return(has_i && has_j && has_k);
}

bool is_identical(long long len, long long rep) {
  if (rep >= 12)
    rep = (rep % 4) + 8;
  for (int i = 1; i < rep; i++) {
    for (int j = 0; j < len; j++) {
      typo[i * len + j] = typo[j];
    }
  }

  return is_identical(len * rep);
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int t;
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    long long len, rep;
    cin >> len >> rep;
    for (int i = 0; i < len; i++)
      cin >> typo[i];

    cout << "Case #" << tc << ": " << 
      (is_identical(len, rep) ? "YES" : "NO") << endl;
  }

}