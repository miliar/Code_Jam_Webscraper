/*
 * =====================================================================================
 *
 * Nazwa pliku:  	B.cpp
 * Autor:		Szymon Stankiewicz (Daku)
 * Kontakt:		dakurels@gmail.com
 * Stworzony:		13.04.2013 23:28:27
 *
 * =====================================================================================
 */
#include<cstdio>
#include<algorithm>

using namespace std;

int maxi[2][107], N, M, traw[107][107];

bool test()
{
	scanf("%d %d", &N, &M);
	for(int i = 0; i<max(N, M); i++)
		maxi[0][i]=maxi[1][i]=0;
	for(int i = 0; i<N; i++)
	{
		for(int j = 0; j<M; j++)
		{
			scanf("%d", &traw[i][j]);
			maxi[0][i]=max(maxi[0][i], traw[i][j]);
			maxi[1][j]=max(maxi[1][j], traw[i][j]);
		}
	}
	for(int i = 0; i<N; i++)
		for(int j = 0; j<M; j++)
			if(traw[i][j]< maxi[0][i] && traw[i][j]<maxi[1][j])
				return false;
	return true;
}

int T;

int main()
{
	bool wart;
	scanf("%d", &T);
	for(int i = 1; i<=T; i++)
	{
		wart=test();
		printf("Case #%d: ", i);
		if(wart)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
