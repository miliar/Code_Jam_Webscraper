#include <stdio.h>
#include<iostream>
#include<cstdlib>
#include<climits>

using namespace std;

int solve(string S)
{
  // find first differing bit
  int steps = 0;
  for (int i = 1; i < S.length(); i++)
    {
      if (S[i] != S[i-1])
        {
          steps++;
        }
    }
  if (S[S.length()-1] == '-') return steps+1;
  return steps;
}

int main()
{
  int T = 0;
  cin >> T;

  for (int i = 0; i < T; i++)
    {
      string S;
      cin >> S;
      cout << "Case #" << i+1 << ": " << solve(S) << endl;
    }
  return 0;
}
