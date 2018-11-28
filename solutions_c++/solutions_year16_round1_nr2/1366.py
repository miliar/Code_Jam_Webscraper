#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;
/*
bool is_valid(int **A, vector<int> v, int m)
{
  if (m == v.size())
    return false;
  return true;
}

void process_vectors(vector<vector<int> > v)
{
  int A[v.size()][v.size()];
  int m = 0, n = 0;
  for (int i = 0; i < v.size(); ++i)
    {
      if (is_valid(v[i], A, m))
      {
	for (int j = 0; j < v.size(); ++j)
	  {
	    A[m][j] = v[i][j];
	  }
	++m;
      }
      else
      {
	for (int j = 0; j < v.size(); ++j)
	  {
	    A[j][n] = v[i][j];
	  }
	++n;
      }
    }
  if (m < v.size())
    {
      for (int i = 0; i < v.size(); ++i)
	{
	  cout << A[m][i] << " ";
	}
      cout << endl;
    }
  else
    {
      for (int i = 0; i < v.size(); ++i)
	{
	  cout << A[i][n] << " ";
	}
      cout << endl;
    }
}
*/
void easy_soln(vector<vector<int> > v)
{
  map<int,bool> m;
  for (int i = 0; i < v.size(); ++i)
    {
      for (int j = 0; j < v[i].size(); ++j)
	{
	  if(m.find(v[i][j]) == m.end())
	    m.insert(make_pair(v[i][j], true));
	  else
	    m.erase(m.find(v[i][j]));
	}
    }
  for (map<int, bool>::const_iterator it = m.begin();
       it != m.end();
       ++it)
    {
      cout << (*it).first << " ";
    }
  cout << endl;
}

int main()
{

  int T;
  cin >> T;
  for (int t = 0; t < T; ++t)
  {
    int N;
    cin >> N;
    vector<vector<int> > v;
    for (int i = 0; i < 2*N-1; ++i)
      {
	vector<int> u;
	v.push_back(u);
	for (int j = 0; j < N; ++j)
	  {
	    int temp;
	    cin >> temp;
	    v[i].push_back(temp);
	  }
      }
    cout << "Case #" << (t+1) << ": ";
    easy_soln(v);
  }

}
