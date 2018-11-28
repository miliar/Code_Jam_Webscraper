#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <cstring>
using namespace std;

#define mp make_pair
#define pp push_back
#define Sort(x) sort(x.begin(), x.end())
#define rep(i, x, y) for(int i = x; i < y; i++)
#define Rep(i, x, y) for(int i = x; i <= y; i++)
#define vi vector<int>
#define vvi vector<vector<int> >
#define ll long long
#define all(v) v.begin(),v.end()
#define ii pair<int, int>
#define mem(x, v) memset(x, v, sizeof(x))
#define nl '\n'

int main()
{
	int t, first, second;
	int res;
	int arr1[5][5], arr2[5][5];
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("magic.txt", "w", stdout);
	cin >> t;
	Rep(k, 1, t)
	{
		cin >> first;
		Rep(i, 1, 4)
		{
			Rep(j, 1, 4)
				cin >> arr1[i][j]; 
		}
		cin >> second;

		Rep(i, 1, 4)
		{
			Rep(j, 1, 4)
				cin >> arr2[i][j]; 
		}
		res = -1;

		Rep(i, 1, 4)
		{
			Rep(j, 1, 4)
			{
				if(arr1[first][i] == arr2[second][j])
				{
					if(res == -1)
						res = arr1[first][i];
					else if(res > 0)
						res = -2;
				}
			}
		}

		cout << "Case #" << k << ": ";
		if(res > 0)
			cout << res;
		else if(res == -1)
			cout << "Volunteer cheated!";
		else
			cout << "Bad magician!";
		cout << nl;
	}
	return 0;
}

	