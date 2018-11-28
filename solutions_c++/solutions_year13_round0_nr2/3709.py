//Jakub Kuderski
#include <iostream>

using namespace std;

int tab[102][102];

bool checkHori(int x, int y)
{
	int min = tab[x][y];
	bool resL = true, resR = true;
	for(int i = 1; i<x && resL; i++) resL = tab[i][y] <= min;
	for(int i = x+1; tab[i][y] > -1 && resR; i++) resR = tab[i][y] <= min;
	return resL && resR;
}

bool chceckVerti(int x, int y)
{
	int min = tab[x][y];
	bool resU = true, resD = true;
	for(int i=1; i < y && resU; i++) resU = tab[x][i] <= min;
	for(int i = y+1; tab[x][i] > -1 && resD; i++) resD = tab[x][i] <= min;
	return resU && resD;
}


int main()
{
	ios::sync_with_stdio(0);

	int t, n = 0;
	cin >> t;
	while(t--)
	{
		n++;
		int a, b;
		cin >> a >> b;
		for(int i=0; i<102; i++) for(int k=0; k<102; k++) tab[i][k] = -1;

		for(int i=1; i<=a; i++) for(int k=1; k<=b; k++) cin >> tab[i][k];


		bool res = true;
		for(int i=1; i<=a; i++) for(int k=1; k<=b && res; k++)
		{
			res = chceckVerti(i, k) || checkHori(i, k);
		}
		cout << "Case #" << n << ": " << (res ? "YES" : "NO") << endl;
	}
	return 0;
}