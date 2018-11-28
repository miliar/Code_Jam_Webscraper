#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
using namespace std;

int r, c, m, f;
char sgr[55][55];
int gr[55][55];

int df[8][2] = {1, 0, 1, 1, 0, 1, -1, 1, -1, 0, -1, -1, 0, -1, 1, -1};

bool fok()
{
	for(int i = 0; i < r; ++i)
		for(int j = 0; j < c; ++j)
			if(gr[i][j] != -1)
			{
				for(int k = 0; k < 8; ++k)
				{
					int ii = i+df[k][0], jj = j + df[k][1];
					if(ii >= 0 && ii < r && jj >= 0 && jj < c)
						gr[i][j] += (gr[ii][jj] == -1);
				}
			}
	for(int i = 0; i < r; ++i)
		for(int j = 0; j < c; ++j)
			if(gr[i][j] > 0)
			{
				int q = 0;
				for(int k = 0; k < 8; ++k)
				{
					int ii = i+df[k][0], jj = j + df[k][1];
					if(ii >= 0 && ii < r && jj >= 0 && jj < c)
						q += (gr[ii][jj] == 0);
				}
				if(!q) return false;
			}
	return true;
}

bool fill(int a, int b, bool fr)
{
	memset(gr, 0, sizeof(gr));
	if(!a || !b) return !m;
	if(a > r || b > c)
		return false;

	memset(gr, (fr ? -1 : 0), sizeof(gr));
	for(int i = 0; i < a; ++i)
		for(int j = 0; j < b; ++j)
			gr[i][j] = (fr ? 0 : -1);

	int q = a*b - (fr ? f : m);
	if(q < b)
	{
		for(int j = 0; j < q; ++j)
			gr[a-1][j] = (fr ? -1 : 0);
		if(fok()) return true;

		memset(gr, (fr ? -1 : 0), sizeof(gr));
		for(int i = 0; i < a; ++i)
			for(int j = 0; j < b; ++j)
				gr[i][j] = (fr ? 0 : -1);
		for(int j = 0; j < q; ++j)
			gr[a-1][b-1-j] = (fr ? -1 : 0);
		if(fok()) return true;
	}

	memset(gr, (fr ? -1 : 0), sizeof(gr));
	for(int i = 0; i < a; ++i)
		for(int j = 0; j < b; ++j)
			gr[i][j] = (fr ? 0 : -1);

	if(q < a)
	{
		for(int j = 0; j < q; ++j)
			gr[j][b-1] = (fr ? -1 : 0);
		if(fok()) return true;

		memset(gr, (fr ? -1 : 0), sizeof(gr));
		for(int i = 0; i < a; ++i)
			for(int j = 0; j < b; ++j)
				gr[i][j] = (fr ? 0 : -1);
		for(int j = 0; j < q; ++j)
			gr[a-1-j][b-1] = (fr ? -1 : 0);
		if(fok()) return true;
	}
	
	return false;
}

void gr2sgr()
{
	memset(sgr, 0, sizeof(sgr));
	for(int i = 0; i < r; ++i)
		for(int j = 0; j < c; ++j)
			sgr[i][j] = (gr[i][j] == -1 ? '*' : '.');
	for(int i = 0; i < r; ++i)
		for(int j = 0; j < c; ++j)
			if(gr[i][j] == 0)
			{
				sgr[i][j] = 'c';
				return;
			}
}

int main()
{
	freopen("C-large.in", "r", stdin);
	//freopen("Cinput.txt", "r", stdin);
	freopen("Coutput.txt", "w", stdout);

	int T;
	cin >> T;
	for(int tt = 1; tt <= T; ++tt)
	{
		cin >> r >> c >> m;
		f = r*c - m;
		memset(gr, 0, sizeof(gr));

		printf("Case #%d:\n", tt);
		
		bool ok = 0;
		for(int a = 1; a <= f; ++a)
		{
			int b = (f + a - 1) / a;
			if(ok = fill(a, b, true))
				break;
		}

		if(!ok)
			for(int a = 1; a <= m; ++a)
			{
				int b = (m + a - 1) / a;
				if(ok = fill(a, b, false))
					break;
			}

		//cout << r << " " << c << " " << m << endl;	/// !!!

		if(!ok)
		{
			if(f == 1)
			{
				memset(sgr, 0, sizeof(sgr));
				for(int i = 0; i < r; ++i)
					for(int j = 0; j < c; ++j)
						sgr[i][j] = '*';
				sgr[0][0] = 'c';
				for(int i = 0; i < r; ++i)
					printf("%s\n", sgr[i]);
			}
			else
				printf("Impossible\n");


			// perebor
			/*for(int msk = (1<<(r*c)) - 1; msk >= 0; --msk)
			{
				memset(gr, 0, sizeof(gr));
				int q = 0;
				for(int i = 0; i < r*c; ++i)
					if(msk&(1<<i))
					{
						++q;
						gr[i/c][i%c] = -1;
					}
				if(q != m)
					continue;
				bool oo = fok();
				if(!oo)
					continue;
				else
				{
					gr2sgr();
					cout << "!!!\n";
					for(int i = 0; i < r; ++i)
						printf("%s\n", sgr[i]);
				}
			}*/
		}
		else
		{
			
			gr2sgr();
			for(int i = 0; i < r; ++i)
				printf("%s\n", sgr[i]);
		}
	}
	
	return 0;
}