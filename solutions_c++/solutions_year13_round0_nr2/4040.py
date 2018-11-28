#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

bool okay(const vector<vector<int> >& tab, int i, int j)
{
  bool ok = true;
  for(int x = 0; x < tab.size(); ++x)
    {
      if(tab[x][j] <= tab[i][j])
	{continue;}
      else
	{
	  ok = false;
	  break;
	}
    }
  if(ok)
    {return ok;}
  ok = true;
  for(int y = 0; y < tab[0].size(); ++y)
    {
      if(tab[i][y] <= tab[i][j])
	{continue;}
      else
	{
	  ok = false;
	  break;
	}
    }
  return ok;
}

bool check(const vector<vector<int> >& tab, const set<int>& height)
{
  for(int h = 100; h > 0; --h)
    {
      if(!height.count(h))
	{continue;}
      for(int i = 0; i < tab.size(); ++i)
	{
	  for(int j = 0; j < tab[0].size(); ++j)
	    {
	      if(tab[i][j] == h)
		{
		  if(!okay(tab, i, j))
		    {return false;}
		}
	    }
	}
    }
  return true;
}

int main()
{
  int T;
  cin >> T;
  for(int i = 0; i < T; ++i)
    {
      int n, m;
      cin >> n >> m;
      vector<vector<int> > tab;
      set<int> height;
      for(int j = 0;j < n; ++j)
	{
	  vector<int> temp;
	  for(int k = 0; k < m; ++k)
	    {
	      int t;
	      cin >> t;
	      height.insert(t);
	      temp.push_back(t);
	    }
	  tab.push_back(temp);
	}
      bool ans = check(tab, height);
      cout << "Case #" << i+1 << ": ";
      if(ans)
	{cout << "YES" << endl;}
      else
	{cout << "NO" << endl;}
    }
}
