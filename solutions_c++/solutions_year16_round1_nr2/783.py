#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

int N;
vi result;
int grid[50][50];

void bourrin(vvi tab, int col, int unknown)
{
  for (int i=1; i<N; i++)
  {
    bool ok = false;
    for (auto x : tab)
    {
      bool tmp = true;
      for (int j=0; j<N; j++)
        if (j != unknown && j < col)
          if (grid[i][j] != x[j])
            tmp = false;
      if (tmp)
        ok = true;
    }
    if (!ok)
      return;
  }
  
  if (col == N)
  {
    if (unknown == -1)
      return;
    
    for (int i=0; i<N; i++)
    for (auto x : tab)
    {
      bool tmp = true;
      for (int j=0; j<N; j++)
        if (j != unknown)
          if (grid[i][j] != x[j])
            tmp = false;
      if (tmp)
      {
        for (int j=0; j<N; j++)
          grid[i][j] = x[j];
      }
    }
    
    vi r;
    for (int i=0; i<N; i++)
      r.push_back(grid[i][unknown]);
    result = r;
  }
  
  if (unknown == -1)
    bourrin(tab, col+1, col);
  
  for (auto x : tab)
  {
    if (grid[0][col] == x[0])
    {
      vvi t(tab);
      t.erase(find(t.begin(), t.end(), x));
      for (int i=0; i<N; i++)
        grid[i][col] = x[i];
      bourrin(t, col+1, unknown);
    }
  }
}

void main2()
{
  cin >> N;
  vvi tab;
  for (int i=0; i<2*N-1; i++)
  {
    vi act;
    for (int j=0; j<N; j++)
    {
      int tmp;
      cin >> tmp;
      act.push_back(tmp);
    }
    tab.push_back(act);
  }
  
  int mini = 5000;
  for (auto x : tab)
    mini = min(mini, x[0]);
  
  for (auto x : tab)
  if (x[0] == mini)
  {
    vvi t(tab);
    t.erase(find(t.begin(), t.end(), x));
    for (int i=0; i<N; i++)
      grid[0][i] = x[i];
    bourrin(t, 0, -1);
  }
  
  for (int i=0; i<N; i++)
    cout << " " << result[i];
  cout << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ":";
    main2();
  }
}
