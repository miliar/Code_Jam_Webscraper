#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

char input[1005];

int main()
{
  int T = 0;
  scanf("%d", &T);
  for(int Case = 1; Case <= T; ++Case)
  {
    int Smax = 0;
    scanf("%d%s", &Smax, input);
    string audiences(input);
    int sum = 0, ans = 0;
    for(int i = 0; i < (int)audiences.size(); ++i)
    {
      if(sum < i)
      {
        ans += i - sum;
        sum += i - sum;
      }
      sum += audiences[i] - '0';
    }
    printf("Case #%d: %d\n", Case, ans);
  }
  return 0;
}
