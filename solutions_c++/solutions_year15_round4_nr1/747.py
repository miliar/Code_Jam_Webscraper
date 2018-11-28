#include <iostream>
#include <algorithm>

using namespace std;



char T[109][109];
int CI[109][2];
int RI[109][2];

void solve()
{
  int R, C;
  cin >> R >> C;
  for (int i = 0; i < R; ++i)
    RI[i][0] = RI[i][1] = -1;
  for (int i = 0; i < C; ++i)
    CI[i][0] = CI[i][1] = -1;
  cin.ignore(1, '\n');
  for (int i = 0; i < R; ++i)
  {
    char c;
    for (int j = 0; j < C; ++j)
    {
      c = cin.get();
      T[i][j] = c;
      if (c != '.')
      {
	if (CI[j][0] == -1)
	  CI[j][0] = i;
	CI[j][1] = i;
	if (RI[i][0] == -1)
	  RI[i][0] = j;
	RI[i][1] = j;
      }
    }
    c = cin.get();
  }
  int ans = 0;
  for  (int i = 0; i < R; ++i)
  {
    for (int j = 0; j < C; ++j)
    {
      switch (T[i][j])
      {
	case '>':
	  if (RI[i][1] == j)
	  {
	    if (RI[i][0] == j && CI[j][0] == i && CI[j][1] == i)
	    {
	      cout << "IMPOSSIBLE";
		return;
	    }
	    ++ans;
	  }
	  break;
	case '<':
	  if (RI[i][0] == j)
	  {
	    if (RI[i][1] == j && CI[j][0] == i && CI[j][1] == i)
	    {
	      cout << "IMPOSSIBLE";
		return;
	    }
	    ++ans;
	  }
	  break;
	case '^':
	  if (CI[j][0] == i)
	  {
	    if (CI[j][1] == i && RI[i][0] == j && RI[i][1] == j)
	    {
	      cout << "IMPOSSIBLE";
		return;
	    }
	    ++ans;
	  }
	  break;
	case 'v':
	  if (CI[j][1] == i)
	  {
	    if (CI[j][0] == i && RI[i][0] == j && RI[i][1] == j)
	    {
	      cout << "IMPOSSIBLE";
		return;
	    }
	    ++ans;
	  }
	  break;
      }
    }
  }
  cout << ans;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
  {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
  return 0;
}
