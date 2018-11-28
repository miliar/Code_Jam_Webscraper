#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;
#define PMAX 110
#define VMAX 260
int t, fir, sec, cnt(0);
int be[5][5], en[5][5];
ifstream fin("A-small-attempt0.in");
void solve();
int main()
{
	cin.rdbuf(fin.rdbuf());
	cin >> t;
	while(t --){
		cin >> fir;
		for(int i = 1; i <= 4; ++ i)
			for(int j = 1; j <= 4; ++ j)
				cin >> be[i][j];
		cin >> sec;
		for(int i = 1; i <= 4; ++ i)
			for(int j = 1; j <= 4; ++ j)
				cin >> en[i][j];
		solve();
	}
}
void solve()
{
	int ans(0), anscnt(0);
	for(int i = 1; i <= 4; ++ i)
		for(int j = 1; j <= 4; ++ j)
			if(be[fir][i] == en[sec][j]){
				ans = be[fir][i];
				++ anscnt;
			}
	cout << "Case #" << ++ cnt << ": ";
	if(anscnt > 1)
		cout << "Bad magician!";
	else if(anscnt == 1)
		cout << ans;
	else
		cout << "Volunteer cheated!";
	cout << endl;
}


