//Program: a
//Author: gary
//Date: 12/04/2014
#include <bits/stdc++.h>
using namespace std;
#define SZ(x) ( (int) (x).size() )
#define mp make_pair
#define pb push_back
#define fi first
#define se second
typedef pair<int, int> i2;
typedef long long ll;
const int INF = 1e9;

string convertInt(int number)
{
  stringstream ss;
  ss << number;
  return ss.str();
}

const int MAX_N = 20;

int T;
int chosen[MAX_N];

string solve()
{
  int row, i, j, x, p;
  memset(chosen, 0, sizeof chosen);

  cin >> row;
  for(i = 1; i <= 4; i++)
  {
    for(j = 1; j <= 4; j++)
    {
      cin >> x;
      if(i == row)
	chosen[x] = 1;
    }
  }

  p = -1;

  cin >> row;
  for(i = 1; i <= 4; i++)
  {
    for(j = 1; j <= 4; j++)
    {
      cin >> x;
      if(i == row && chosen[x])
      {
	if(p == -1)
	  p = x;
	else {
	  p = -2;
	}
      }
    }
  }
  if(p == -2)
    return "Bad magician!";
  if(p == -1)
    return "Volunteer cheated!";
  return convertInt(p);
}

int main()
{
  ios::sync_with_stdio(0);
  cin >> T;
  for(int i = 1; i <= T; i++)
  {
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}
