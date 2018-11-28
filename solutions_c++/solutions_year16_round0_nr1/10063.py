#include <cstdio>
#include <unordered_set>

void addDigitsToSet(int number);

using namespace std;
unordered_set<int> set;

int main() {

  setbuf(stdout, NULL);

  //const int NMAX = 200;
  int T;
  scanf("%d", &T);

  for(int test = 1; test <= T; ++test) {

    int N;
    scanf("%d", &N);

    int value = N;
    for(int i = 1; set.size() != 10; ++i) {
      if(N == 0) {
        printf("Case #%d: INSOMNIA\n", test);
        break;
      }
      value = i * N;
      //printf("Current value: %d\n", value);
      addDigitsToSet(value);
      if(set.size() == 10) {
        printf("Case #%d: %d\n", test, value);
        set.clear();
        break;
      }
    }

  }

  return 0;
}

void addDigitsToSet(int number) {
  int digit;
  while(number > 0) {
    digit = number % 10;
    set.insert(digit);
    number /= 10;
  }
}
