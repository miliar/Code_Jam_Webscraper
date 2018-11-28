
#include <iostream>

#include <vector>
#include <string>


using namespace std;

int m( int l, int r )
{
	return ( l < r ? l : r );
}

int main( int, const char*[] )
{

	int test_num;
	cin >> test_num;

	int dp[2][100];
	dp[0][0] = 1;
	dp[1][0] = 0;
	for( int i=1; i<100; ++i )
	{
		dp[0][i] = dp[1][i-1] + 1;
		dp[1][i] = dp[0][i-1] + 1;
	}

	int ac[100];
	for( int test=0; test<test_num; ++test )
	{
		string v;
		cin >> v;

		int cnum = 0;
		ac[0] = v[0] == '+';
		for( int i=1; i<v.size(); ++i )
		{
			if ( v[i-1] != v[i] )
			{
				++cnum;
				ac[cnum] = !ac[cnum-1];
			}
		}

		int res = dp[ac[0]][cnum];

		cout << "Case #" << (test+1) << ": ";
		{ cout << res; }
		cout << endl;
	}

	return 0;
}

