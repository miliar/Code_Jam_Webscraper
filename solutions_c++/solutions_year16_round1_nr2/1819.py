
#include <iostream>
#include <cassert>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <algorithm>


using namespace std;

template<class T>
class compare_nth
{
  int n;
  public:
    compare_nth(int k) : n(k) {}
    bool operator()(vector<T> a, vector<T> b) 
    { 
      for (int k = n; k < a.size(); k++)
      {
        if (a[k] < b[k])
          return true;
        if (a[k] > b[k])
          return false;
      }
      return false;
    }
};

void processCase(int c)
{
  int N;
  cin >> N;
  
  vector<vector<int>> lists;
  lists.resize(2*N-1);
  for (int idx = 0; idx < 2*N-1; idx++)
  {
    for (int k = 0; k < N; k++)
    {
      int h;
      cin >> h;
      lists[idx].push_back(h);
    }
  }
  
  int missing_idx = N-1;
  vector<vector<int> >::iterator current = lists.begin();
  for (int idx = 0; idx < N-1; idx++)
  {
    partial_sort(current,current+2, lists.end(),compare_nth<int>(idx));
    
    if ((*current)[idx] == (*(current+1))[idx])
    {
      current += 2;
    }
    else
    {
      current += 1;
      missing_idx = idx;
    }
  }
  /*
  cerr << "Sorted Grid: " << endl;
  for (int idx = 0; idx < 2*N-1; idx++)
  {
    for (int k = 0; k < N; k++)
      cerr << "\t" << lists[idx][k];
    cerr << endl;
    if ((idx%2 == 0) and (idx/2 == missing_idx))
      cerr << "MISSING" << endl;
  }*/
  

  vector<int> missing;  
  //missing one's pair is at 2*missing_idx
  for (int idx = 0; idx < N; idx++)
  {
    int listidx = 2*idx;
    if (idx == missing_idx)
    {
      missing.push_back(lists[listidx][missing_idx]);
    } else
    {
      if (idx > missing_idx)
      {
        listidx--;
      }
      
      //cerr << "Element " << idx << " either " << lists[listidx][missing_idx] << " or " << lists[listidx+1][missing_idx] << "(not " << lists[2*missing_idx][idx]<< ")" << endl;
      if (lists[listidx][missing_idx] == lists[2*missing_idx][idx])
      {
        missing.push_back(lists[listidx+1][missing_idx]);
      }
      else
      {
        missing.push_back(lists[listidx][missing_idx]);
      }
    }
  }


  cout << "Case #" << c << ":";
  for (int idx = 0; idx < missing.size(); idx++)
  {
    cout << " " << missing[idx];
  }
  cout << endl;

}


int main()
{
  int numcases;
  cin >> numcases;
  
  for (int c = 0; c < numcases; c++)
    processCase(c+1);
}

