#include <algorithm>
#include <cstdint>
#include <deque>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

string lastWord(const string& S)
{
  std::deque<char> lastWord;
  lastWord.push_back(S[0]);

  for (int i = 1; i < S.size(); ++i)
  {
    if (lastWord.front() > S[i])
    {
      lastWord.push_back(S[i]);
    }
    else
    {
      lastWord.push_front(S[i]);
    }
  }

  return std::string(lastWord.cbegin(), lastWord.cend());
}

int main()
{
  int T;
  cin >> T;

  for (int i = 0; i < T; ++i)
  {
    string S;
    cin >> S;

    cout << "Case #" << (i + 1) << ": " << lastWord(S) << endl;
  }
}