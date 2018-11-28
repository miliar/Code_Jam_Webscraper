#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <utility>

using namespace std;

typedef unsigned long long longint;

void solve()
{
  longint n, p;
  cin >> n >> p;
  longint tmp_p = p;
  p--;
  
  longint k = (1 << n);


  vector < int > bin(0);
  for (int i = 0; i < n; ++i)
  {
    bin.push_back(p % 2);
    p /= 2;
  }
  reverse(bin.begin(), bin.end());

  int t = 1;
  int col = 0;
  for (int i = 0; i < n; ++i)
  {
    if (bin[i] == 0)
      t = 0;
    col += t;
  }
  longint resA;
  resA = (1 << (col + 1)) - 2;
  if (resA >= k)
    resA = k - 1;
    

  cout << resA << " ";
  cerr << resA << " ";


  t = 0;
  for (int i = n - 1; i >= 0; i--)
  {
    if (bin[i] == 0)
      t = 1;
    bin[i] = t;
  }

  longint resB = 0;
  reverse(bin.begin(), bin.end());
  for (int i = 0; i < n; ++i)
  {
    resB += bin[i] * (1 << i);
  }

  p = tmp_p;
  longint r = 1;
  for (longint i = 1, t = k; t > p;)
  {
    t -= (1 << (n - i));
//    cerr << "t: " << t << endl;
    i++;
    r = i;
  }
  resB = k - (1 << (r - 1));

  cout << resB;
  cerr << resB << endl;
  
  

  
  /*
  vector < long long > perm(0);
  for (int i = 0; i < k; ++i)
  {
    perm.push_back(i);
  }

  vector < long long > best(k, k);
  vector < long long > worst(k, 0);

  do
  {
    vector < pair < string, int > > rate(k);
    for (int i = 0; i < k; ++i)
      rate[i] = make_pair("", perm[i]);

    for (int step = 0; step < n; ++step)
    {
      for (int i = 0; i < rate.size(); i += 2)
      {
        if (rate[i].second > rate[i + 1].second)
          swap(rate[i], rate[i + 1]);
        rate[i].first += "A";
        rate[i + 1].first += "B";
      }
      sort(rate.begin(), rate.end());
    }

    for (int i = 0; i < rate.size(); ++i)
    {
      best[rate[i].second] = min(best[rate[i].second], (long long)i);
      worst[rate[i].second] = max(worst[rate[i].second], (long long)i);
    }
  }
  while (next_permutation(perm.begin(), perm.end()));

  for (int i = 0; i < k; ++i)
  {
    cerr << i << " " << best[i] << " " << worst[i] << endl;
    cout << i << " " << best[i] << " " << worst[i] << endl;
  }
  */
}

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int tests_count;
  scanf("%d\n", &tests_count);
  for (int test = 0; test < tests_count; ++test)
  {
    cout << "Case #" << test + 1 << ": ";
    solve();
    cout << endl;
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}

