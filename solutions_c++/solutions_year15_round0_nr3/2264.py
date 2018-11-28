#include <iostream>
#include <algorithm>
#include <string>
#include <queue>

int T;
long long int X;
int L;
long long int N;
std::string S;
int a[10000];
int comp[4][4] = {
  {0, 1, 2, 3},
  {1, 0, 3, 2},
  {2, 3, 0, 1},
  {3, 2, 1, 0}
};
int comp_sign[4][4] = {
  {1, 1, 1, 1},
  {1, -1, 1, -1},
  {1, -1, -1, 1},
  {1, 1, -1, -1}
};

int left_right[10000];
int left_right_sign[10000];
int right_left[10000];
int right_left_sign[10000];

std::pair<int, int> parts[4];


bool compute();
void preprocess();

int main(int argc, const char* argv[]) {

  std::cin >> T;
  for (int i = 1; i <= T; i++) {
     std::cin >> L >> X;
     N = L * X;
     std::cin >> S;
     for (int k = 0; k < L; k++) {
       int num;
       switch (S[k]) {
         case 'i':
           num = 1;
           break;
         case 'j':
           num = 2;
           break;
         case 'k':
           num = 3;
           break;
         default:
           std::cout << "SOMETHING WRONG" << std::endl;
       }
       a[k] = num;
     }
     preprocess();
     bool r = compute();
     if (r)
       std::cout << "Case #" << i << ": YES" << std::endl;
     else
       std::cout << "Case #" << i << ": NO" << std::endl;
  }
  return 0;
}

bool compute() {
  std::pair<int, int> val_XL = parts[X % 4];
  if ((val_XL.first != -1) || (val_XL.second != 0))
    return false;
  for (int i = 0; i < L; i++)
    for (int iX = 0; iX < 4; iX++)
      if (i + iX * L < N) {
        int val_left = comp[parts[iX].second][left_right[i]];
        int sign_left = left_right_sign[i] * parts[iX].first * comp_sign[parts[iX].second][left_right[i]];
        if ((sign_left != 1) || (val_left != 1))
          continue;
        for (int j = 0; j < L; j++)
          for (int jX = 0; jX < 4; jX++){
            long long int pos = N - (L - j + jX * L);
            if (pos <= i + iX * L + 1)
              continue;
            int val_right = comp[right_left[j]][parts[jX].second];
            int sign_right = right_left_sign[j] * parts[jX].first * comp_sign[right_left[j]][parts[jX].second];
            if ((sign_right == 1) && (val_right == 3))
              return true;
          }
      }
  return false;
}

void preprocess() {
  int current = 0;
  int sign = 1;
  for (int i = 0; i < L; i++){
    sign = sign * comp_sign[current][a[i]];
    current = comp[current][a[i]];
    left_right[i] = current;
    left_right_sign[i] = sign;
  }
  for (int i = 0; i < L; i++) {
    current = 0;
    sign = 1;
    for (int j = i; j < L; j++) {
      sign = sign * comp_sign[current][a[j]];
      current = comp[current][a[j]];
     }
    right_left[i] = current;
    right_left_sign[i] = sign;
  }
  int val_L = left_right[L - 1];
  int sign_L = left_right_sign[L - 1];
  
  current = 0;
  sign = 1;
  parts[0] = std::pair<int, int>(sign, current);
  for (int i = 1; i < 4; i++){
    sign = sign * sign_L * comp_sign[current][val_L];
    current = comp[current][val_L];
    parts[i] = std::pair<int, int>(sign, current);
  }
    

  /*
  std::cout << "Left to right" << std::endl;
  for (int i = 0; i < N; i++) {
    std::cout << left_right_sign[i] << "*" << left_right[i] << " , ";
  }
  std::cout << std::endl;
  std::cout << "Right to left" << std::endl;
  for (int i = 0; i < N; i++) {
    std::cout << right_left_sign[i] << "*" << right_left[i] << " , ";
  }
  std::cout << std::endl;
  */

}
