#include <bits/stdc++.h>

using namespace std;

int main()
{
  //freopen("input.in", "r", stdin);
  freopen("D-small-attempt0.in", "r", stdin);
  freopen("myfile.out", "w", stdout);
  int tsts;
  cin >> tsts;
  for (int tno = 1; tno <= tsts; tno++)
  {
    int n;
    double x;
    vector<double> a, b;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
      cin >> x;
      a.push_back(x);
    }
    for (int i = 0; i < n; i++)
    {
      cin >> x;
      b.push_back(x);
    }
    cout << "Case #" << tno << ": ";
    int mini = n;
    int maxi = 0;
    sort(b.begin(), b.end());
    do
    {
      int cnt = 0;
      for (int i = 0; i < n; i++)
      {
        if (a[i] > b[i])
        {
          cnt++;
        }
      }
      if (cnt > maxi) maxi = cnt;
      if (cnt < mini) mini = cnt;
    } while (next_permutation(b.begin(), b.end()));
    cout << maxi << " " << mini;
    cout << endl;
  }
  return 0;
}



