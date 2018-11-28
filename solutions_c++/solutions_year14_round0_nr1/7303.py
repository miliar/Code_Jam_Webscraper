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
#define forn(i, n) for (int i = 0; i < (n); i++)
#define rforn(i, n) for (int i = (n) - 1; i >= 0; i--)
#define clr(x, y) memset(x, y, sizeof(x))
#define sqr(x) ((x) * (x))

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef long long ll;
typedef pair<ll,ll> pll;


int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	forn(casenum,t)
	{
		int first_choise;
		cin >> first_choise;
		int first[4][4];
		forn(i,4)
			forn(j,4)
				cin >> first[i][j];
				
		int second_choise;
		cin >> second_choise;
		int second[4][4];
		forn(i,4)
			forn(j,4)
				cin >> second[i][j];
				
		int found = 0;
		int answer = -1;
		forn(i,4)
			forn(j,4)
			{
				if (first[first_choise-1][i] == second[second_choise-1][j])
				{
					answer = first[first_choise-1][i];
					found++;
				}
			}
		if (found == 0)
			cout << "Case #" << casenum+1 << ": " << "Volunteer cheated!" << endl;
		else if (found == 1)
			cout << "Case #" << casenum+1 << ": " << answer << endl;
		else
			cout << "Case #" << casenum+1 << ": " << "Bad magician!" << endl;
			
	
		// cout << "Case #" << casenum+1 << ": " << answer << endl;
	}
	

	return 0;
}