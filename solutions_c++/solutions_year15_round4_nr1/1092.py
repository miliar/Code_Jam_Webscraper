#include <bits/stdc++.h>
using namespace std;

const int hx[4] = {-1, 0, 1, 0};
const int hy[4] = {0, 1, 0, -1};
int test;
int r,c;
int a[111][111];
bool kt[111][111];

bool check(int i, int j)
{
	return((i >= 0 && i < r && j >= 0 && j < c));
}

int process()
{
	int rs = 0;
	memset(kt, false, sizeof kt);
		for(int i = 0; i < r; i++)
			for(int j = 0; j < c; j++)
				if(a[i][j] != -1 && !kt[i][j])
				{
					int u = i, v = j;
					int k = a[u][v];
					bool ok = false;
					kt[i][j] = true;
					u += hx[k]; v += hy[k];
					while(check(u, v) && a[u][v] == -1)
					{
						u += hx[k];
						v += hy[k];
					}
					if(!check(u, v)) 
					{
						int dem = 0;
						for(int hu = 0; hu < r; hu++)
							if(a[hu][j] != -1) dem++;
						for(int hv = 0; hv < c; hv++)
							if(a[i][hv] != -1) dem++;
						if(dem < 3) return -1;
						rs++;
					}
				}
	return rs;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> test;
	for(int t = 1; t <= test; t++)
	{
		cin >> r >> c;
		for(int i = 0; i < r; i++)
		{
			for(int j = 0; j < c; j++)
			{
				char ch;
				cin >> ch;
				if(ch == '^') a[i][j] = 0;
				if(ch == '.') a[i][j] = -1;
				if(ch == '>') a[i][j] = 1;
				if(ch == 'v') a[i][j] = 2;
				if(ch == '<') a[i][j] = 3;
			}
		}
		cout << "Case #" << t << ": ";
		int kq = process();
		if(kq == -1) cout << "IMPOSSIBLE" << "\n";
		else cout << kq << "\n";
	}
	return 0;
}