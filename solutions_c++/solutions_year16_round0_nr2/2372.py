#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int test;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  {
    cerr << "Running test " << iTest << "..." << endl;
    string s;
    cin >> s;
    char cur = s[0];
    int cnt = 0;
    for (int i = 1; i < s.size(); i++)
      if (s[i] != cur)
      {
        cur = s[i];
        cnt++;
      }
    cout << "Case #" << iTest << ": " << cnt + (cur == '-') << endl;
  }
}