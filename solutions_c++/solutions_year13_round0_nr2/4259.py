#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t=1;t<=T;++t)
	{
		int N,M;
		int map[101][101];
		
		cin >> N >> M;
		for (int i=0;i<N;++i)
		{
			for (int j=0;j<M;++j)
			{
				cin >> map[i][j];
			}
		}
		
		int row[101]={0}, col[101]={0};
		int state = 1;
		for (int h=1;h<=100;++h)
		{
			for (int i=0;i<N;++i)
			{
				for (int j=0;j<M;++j)
				{
					if (map[i][j] == h)
					{
						if (row[i] == 0)
						{
							//check row[i]
							int cutRow = 1;
							for (int k=0;k<M;++k)
							{
								if (map[i][k] > h)
								{
									cutRow = 0;
									break;
								}
							}
							row[i] = cutRow;
						}
						if (col[j] == 0)
						{
							//check col[j]
							int cutCol = 1;
							for (int k=0;k<N;++k)
							{
								if (map[k][j] > h)
								{
									cutCol = 0;
									break;
								}
							}
							col[j] = cutCol;
						}
						
						if (row[i] == 0 && col[j] == 0)
						{
							state = -1;
							break;
						}
					}
				}
				if (state == -1) break;
			}
			if (state == -1) break;
		}
		
		cout << "Case #" << t << ": ";
		if (state == -1) cout << "NO\n";
		else
		{
			//just to make sure
			for (int i=0;i<N;++i)
			{
				if (row[i] == 0) 
				{
					state = -1;
					break;
				}
			}
			for (int i=0;i<M;++i)
			{
				if (col[i] == 0) 
				{
					state = -1;
					break;
				}
			}
			if (state == -1) cout << "NO\n";
			else cout << "YES\n";
		}
	
	}
	return 0;
}