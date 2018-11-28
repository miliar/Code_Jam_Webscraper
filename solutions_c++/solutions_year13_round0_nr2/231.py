#include <bits/stdc++.h>

using namespace std;

int R, C, M[105][105], maxR[105], maxC[105];

int main()
{
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		cin>>R>>C;
		
		for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
				cin>>M[i][j];
		
		for(int i=0; i<R; i++)
		{
			maxR[i] = M[i][0];
			for(int j=1; j<C; j++)
				maxR[i] = max(maxR[i], M[i][j]);
		}
		
		for(int j=0; j<C; j++)
		{
			maxC[j] = M[0][j];
			for(int i=0; i<R; i++)
				maxC[j] = max(maxC[j], M[i][j]);
		}
		
		bool ok = 1;
		for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
				ok = ok && (M[i][j] >= maxR[i] || M[i][j] >= maxC[j]);
		
		cout<<"Case #"<<caso<<": "<<(ok ? "YES" : "NO")<<endl;
	}
  
	return 0;
}
