#include <algorithm>
#include <cstdint>
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

void evacuationPlan(const vector<int>& P)
{
  int Ptotal = accumulate(P.cbegin(), P.cend(), 0);

  priority_queue<pair<int, int>> Q;

  for (int k = 0; k < P.size(); ++k)
  {
    Q.push(make_pair(P[k], k));
  }

  if (Ptotal % 2)
  {
    const auto top = Q.top();
    Q.pop();
    Q.push(make_pair(top.first - 1, top.second));

    --Ptotal;

    const char letter = 'A' + top.second;
    cout << letter;

    if (Ptotal)
    {
      cout << " ";
    }
  }

  while (Ptotal)
  {
    const auto top1 = Q.top();
    Q.pop();

    const auto top2 = Q.top();
    Q.pop();

    const char letter1 = 'A' + top1.second;
    const char letter2 = 'A' + top2.second;

    if (top1.first != top2.first)
    {
      Q.push(make_pair(top1.first - 2, top1.second));
      Q.push(top2);

      Ptotal -= 2;
      cout << letter1 << letter1;
    }
    else
    {
      Q.push(make_pair(top1.first - 1, top1.second));
      Q.push(make_pair(top2.first - 1, top2.second));

      Ptotal -= 2;
      cout << letter1 << letter2;
    }

    if (Ptotal)
    {
      cout << " ";
    }
  }
}

int main()
{
  int T;
  cin >> T;

  for (int i = 0; i < T; ++i)
  {
    int N;
    cin >> N;

    vector<int> P(N);

    for (int k = 0; k < N; ++k)
    {
      cin >> P[k];
    }

    cout << "Case #" << (i + 1) << ": ";
    evacuationPlan(P);
    cout << endl;
  }
}