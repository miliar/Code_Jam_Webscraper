#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("outb.txt", "w", stdout);
	
	int TC;
	cin >> TC;
	
	for(int i = 0; i < TC; ++i)
	{
		int N, M;
		cin >> N >> M;
		
		int arr[N][M];
		
		for(int j = 0; j < N; ++j)
			for(int k = 0; k < M; ++k)
				cin >> arr[j][k];
				
		bool ans = true;
		
		for(int j = 0; j < N && ans; ++j)
			for(int k = 0; k < M && ans; ++k)
			{
				int max_col = 0;
				int max_row = 0;
				
				for(int u = 0; u < M; ++u)
					max_col = max(max_col, arr[j][u]);
					
				for(int u = 0; u < N; ++u)
					max_row = max(max_row, arr[u][k]);
					
				if( max_col > arr[j][k] )
				{
					if( max_row > arr[j][k] )
						ans = false;
				}
				else if( max_row > arr[j][k] )
						if( max_col > arr[j][k] )
							ans = false;
			}
			
		cout << "Case #" << i + 1 << ": " << ( ans ? "YES" : "NO" ) << endl;
	}
	
	return 0;
}
