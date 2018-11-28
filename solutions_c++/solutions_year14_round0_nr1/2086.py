/* bhupkas */

using namespace std;

#include "bits/stdc++.h"

int main()
{
	int t;
	cin >> t;
	int grid[2][5][5];
	int x[2];
	int cnt;
	bool B[20];
	int re;
	for(int tc = 1 ; tc <= t ; tc++)
	{
		for(int i = 0 ; i < 20 ; ++i)	B[i] = false;
		cnt = 0;
		cin >> x[0];
		x[0]--;
		for(int i = 0 ; i < 4 ; ++i)	for(int j = 0 ; j < 4 ; ++j)	cin >> grid[0][i][j];
		for(int j = 0 ; j < 4 ; ++j)	B[grid[0][x[0]][j]] = true;	
		cin >> x[1];
		x[1]--;
		for(int i = 0 ; i < 4 ; ++i)	for(int j = 0 ; j < 4 ; ++j)	cin >> grid[1][i][j];
		for(int j = 0 ; j < 4 ; ++j)	if(B[grid[1][x[1]][j]])		re = grid[1][x[1]][j] , cnt++;
		printf("Case #%d: ",tc);
		if(cnt == 1)
			cout << re << endl;
		else if(cnt == 0)
			cout << "Volunteer cheated!" << endl;
		else	cout << "Bad magician!" << endl;
			
	}
	return 0;
}
