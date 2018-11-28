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

vector<int> digits(int n)
{
  vector<int> ret;
  while(n > 0)
  {
    ret.push_back(n % 10);
    n /= 10;
  }
  //reverse(ret.begin(), ret.end());
  return ret;
}

//lsd first
void add(vector<int> a, vector<int> &b)
{
  a.resize(max(b.size(), a.size()), 0);
  b.resize(max(b.size(), a.size()), 0);
  bool carry = 0;
  for(int i = 0; i < b.size(); i++)
  {
    b[i] += a[i] + carry;
    carry = b[i] >= 10;
    b[i] %= 10;
  }
  if(carry)
  {
    b.push_back(1);
  }
}

int main()
{
  int n;
  cin >> n;
  const set<int> done = {0,1,2,3,4,5,6,7,8,9};
  for(int i = 1; i <= n; i++)
  {
    //solving
    int num, t = 0;
    //num = i;
    cin >> num;
    if(num == 0)
    {
      cout << "Case #" << i << ": " << "INSOMNIA" << endl;
      continue;
    }
    vector<int> d = digits(num), current = {0};
    set<int> seen;
    while(seen != done)
    {
      t++;
      add(d, current);
      for(int j : current)
      {
        //cerr << j << " ";
        seen.insert(j);
      }
      //cerr << endl;
    }
    //cerr << endl;
    //cerr << endl;

    cout << "Case #" << i << ": ";
    reverse(current.begin(), current.end());
    for(int j : current)
    {
      cout << j;
    }
    cout << endl;

    //output
  }
  return 0;
}
