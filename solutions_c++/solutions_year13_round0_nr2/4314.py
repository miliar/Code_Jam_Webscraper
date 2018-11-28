#include <iostream>
#include <cstring>
#define For(i, a, b) for(int i=a; i<b; ++i)
using namespace std;

int tabla[105][105], col[105], row[105];

int main()
{
	int T, N, M;
	cin>>T;
	For(k, 0, T)
	{
		memset(col, 0, sizeof(col));
		memset(row, 0, sizeof(row));
		
		cin>>N>>M;
		For(i, 0, N)
			For(j, 0, M)
			{
				cin>>tabla[i][j];
				col[j] = tabla[i][j] > col[j] ? tabla[i][j] : col[j];
				row[i] = tabla[i][j] > row[i] ? tabla[i][j] : row[i];
			}	
			
		bool could = true;
		For(i, 0, N)
		{
			if (!could) break;
			For(j, 0, M)
				if (tabla[i][j] < col[j] and tabla[i][j] < row[i])
				{
					could = false;
					break;
				}
		}
		
		if (could)
			cout<<"Case #"<<k+1<<": YES"<<endl;
		else
			cout<<"Case #"<<k+1<<": NO"<<endl;
	}
	return 0;
}
