#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <hash_map>
#include <unordered_set>


using namespace std;
typedef long long ll;


int main(){
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t)
	{
	

		int x, n, m;
		cin >> x >> n >> m;
		if (x == 4 && min(n, m) == 2 && max(n, m) == 4)
		{
			cout << "Case #" << t << ": RICHARD" << endl;
			continue;
		}
		bool can = true;
		for (int i = 1; i <= x; ++i)
		{
			for (int j = 1; j <= x; ++j)
			{
				if (i+j-1 == x)
				{
					if ((i > n || j > m) && (i > m || j > n))
						can = false;
				}
			}
		}
		if (can && ((n*m)%x == 0))
			cout <<"Case #"<<t<<": GABRIEL"<< endl;
		else
			cout << "Case #" << t << ": RICHARD" << endl;
	}


	return 0;
}