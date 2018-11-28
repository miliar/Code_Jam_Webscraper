#include <bits/stdc++.h>

using namespace std;

int main()
{
  freopen("A-small-attempt1.in", "r", stdin);
  freopen("myfile.out", "w", stdout);
  int tsts;
  cin >> tsts;
  for (int _tno = 1; _tno <= tsts; _tno++)
  {
    int x, a;
    vector<int> first, second;
    cin >> a;
    for (int i = 0; i < 4; i++)
    {
      for (int j = 0; j < 4; j++)
      {
        cin >> x;
        if (i + 1 == a)
        {
          first.push_back(x);
        }
      }
    }
    cin >> a;
    for (int i =0;i < 4; i++)
    {
      for (int j = 0; j < 4; j++)
      {
        cin >> x;
        if (i + 1 == a)
        {
          second.push_back(x);
        }
      }
    }
    int cnt = 0, ret = -1;
    for (int i =0; i < 4; i++)
    {
      bool found = false;
      for (int j  =0; j < 4; j++)
      {
        if (first[i] == second[j])
        {
          found = true;
          ret = first[i];
        }
      }
      if (found) cnt++;
    }
    cout << "Case #" << _tno << ": ";
    if (cnt == 0)
    {
      cout << "Volunteer cheated!";
    }
    else if (cnt == 1)
    {
      cout << ret;
    }
    else
    {
      cout << "Bad magician!";
    }
    cout << endl;
  }
  return 0;
}
