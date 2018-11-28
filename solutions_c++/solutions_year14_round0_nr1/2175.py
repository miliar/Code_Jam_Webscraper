#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

vector<int> readP()
{
  vector<int> p;
  int a;
  cin >> a;
  for (int j = 1; j <= 4; ++j)
  {
    for (int k = 0; k < 4; ++k)
    {
      int c;
      cin >> c;
      if (j == a)
	p.push_back(c);
    }
  }
  return p;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
  {
    vector<int> p1 = readP();
    vector<int> p2 = readP();
    sort(p1.begin(), p1.end());
    sort(p2.begin(), p2.end());
    vector<int> r;
    set_intersection(p1.begin(), p1.end(), p2.begin(), p2.end(), back_insert_iterator<vector<int> >(r));
    cout << "Case #" << i << ": ";
    if (r.empty())
      cout << "Volunteer cheated!" << endl;
    else if (r.size() > 1)
      cout << "Bad magician!" << endl;
    else
      cout << r.front() << endl;
  }
  return 0;
}
