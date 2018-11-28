#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
#include <array>

using namespace std;

void testcase()
{
  string s;
  
  cin >> s;
  string res;
  res.append(1, s[0]);
  for (int i = 1; i < s.size(); ++i)
  {
    if (s[i] >= res[0])
    {
      res.insert(0, 1, s[i]);
    }
    else
      res.append(1, s[i]);
  }
  cout << res << endl;
} 

int main()
{
  int n;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
    cout << "Case #" << i + 1 << ": ";
		testcase();
	}
	
	return 0;
}