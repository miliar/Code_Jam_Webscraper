#include <iostream>
#include <set>
#include <sstream>
using namespace std;

void SolveACase(int number)
{
  int ans;
  cin >> ans;
  --ans;
  set<int> row1;
  for (int i = 0; i != 16; ++i)
  {
    int v;
    cin >> v;
    if (i >= 4*ans && i < 4*(ans+1))
    {
      row1.insert(v);
    }
  }
  
  cin >> ans;
  --ans;
  set<int> row2;
  for(int i = 0; i != 16; ++i)
  {
    int v;
    cin >> v;
    if (i >= 4*ans && i < 4*(ans+1))
    {
      row2.insert(v);
    }
  }
  
  set<int> intersection;
  for (set<int>::iterator i = row1.begin(); i != row1.end(); ++i)
  {
    if (row2.count(*i) > 0)
      intersection.insert(*i);
  }

  string result;
  if (intersection.empty())
    result = "Volunteer cheated!";
  else if (intersection.size() > 1)
    result = "Bad magician!";
  else
  {
    //result = to_string(*intersection.begin());
    ostringstream convert;

    convert << *intersection.begin();

    result = convert.str();
  }
  cout << "Case #" << number << ": " << result;
}


int main (int argc, char* args[])
{
  int T;
  cin >> T;
  
  for (int i = 0; i != T; ++i)
  {
    SolveACase(i + 1);
    if (i < T-1)
      cout << "\n";
  }
  return 0;
}
