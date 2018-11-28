#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
int card[2][4][4];
int select[2];
void solve(){
  vector<int> ans;
  for( int i  = 0; i < 4; ++i )
    {
      for( int j = 0; j < 4; ++j )
	{
	  if( card[0][select[0]-1][i] == card[1][select[1]-1][j] )
	    {
	      ans.push_back(card[0][select[0]-1][i]);
	    }
	}      
    }
  if( ans.size() == 1)
    {
    cout << ans[0] << endl;
    }
  else if( ans.size() >= 2 )
    {
      cout << "Bad magician!" << endl;
    }
  else if( ans.size() == 0 )
    {
      cout << "Volunteer cheated!" << endl;
    }
  else
    {
      cerr << "not ans" << endl;
    }
}
int main(){
  int t;
  cin >> t;
  for( int i = 0 ; i < t; ++i )
    {
      cout << "Case #" << i+1 << ": ";
      for( int j = 0 ; j < 2; ++j )
	{
	  cin >> select[j];
	  for( int row = 0; row < 4; ++row )
	    {
	      for( int col = 0; col < 4; ++col )
		{
		  cin >> card[j][row][col];
		}
	    }
	}
      solve();
    }
  return 0;
}
