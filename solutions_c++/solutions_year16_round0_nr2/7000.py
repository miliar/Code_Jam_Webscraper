#include <iostream>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <iomanip>
#include <sstream>

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

using namespace std;
struct status{
  string str;
  int count;

};

status change(status a, int index)
{
  a.count++;
  for(int low = 0, high = index; low < high; low++, high--)
  {
    swap(a.str[low], a.str[high]);
  }

  for(int i = 0; i <= index; i++)
  {
    if(a.str[i] == '+')
      a.str[i] = '-';
    else a.str[i] = '+';
  }
  return a;
}

int main()
{
  int T;
  string str;
  cin >> T;
  for(int t = 1; t <= T; t++)
  {
  	cout << "Case #"<<t << ": ";
  	cin >> str;
    string res(str.length(), '+');
 
    long long count = 0;

    queue<status> Q;
    set<string> LIST;

    status a;
    a.str = str;
    a.count = 0;
    Q.push(a);
    while(true)
    {
      status temp = Q.front(); 
      Q.pop();
      if (temp.str == res)
      {
        cout << temp.count << endl;
        break;
      }
      if(LIST.find(temp.str) != LIST.end() )
        continue;

      LIST.insert(temp.str);
      for(int i = 0; i <str.length(); i++)
      {
        status temp2 = change(temp, i);

        Q.push(temp2);
      }
    }

  }


  return 0;
}