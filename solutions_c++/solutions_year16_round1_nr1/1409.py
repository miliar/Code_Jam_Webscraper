#include <iostream>
#include <string>

using namespace std;

string get_best_string(string str)
{
  string res;
  res.push_back(str.at(0));
  for (int i = 1; i < str.length(); ++i)
    {
      if (str.at(i) >= res.at(0))
	res.insert(0, 1, str.at(i));
      else
	res.push_back(str.at(i));
    }
  return res;
}


int main()
{

  int T;
  cin >> T;
  for (int t = 0; t < T; ++t)
  {
    string s;
    cin >> s;
    cout << "Case #" << (t+1) << ": "
	 << get_best_string(s) << endl;
  }

}
