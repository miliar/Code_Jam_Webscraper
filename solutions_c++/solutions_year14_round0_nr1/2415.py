#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int t, test = 1;
int map[5][5];
int map2[5][5];
int ans1,ans2;
int res = 0;
bool check1[17];
bool check2[17];
bool done = false;

void solve()
{
	cin >> ans1;
	for( int i = 1 ; i <= 4 ; i++ )
		for( int j = 1 ; j <= 4 ; j++ )
			cin >> map[i][j];
	cin >> ans2;
	for( int i = 1 ; i <= 4 ; i++ )
		for( int j = 1 ; j <= 4 ; j++ )
			cin >> map2[i][j];
	for( int i = 1 ; i <= 4 ; i++ )
	{
		check1[ map[ans1][i] ] = true;
		check2[ map2[ans2][i] ] = true;
	}
	for( int i = 1 ; i <= 16 ; i++ )
	{
		if( check1[i] && check2[i] )
		{
			if( !done )
			{
				done = true;
				res = i;
			}
			else
			{
				cout << "Case #" << test << ": Bad magician!" <<endl;
				return;
			}
		}
	}
	if( done )
	{
		cout << "Case #" << test << ": " << res << endl;
	}
	else
	{
		cout << "Case #" << test << ": Volunteer cheated!" <<endl;
	}
	return;
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out.","w",stdout);
	cin >> t;
	for( ; test <= t ; test++ )
	{
		done = false;
		memset(check1,false,sizeof(bool)*17);
		memset(check2,false,sizeof(bool)*17);
		solve();
	}
	return 0;
}