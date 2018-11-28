#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <stack>
#include <sstream>
#include <cstring>
#include <numeric>
#include <ctime>

using namespace std;

#define pb push_back
#define sz(x) ((int) (x).size())
#define fo(i, n) for (int i = 0; i < (n); i++)
#define fo2(i, j, n) for (int i = j; i < (n); i++)
#define rfo(i, n) for (int i = (n) - 1; i >= 0; i--)
#define clr(x, y) memset(x, y, sizeof(x))
#define sqr(x) ((x) * (x))

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef long long ll;
typedef pair<ll,ll> pll;

bool win(char fields[4][4], char a)
{

	fo(i,4)
	{
		if ( 
				( (fields[i][0] == a) || (fields[i][0] == 'T') ) && 
				( (fields[i][1] == a) || (fields[i][1] == 'T') ) && 
				( (fields[i][2] == a) || (fields[i][2] == 'T') ) && 
				( (fields[i][3] == a) || (fields[i][3] == 'T') )
		   )
			return true;

		if ( 
				( (fields[0][i] == a) || (fields[0][i] == 'T') ) && 
				( (fields[1][i] == a) || (fields[1][i] == 'T') ) && 
				( (fields[2][i] == a) || (fields[2][i] == 'T') ) && 
				( (fields[3][i] == a) || (fields[3][i] == 'T') )
		   )
			return true;

		if ( 
				( (fields[0][0] == a) || (fields[0][0] == 'T') ) && 
				( (fields[1][1] == a) || (fields[1][1] == 'T') ) && 
				( (fields[2][2] == a) || (fields[2][2] == 'T') ) && 
				( (fields[3][3] == a) || (fields[3][3] == 'T') )
		   )
			return true;

		if ( 
				( (fields[0][3] == a) || (fields[0][3] == 'T') ) && 
				( (fields[1][2] == a) || (fields[1][2] == 'T') ) && 
				( (fields[2][1] == a) || (fields[2][1] == 'T') ) && 
				( (fields[3][0] == a) || (fields[3][0] == 'T') )
		   )
			return true;
	}
}

bool empty_exist(char fields[4][4])
{
	fo(i,4)
		fo(j,4)
			if (fields[i][j] == '.')
				return true;

	return false;
}

int main()
{
	int T;
	cin >> T;
	
	fo(t,T)
	{
		//cout << t + 1 << endl;

		char fields[4][4];
		fo(i,4)
			fo(j,4)
			{
				//cout << i << j << endl;
				cin >> fields[i][j];
			}
		
		
		cout << "Case #" << t + 1 << ": ";

		if ( win(fields, 'X') )
		{
			cout << "X won" << endl;
			continue;
		}
		if ( win(fields, 'O') )
		{
			cout << "O won" << endl;
			continue;
		}
		if (empty_exist(fields))
			cout << "Game has not completed"  << endl;
		else
			cout << "Draw" << endl;

/*
		fo(i,4)
			fo(j,4)
			{
				cout << i << ' ' << j << ' ' << fields[i][j] << endl;
			}
*/
		
	}
}
