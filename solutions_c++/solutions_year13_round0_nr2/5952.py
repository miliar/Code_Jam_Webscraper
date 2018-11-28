#include <iostream>
using namespace std;
struct sides
{
	int south, north, east, west;
	int act;
};
sides tab[101][101];
int main()
{
	int Z;
	cin >> Z;
	for(int i = 0; i < Z; i++)
	{
		bool good = true;
		int N,M;
		cin >> N >> M;
		for(int j = 0; j < N; j++)
		{
			for(int k = 0; k < M; k++)
			{
				int val;
				cin >> val;
				tab[j][k].south = tab[j][k].north = tab[j][k].east = tab[j][k].west = tab[j][k].act = val;
			}
		}

		for(int j = 0; j < N; j++)
		{
			int max = tab[j][0].act;
			for(int k = 0; k < M; k++) 
			{
				tab[j][k].west = max;
				if(max < tab[j][k].act) max = tab[j][k].act;
			}
			max = tab[j][M-1].act;
			for(int k = M - 1; k >= 0; k--) 
			{
				tab[j][k].east = max;
				if(max < tab[j][k].act) max = tab[j][k].act;
			}

		}
		for(int j = 0; j < M; j++)
		{
			int max = tab[0][j].act;
			for(int k = 0; k < N; k++) 
			{
				tab[k][j].north = max;
				if(max < tab[k][j].act) max = tab[k][j].act;
			}
			max = tab[N-1][j].act;
			for(int k = N - 1; k >= 0; k--) 
			{
				tab[k][j].south = max;
				if(max < tab[k][j].act) max = tab[k][j].act;
			}

		}
		
		for(int j = 0; j < N; j++)
		{
			for(int k = 0; k < M; k++)
			{
				if((tab[j][k].act < tab[j][k].south || tab[j][k].act < tab[j][k].north) && (tab[j][k].act < tab[j][k].east || tab[j][k].act < tab[j][k].west)) good = false;
			}
		}
		string ans = "YES";
		if(!good) ans = "NO";
		cout << "Case #" << i + 1 << ": "<< ans << endl;
	}  
}
