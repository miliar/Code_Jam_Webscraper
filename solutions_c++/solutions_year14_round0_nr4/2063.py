#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  freopen("D-large.in", "r", stdin);
  freopen("D-result-large.txt", "w", stdout);
  int T;
  scanf("%d", &T);

  for (int i = 0; i < T; ++i)
  {
    int n;
    scanf("%d", &n);
    vector<double> p1;
    vector<double> p2;

    p1.reserve(n);
    p2.reserve(n);

    for (int j = 0; j < n; ++j)
    {
      double d;
      scanf("%lf", &d);
      p1.push_back(d);
    }
    for (int j = 0; j < n; ++j)
    {
      double d;
      scanf("%lf", &d);
      p2.push_back(d);
    }

    sort(p1.begin(), p1.end());
    sort(p2.begin(), p2.end());

    int war_score = 0;

    vector<double> p2c;
    p2c.assign(p2.begin(), p2.end());

    for (int  i= n - 1 ;i >= 0; --i)
    {
      if (p1[i] > p2c.back())
      {
        ++war_score;
        p2c.erase(p2c.begin());
      }
      else
        p2c.pop_back();
    }

    int dwar_score = 0;

    auto it = p1.begin();
    auto it2 = p2.begin();

    while (it != p1.end())
    {
      if (*it > * it2)
      {
        dwar_score++;
        it = p1.erase(it);
        it2 = p2.erase(it2);
      }
      else
      {
        it = p1.erase(it);
        p2.pop_back();
      }
    }

    printf("Case #%d: ", i + 1);

    printf("%d %d", dwar_score, war_score);


    printf("\n");
  }

  fclose(stdin);
  fclose(stdout);

  return 0;
}
