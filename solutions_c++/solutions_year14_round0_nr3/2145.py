#include <iostream>
using namespace std;

#define L 6
#define N 26

int click(int m[L][L], bool visitadas[L][L], int i, int j, int r, int c)
{
	if (i<1 || j<1 || i>r || j>c) return 0;
	if (visitadas[i][j]) return 0;
	if (m[i][j] == -1) return 0;

	visitadas[i][j] = true;

	if (m[i][j] > 0) 
		return 1;
	else
	{
		int s = 1;
		for (int k=-1; k<=1; k++)
			for (int l=-1; l<=1; l++)
				s += click(m, visitadas, i+k, j+l, r, c);
		return s;
	}
}

bool bt(int ai[N], int aj[N], int k, int n, int r, int c, int &ci, int &cj, int r0, int c0)
{
	if (k == n)
	{
		int m[L][L];
		memset(m, 0, sizeof(m));

		for (k=1; k<=n; k++)
		{
			int fil = ai[k], 
				col = aj[k];

			m[fil][col] = -1;

			for (int i=-1; i<=1; i++)
				for (int j=-1; j<=1; j++)
					//if (i*i+j*j!=0 && fil+i>=1 && col+j>=1 && fil+i<=r && col+j<=c && m[fil+i][col+j]!=-1)
					if (i*i+j*j!=0 && fil+i>=1 && col+j>=1 && fil+i<=r0 && col+j<=c0 && m[fil+i][col+j]!=-1)
						m[fil+i][col+j]++;
		}

		for (int i=1; i<=r; i++)
			for (int j=1; j<=c; j++)
			{
				bool visitadas[L][L];
				memset(visitadas, false, sizeof(visitadas));

				if (click(m, visitadas, i,j,r0,c0) == r0*c0-n) 
				{
					ci = i;
					cj = j;
					return true;
				}
			}
	}
	else 
	{
		if (n-k<r && n-k<c)
		{
			//bool ensoli[L] = {false}, 
				//ensolj[L] = {false};
			bool ensol[L][L];
			memset(ensol, false, sizeof(ensol));
		
			for (int i=1; i<=k; i++)
			{
				//ensoli[ai[i]] = true;
				//ensolj[aj[i]] = true;
				ensol[ai[i]][aj[i]] = true;
			}

			k=k+1;
			for (int i=1; i<=r; i++)
				for (int j=1; j<=c; j++)
				{
					//if (ensoli[i] && ensolj[j]) continue;
					if (ensol[i][j]) continue;
					ai[k] = i;
					aj[k] = j;
					if (bt(ai, aj, k, n, r, c, ci, cj, r0, c0)) 
						return true;
				}
		}
		else
		{
			if (n-k>=c)
			{
				for (int i=1; i<=c; i++)
				{
					//k=k+1;
					ai[k+i] = r;
					aj[k+i] = i;				
				}
				if (bt(ai, aj, k+c, n, r-1, c, ci, cj, r0, c0)) 
					return true;
			}

			if (n-k>=r)
			{
				for (int i=1; i<=r; i++)
				{
					//k=k+1;
					ai[k+i] = i;
					aj[k+i] = c;
				}
				if (bt(ai, aj, k+r, n, r, c-1, ci, cj, r0, c0))
					return true;
			}			
		}		
	}

	return false;
}

void imprimir(int ai[N], int aj[N], int n, int r, int c, int ci, int cj)
{
	//bool ensoli[L] = {false}, 
	//	ensolj[L] = {false};
	//	
	//for (int i=1; i<=n; i++)
	//{
	//	ensoli[ai[i]] = true;
	//	ensolj[aj[i]] = true;
	//}
	bool ensol[L][L];
	memset(ensol, false, sizeof(ensol));
		
	for (int i=1; i<=n; i++)
		ensol[ai[i]][aj[i]] = true;

	for (int i=1; i<=r; i++)
	{		
		for (int j=1; j<=c; j++)
			if (i == ci && j == cj)
				cout << 'c';
			//else if (ensoli[i] && ensolj[j])
			else if (ensol[i][j])
				cout << '*';
			else
				cout << '.';
		cout << endl;
	}
}

int main()
{
	int casos;
	cin >> casos;
	for (int caso=1; caso<=casos; caso++)
	{
		int r, c, m;
		cin >> r >> c >> m;
		
		int ai[N], aj[N];
		int ci, cj;

		cout << "Case #" << caso << ":" << endl;

		//if (caso == 25)
		//{
		//	cout << r << c << m << endl;
		//}

		if (bt(ai, aj, 0, m, r, c, ci, cj, r, c))
			imprimir(ai, aj, m, r, c, ci, cj);
		else 
			cout << "Impossible" << endl;
	}

	//cin >> casos;
	return 0;
}