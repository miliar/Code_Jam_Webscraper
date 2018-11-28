#include <stdio.h>
#include<iostream>
#include<cstdlib>
#include<climits>

using namespace std;

int solve(string S)
{
  std::string ans(1, S[0]);
  for (int i = 1; i < S.length(); i++)
    {
      if (S[i] >= ans[0])
        {
          ans.insert(0, 1, S[i]);
        }
      else
        {
          ans.append(1, S[i]);
        }
    }
  cout << ans << endl;
}

int main()
{
  int T = 0;
  cin >> T;

  for (int i = 0; i < T; i++)
    {
      string S;
      cin >> S;
      cout << "Case #" << i+1 << ": " ;
      solve(S);
    }
  return 0;
}
