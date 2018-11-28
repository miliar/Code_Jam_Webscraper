#include <cstdio>
#include <algorithm>
using namespace std;

int input[1001];

int main()
{
  int T = 0;
  scanf("%d", &T);
  for(int Case = 1; Case <= T; ++Case)
  {
    int n = 0;
    scanf("%d", &n);
    for(int i = 0; i < n; ++i)
      scanf("%d", &input[i]);
    int ans_a = 0;
    for(int i = 1; i < n; ++i)
      if(input[i] < input[i - 1])
        ans_a += input[i - 1] - input[i];
    int ans_b = 0;
    int speed = 0;
    for(int i = 1; i < n; ++i)
    {
      int tmp = input[i - 1] - input[i];
      if(tmp > speed)
        speed = tmp;
    }
    for(int i = 1; i < n; ++i)
      ans_b += (input[i - 1] > speed) ? speed : input[i - 1];
    printf("Case #%d: %d %d\n", Case, ans_a, ans_b);
  }
  return 0;
}
