/*
duyet binh thuong, tim nhung so trung o ca hai hang
*/
#include <iostream>
#include <stdio.h>
using namespace std;

#define FOR(i, a, b) for(int i = a; i <= b; i++)

int h1, h2, sotest;
int a[5][5], b[5][5];

void nhap()
{
	cin >> h1;
	FOR(i, 1, 4)
	FOR(j, 1, 4) 
		{
			scanf("%d", &a[i][j]);
			//cout << a[i][j] << ' ';
		}
	cin >> h2;
	FOR(i, 1, 4)
	FOR(j, 1, 4) 
		{
			scanf("%d", &b[i][j]);
			//cout << b[i][j] << ' ';
		}
}

void lam()
{
	int count = 0, luu;
	FOR(i, 1, 4)
	FOR(j, 1, 4)
	if (a[h1][i] == b[h2][j])
		{
			count++;
			luu = a[h1][i];
		}
	if (count == 0) cout << "Case #" << sotest << ": " << "Volunteer cheated!" << endl;
	else
		if (count == 1) cout << "Case #" << sotest << ": " << luu << endl;
		else cout << "Case #" << sotest << ": " << "Bad magician!" << endl;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int test;
	cin >> test;
	for (sotest = 1; sotest <= test; sotest++)
		{
			nhap();
			lam();
		}
	return 0;
}
