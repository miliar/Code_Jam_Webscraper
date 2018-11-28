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


using namespace std;



int main()
{
  int tot;
  cin >> tot;
  for(int i = 0; i < tot; ++i)
    {
      int N, X;
      cin >> N >> X;
      vector<int> data;
      for(int j = 0; j < N; ++j)
	{
	  int temp;
	  cin >> temp;
	  data.push_back(temp);
	}
      sort(data.begin(), data.end());
      vector<int> used(N, 0);
      int cnt=0;
      for(int j = 0; j < N; ++j)
	{
	  if(used[j])
	    {continue;}
	  int val1=data[j];
	  used[j]=1;
	  for(int k = N-1;k>=0; --k)
	    {
	      if(used[k])
		{continue;}
	      if(val1+data[k]<=X)
		{
		  used[k]=1;
		  break;
		}
	    } 
	  ++cnt;
	}
      cout << "Case #" << i+1 << ": " << cnt;
      cout << endl;
    }
}
