#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector< vector<int> > mat;

bool solve()
{
	int n, m;

	scanf("%d %d", &n, &m);

	mat.assign( n+1, vector<int>(m+1,0) );


	for(int i=1; i<=n; ++i)
	{

		for(int j=1; j<=m; ++j)
		{
			scanf("%d", &mat[i][j]);
			mat[0][j] = max( mat[0][j], mat[i][j] );
			mat[i][0] = max( mat[i][0], mat[i][j] );
		}
	}

	/*
	for(int i=0; i<=n; ++i)
	{

		for(int j=0; j<=m; ++j)
		{
			printf("%d ", mat[i][j]);
		}
		printf("\n");
	}
	*/

	for(int i=1; i<=n; ++i)
	{

		for(int j=1; j<=m; ++j)
		{
			if(mat[i][j] < mat[i][0] and mat[i][j] < mat[0][j])
				return false;
		}
	}


	return true;
}


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("Lawnmower.out", "w", stdout);
	int casos = 0;

	scanf("%d\n", &casos);
	for(int i=1; i<=casos; ++i)
	{
		bool tmp = solve();

		if (tmp == true)
			printf("Case #%d: YES\n", i);
		else
			printf("Case #%d: NO\n", i);
	}

	return 0;
}