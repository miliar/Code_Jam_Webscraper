#include <cstdio>
#include <iostream> 

using namespace std; 

int a[4][4], b[4][4], used[20];

void solve(int tnum)
{
	memset(used, 0, sizeof(used)); 
	int a1, a2; 
	cin >> a1; 
	a1--; 
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cin >> a[i][j]; 
		}
	}
	cin >> a2; 
	a2--; 
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cin >> b[i][j]; 
		}
	}

	for (int i = 0; i < 4; i++)
	{
		used[a[a1][i]]++; 
		used[b[a2][i]]++; 
	}

	int cnt = 0, val = 0; 
	for (int i = 1; i <= 16; i++)
	{
		if (used[i] == 2) cnt++, val = i; 
	}
	cout << "Case #" << tnum << ": "; 
	if (cnt == 1) cout << val; 
	if (cnt == 0) cout << "Volunteer cheated!"; 
	if (cnt > 1) cout << "Bad magician!"; 
	cout << endl; 
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout); 

	int tc; 
	cin >> tc; 
	for (int t = 0; t < tc; t++)
	{
		solve(t + 1); 
	}

	return 0; 
}