#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

int V[] = {1, 4, 9, 121, 484};

int main()
{
  freopen("fairandsquare.in", "r", stdin);
  freopen("fairandsquare.out", "w", stdout);
  
  int T;
  scanf("%d", &T);
  
  for (int i = 0; i < T; i++) {
    int a, b;
    scanf("%d %d", &a, &b);
    int poz_a, poz_b;
    for (poz_a = 0; poz_a < 5 && V[poz_a] < a; poz_a++);
    for (poz_b = 0; poz_b < 5 && V[poz_b] <= b; poz_b++);
    printf("Case #%d: %d\n", i + 1, poz_b - poz_a);
  }
  
  /*for (int i = 1; i <= 10000000; i++) {
    int sq = sqrt(i);
    if (sq * sq != i)
      continue;
    vector<int> digits;
    int x = i;
    while (x)
      digits.push_back(x % 10), x /= 10;
    bool pal = true;
    for (int j = 0, k = digits.size() - 1; pal && j < k; j++, k--)
      if (digits[j] != digits[k])
	pal = false;
    x = sq;
    digits.clear();
    while (x)
      digits.push_back(x % 10), x /= 10;
    for (int j = 0, k = digits.size() - 1; pal && j < k; j++, k--)
      if (digits[j] != digits[k])
	pal = false;
    if (pal)
      printf("%d\n", i);
  }*/
  
  return 0;
}
