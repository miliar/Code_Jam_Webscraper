//In the name of God
#include <algorithm>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int tests, A, B, tmp;
set<int> s, t;
vector<int> ans;

int main ()
{
  cin >> tests ;
  for(int ii = 1 ; ii <= tests ; ii++)
    {
      s.clear();
      t.clear();
      ans.resize(0);
      cin >> A ;
      A --;
      for(int i = 0 ; i < 4 ; i++)
	for(int j = 0 ; j < 4 ; j++)
	  {
	    cin >> tmp ;
	    if(i == A)
	      s.insert(tmp);
	  }
      cin >> B ;
      B --;
      for(int i = 0 ; i < 4 ; i++)
	for(int j = 0 ; j < 4 ; j++)
	  {
	    cin >> tmp ;
	    if(i == B)
	      t.insert(tmp);
	  }
      for(int i = 1 ; i <= 16 ; i++)
	if(s.find(i) != s.end() && t.find(i) != t.end())
	  ans.push_back(i);
      cout << "Case #" << ii << ": " ; 
      if(ans.size() > 1)
	cout << "Bad magician!" << endl ;
      else if(ans.size() == 0)
	cout << "Volunteer cheated!" << endl ;
      else
	cout << ans[0] << endl ;
    }
}
