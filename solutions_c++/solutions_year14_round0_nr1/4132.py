#include <bits/stdc++.h>
using namespace std;
int G[5][5];
unordered_set <int> store;

int main()
{
      ios::sync_with_stdio (false);
      int testCases;
      cin >> testCases;
      for (int testNumber = 1; testNumber <= testCases; ++testNumber)
      {
	    store.clear();
	    cout << "Case #" << testNumber << ": ";
	    int ans, firstAns, secAns, found = 0;
	    cin >> firstAns;
	    for (int i = 1; i <= 4; ++i)
		  for (int j = 1; j <= 4; ++j)
			cin >> G[i][j];
	    for (int i = 1; i <= 4; ++i)
		  store.insert(G[firstAns][i]);
	    cin >> secAns;
	    for (int i = 1; i <= 4; ++i)
		  for (int j = 1; j <= 4; ++j)
			cin >> G[i][j];
	    for (int i = 1; i <= 4; ++i)
		  if (store.find(G[secAns][i]) != store.end())
		  {
			found ++;
			ans = G[secAns][i];
		  }
	    if (found > 1)
		  cout << "Bad magician!\n";
	    else if (found == 1)
		  cout << ans << endl;
	    else
		  cout << "Volunteer cheated!\n";
      }
      return 0;
}

