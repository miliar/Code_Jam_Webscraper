#include <cstdio>
#include <algorithm>
using namespace std;
void f(string& s, char letter, int n)
{
  if (n == 0) return;
  for (auto& i : s) {
    if (i == letter) {
      i = '_';
      n--;
      if (n == 0) return;
    }
  }
}
int main() {
  int T; scanf("%d ", &T);
  for (auto test = 0; test<T; test++) {
    printf("Case #%d: ", test+1);
    char str[2001]; scanf("%s ", str);
    string s(str);
    auto zeros = count(begin(s), end(s), 'Z');
    f(s, 'Z', zeros);
    f(s, 'E', zeros);
    f(s, 'R', zeros);
    f(s, 'O', zeros);
    auto twos = count(begin(s), end(s), 'W');
    f(s, 'T', twos);
    f(s, 'W', twos);
    f(s, 'O', twos);
    auto fours = count(begin(s), end(s), 'U');
    f(s, 'F', fours);
    f(s, 'O', fours);
    f(s, 'U', fours);
    f(s, 'R', fours);
    auto sixs = count(begin(s), end(s), 'X');
    f(s, 'S', sixs);
    f(s, 'I', sixs);
    f(s, 'X', sixs);
    auto fives = count(begin(s), end(s), 'F');
    f(s, 'F', fives);
    f(s, 'I', fives);
    f(s, 'V', fives);
    f(s, 'E', fives);
    auto ones = count(begin(s), end(s), 'O');
    f(s, 'O', ones);
    f(s, 'N', ones);
    f(s, 'E', ones);
    auto sevens = count(begin(s), end(s), 'V');
    f(s, 'S', sevens);
    f(s, 'E', 2*sevens);
    f(s, 'V', sevens);
    f(s, 'N', sevens);
    auto nines = count(begin(s), end(s), 'N');
    f(s, 'N', nines);
    nines /= 2;
    f(s, 'I', nines);
    f(s, 'E', nines);
    auto eights = count(begin(s), end(s), 'I');
    f(s, 'E', eights);
    f(s, 'I', eights);
    f(s, 'G', eights);
    f(s, 'H', eights);
    f(s, 'T', eights);
    auto threes = count(begin(s), end(s), 'T');
    for (auto i = 0u; i < zeros; i++) {
      putchar('0');
    }
    for (auto i = 0u; i < ones; i++) {
      putchar('1');
    }

   for (auto i = 0u; i < twos; i++) {
      putchar('2');
    }

   for (auto i = 0u; i < threes; i++) {
      putchar('3');
    }

   for (auto i = 0u; i < fours; i++) {
      putchar('4');
    }

   for (auto i = 0u; i < fives; i++) {
      putchar('5');
    }

   for (auto i = 0u; i < sixs; i++) {
      putchar('6');
    }

   for (auto i = 0u; i < sevens; i++) {
      putchar('7');
    }

   for (auto i = 0u; i < eights; i++) {
      putchar('8');
    }

   for (auto i = 0u; i < nines; i++) {
      putchar('9');
    }
  putchar('\n');

  }
  return 0;
}
