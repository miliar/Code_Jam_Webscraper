#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iomanip>
#include <queue>

using namespace std;

int main()
{
  int n;
  cin >> n;

  string s;
  getline(cin,s);
  for(int i = 1; i <= n; i++)
  {
    //solving
    getline(cin,s);
    reverse(s.begin(), s.end());
    char last = '+';
    int num = 0;
    for(char c : s)
    {
      if (c != last)
      {
        last = c;
        num++;
      }
    }

    cout << "Case #" << i << ": " << num << endl;
    //output
  }
  return 0;
}
