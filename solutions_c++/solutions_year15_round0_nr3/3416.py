#include <cstdio>
using namespace std;

const int maxn = 11000 * 128;
char str[maxn];

char prod(char a, char b, bool& has_minus) {
  if (a == '1') return b;
  if (b == '1') return a;
  if (a == b) {
    has_minus = !has_minus;
    return '1';
  }
  if (a == 'i') {
    if (b == 'j') return 'k';
    if (b == 'k') {
      has_minus = !has_minus;
      return 'j';
    }
  }
  if (a == 'j') {
    if (b == 'i') {
      has_minus = !has_minus;
      return 'k';
    }
    if (b == 'k') return 'i';
  }
  if (a == 'k') {
    if (b == 'i') return 'j';
    if (b == 'j') {
      has_minus = !has_minus;
      return 'i';
    }
  }
  puts("ERROR!");
  return 'e';
}

void run(int test_case_number) {
  int l, x;
  scanf("%d %d", &l, &x);
  int new_x = x % 64;
  if (x >= 64) new_x += 64;
  x = new_x;
  scanf("%s", str);
  for (int i = 1; i < x; ++i) {
    for (int j = 0; j < l; ++j) {
      str[i * l + j] = str[j];
    }
  }

  //printf("%s\n", str);

  // Check that total product is -1.
  {
    bool has_minus = false;
    char current = '1';
    for (int i = 0; i < l * x; ++i) {
      current = prod(current, str[i], has_minus);
    }
    if (current != '1' || !has_minus) {
      printf("Case #%d: NO\n", test_case_number);
      return;
    }
  }

  int chars_to_i = 0;
  {
    bool has_minus = false;
    char current = '1';
    for (; chars_to_i < l * x; ++chars_to_i) {
      current = prod(current, str[chars_to_i], has_minus);
      if (current == 'i' && !has_minus) {
        break;
      }
    }
  }

  int chars_to_k = l * x - 1;
  {
    bool has_minus = false;
    char current = '1';
    for (; chars_to_k >= 0; --chars_to_k) {
      current = prod(str[chars_to_k], current, has_minus);
      if (current == 'k' && !has_minus) {
        break;
      }
    }
  }

  //printf("chars_to_i: %d\nchars_to_k: %d\n", chars_to_i, chars_to_k);

  if (chars_to_i < chars_to_k) {
    printf("Case #%d: YES\n", test_case_number);
  } else {
    printf("Case #%d: NO\n", test_case_number);
  }
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 0; i < t; ++i) {
    run(i + 1);
  }
  return 0;
}
