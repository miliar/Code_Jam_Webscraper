#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 1010;

int n;

int normal_play(int offset, vector<double> a, vector<double> b)
{
  int score = 0;
  int l = 0, r = n - offset - 1;
  for (int i = n - 1; i >= offset; --i)
  {
    if (b[r] > a[i])
    {
      --r;
    }
    else
    {
      ++l;
      ++score;
    }
  }
  return score;
}

int main()
{
  int n_cases;
  scanf("%d", &n_cases);
  for (int T = 0; T < n_cases; ++T)
  {
    printf("Case #%d: ", T + 1);
    scanf("%d", &n);

    vector<double> a, b;
    a.resize(n);
    for (int i = 0; i < n; ++i) scanf("%lf", &a[i]);
    b.resize(n);
    for (int i = 0; i < n; ++i) scanf("%lf", &b[i]);

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int normal_score = normal_play(0, a, b);
    int max_score = normal_score;

    {
      int score = 0;
      int l = 0, r = n - 1;
      for (int i = 0; i < n; ++i)
      {
        if (a[i] > b[l])
        {
          ++l;
          ++score;
        }
        else
        {
          --r;
        }
      }
      if (score > max_score) max_score = score;
    }
    printf("%d %d\n", max_score, normal_score);
  }
  return 0;
}
