#include <iostream>
#include <string>
#include <vector>

int tb[8][8] = {{0,1,2,3,4,5,6,7}, 
                {1,4,3,6,5,0,7,2}, 
                {2,7,4,1,6,3,0,5},
                {3,2,5,4,7,6,1,0},
                {4,5,6,7,0,1,2,3},
                {5,0,7,2,1,4,3,6},
                {6,3,0,5,2,7,4,1},
                {7,6,1,0,3,2,5,4}};
enum {code_1, code_i, code_j, code_k};

int main() {
  int T, L, n_period;
  long long X;
  std::vector<int> vi;
  vi.reserve(10000);
  std::string str;

  std::cin >> T;

  for (int n_case = 1; n_case <= T; n_case++) {
    bool is_yes = false;
    std::cin >> L >> X >> str;
    vi.resize(L);
    for (int i = 0; i < L; i++) {
      if (str[i] == 'i')
        vi[i] = code_i;
      else if (str[i] == 'j')
        vi[i] = code_j;
      else
        vi[i] = code_k;
    }
    n_period = 0;
    int value = code_1, pointer, pv, c = code_i;

    int j = 0;
    for (; n_period < 16 && c <= code_k; ) {
      for (; j < L; j++) {
        value = tb[value][vi[j]];
        if (value == c) {
          c++;
          value = code_1;
          if (c > code_k) {j++; break;}
        }
      }
      if (j == L) {
        j = 0;
        n_period++;
      }
    }
    if (c > code_k) {
      if (j != 0) n_period++;
      if (n_period <= X) {
        X -= n_period;
        X %= 4;
        pv = value = code_1;
        for (int i = 0; i < j; i++)
          pv = tb[pv][vi[i]];
        for (int i = j; i < L; i++) value = tb[value][vi[i]];
        pv = tb[pv][value];
        if (j == 0) value = code_1;
        for (int i = 0; i < X; i++)
          value = tb[value][pv];
        if (value == code_1) is_yes = true;
      }
    }
    std::cout << "Case #" << n_case << ": ";
    if (is_yes)
      std::cout << "YES\n";
    else
      std::cout << "NO\n";
  }

  return 0;
}
