#include <iostream>
#include <string>
using namespace std;
int main()
{
	int T,N,M;
	int a[101][101];
	int Left[101][101];
	int Right[101][101];
	int Top[101][101];
	int Bottom[101][101];
	cin >> T;
	for(int t = 1; t<= T; ++t){
		scanf("%d %d",&N,&M);
		memset(Left,0,sizeof(Left));
		memset(Right,0,sizeof(Right));
		memset(Top,0,sizeof(Top));
		memset(Bottom,0,sizeof(Bottom));
		memset(a,0,sizeof(a));
		for(int i = 0; i< N; ++i)
		{
			for(int j = 0; j< M; ++j) scanf("%d",&a[i][j]);
		}
		
		for(int i = 0; i< N; ++i)
		{
			for(int j = 1; j< M; ++j)
			{
				Left[i][j] = max(Left[i][j-1],a[i][j-1]);
			}
		}
		for(int i = 0; i< N; ++i)
		{
			for(int j = M-2; j>=0; --j)
			{
				Right[i][j] = max(Right[i][j+1],a[i][j+1]);
			}
		}

		for(int j = 0; j< M; ++j)
		{
			for(int i = 1; i< N; ++i)
			{
				Top[i][j] = max(Top[i-1][j],a[i-1][j]);
			}
		}
		for(int j = 0; j< M; ++j)
		{
			for(int i = N-2; i>=0; --i)
			{
				Bottom[i][j] = max(Bottom[i+1][j],a[i+1][j]);
			}
		}
		bool ok = true;
		for(int i = 0; i< N; ++i)
		{
			for(int j = 0; j< M; ++j)
			{
				if((Left[i][j] > a[i][j] || Right[i][j] > a[i][j]) && (Top[i][j] > a[i][j] || Bottom[i][j] > a[i][j]))
				{
					ok = false;
					break;
				}
			}
			if(!ok) break;
		}
		if(ok) printf("Case #%d: YES\n",t);
		else printf("Case #%d: NO\n",t);
	}
}