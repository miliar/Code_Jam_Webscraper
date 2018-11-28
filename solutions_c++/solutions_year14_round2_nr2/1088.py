#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>

using namespace std;

int main()
{
	int T ;
	cin >> T;
	for ( int test = 1 ; test <= T ; test++ )
	{
		int a,b,k;
		int solve = 0;

		cin >> a >> b >> k;

		for ( int i = 0 ; i < a ; i++ )
		{
			for ( int j = 0 ; j < b ; j++ )
			{
				if ( (i & j) < k ) solve++;
			}
		}

		cout << "Case #" << test << ": " << solve << endl;
	}
}
