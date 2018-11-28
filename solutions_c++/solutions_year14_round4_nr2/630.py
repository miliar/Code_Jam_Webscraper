#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <iomanip>
#include <cmath>
#include <utility>
#include <queue>
#include <stack>

typedef long long LL;
using namespace std;

LL min(LL v1, LL v2)
{
  return v1<v2?v1:v2;
}

LL solve(const vector<LL>& vec, vector<LL>& tab, vector<int> visited, int i)
{
  if(tab[i]!=-1)
    {return tab[i];}
  if(i==vec.size()-1)
    {
      tab[i]=0;
      return tab[i];
    }
  LL minVal=1e10;
  LL pos=-1;
  for(int j = 0; j < vec.size(); ++j)
    {
      if(visited[j])
	{continue;}
      else
	{
	  if(minVal>vec[j])
	    {
	      minVal=vec[j];
	      pos=j;
	    }
	}
    }
  LL cnt=0;
  for(int j = 0; j < vec.size(); ++j)
    {
      if(vec[j]==minVal)
	{break;}
      if(vec[j]>minVal)
	{
	  ++cnt;
	}
    }
  visited[pos]=1;
  LL ans=cnt+solve(vec, tab, visited, i+1);
  ans=min(ans, vec.size()-i-1-cnt+solve(vec, tab, visited, i+1));
  tab[i]=ans;
  return tab[i];
}

int main()
{
  int tot;
  cin >> tot;
  for(int i = 0; i < tot; ++i)
    {
      cerr << i << endl;
      int N;
      cin >> N;
      vector<LL> vec;
      for(int j = 0; j < N; ++j)
	{
	  LL temp;
	  cin >> temp;
	  if(temp>1e9+1000)
	    {cerr << "ERROR" << endl;}
	  vec.push_back(temp);
	}
      vector<LL> tab(N, -1);
      vector<int> visited(N,0);
      LL ans=solve(vec, tab, visited, 0);
      cout << "Case #" << i+1 << ": " << ans;
      cout << endl;
    }
}
