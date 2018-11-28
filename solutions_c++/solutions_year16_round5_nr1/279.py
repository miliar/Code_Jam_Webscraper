#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

void main2()
{
  string s;
  cin >> s;
  int score = 0;
  while (true)
  {
    bool done = true;
    string s2;
    int i = 0;
    while (i < (int)s.size())
    {
      if (i+1 < (int)s.size() && s[i] == s[i+1])
      {
        done = false;
        score += 10;
        i += 2;
      }
      else
      {
        s2 += s[i];
        i++;
      }
    }
    
    s = s2;
    
    if (done)
      break;
  }
  
  score += (s.size() / 2) * 5;
  cout << score << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ": ";
    main2();
  }
}
