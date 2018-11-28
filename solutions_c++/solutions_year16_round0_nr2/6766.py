#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

enum STATE
{
  NEUTRAL = 0,
  PLUS = 1,
  MINUS = 2
};



int main()
{
#ifdef MY_DEBUG
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
#endif

  int  t = 0;
  cin >> t;
  for(int i = 1; i <= t; i++)
  {
    string s;
    cin >> s;
    int last_state = NEUTRAL;
    int ans = 0;
    for(int j = 0; j  < s.size(); j++)
    {
      if(s[j]=='-')
      {
        if(last_state==NEUTRAL)
          ans++;
        else if(last_state==PLUS)
          ans+=2;
        last_state = MINUS;
      }
      else if(s[j]=='+')
      {
        last_state = PLUS;
      }
    }

    cout<< "Case #" <<i << ": "<< ans << endl;

  }

  return 0;
}
