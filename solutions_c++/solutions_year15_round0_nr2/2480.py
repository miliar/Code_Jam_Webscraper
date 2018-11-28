#include <cstdio>
#include <iostream>

#define INF 1000000000

using namespace std;

int count_minutes(int number_of_pancakes, int maximum_pancakes) {
  if (number_of_pancakes == 0)
    return 0;
  if (maximum_pancakes >= number_of_pancakes)
    return 0;

  int result = number_of_pancakes - maximum_pancakes;

  if (result % maximum_pancakes == 0)
    return result / maximum_pancakes;
  return result / maximum_pancakes + 1;
}


int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int nTest;
  scanf("%d", &nTest);

  for (int test = 0; test < nTest; test++) {
    int d;
    int p[1111];
    scanf("%d", &d);
    for (int i = 0; i < d; i++)
      scanf("%d", &p[i]);

    int result = INF;
    for (int maximum_pancakes = 1; maximum_pancakes <= 1000; maximum_pancakes++) {
      int curr_result = maximum_pancakes;
      if (curr_result > result) continue;

      for (int i = 0; i < d; i++)
        curr_result += count_minutes(p[i], maximum_pancakes);

      if (curr_result < result)
        result = curr_result;
    }

    printf("Case #%d: %d\n", test + 1, result);
  }

  return 0;
}
