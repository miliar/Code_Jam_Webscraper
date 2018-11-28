#if 1
#include <iostream>
#include <fstream>
using namespace std;

#define ZERO_MEM(x) memset(x, 0, sizeof(x));
#define MAX_SIZE	100
//#define DEBUG_REMOVE
void main()
{
	ifstream fin("B-small-attempt.in");
//	ifstream fin("input.txt");
	int cnt;
	fin >> cnt;

	int field[MAX_SIZE+2][MAX_SIZE+2];
	int n , m;
	ofstream fout("output.txt");
	bool res;
	for(int p=0; p<cnt; p++)
	{
		ZERO_MEM(field)
		fin >> n >> m;
		
		for(int i=1; i<=n; i++)
		{
			for(int j=1; j<=m; j++)
			{
				fin >> field[i][j];
			}
		}

		res = true;
		int cur;
		
		for(int i=1; i<=n; i++)
		{
			for(int j=1; j<=m; j++)
			{

				cur = field[i][j];

				bool bInRow = false;
				for(int k=0; k<=m; k++)
				{
					if(field[i][k] > cur)
					{
						bInRow = true;
					}
				}



				// 가로 방향에 큰값이 있는데
				if(bInRow)
				{
					// 세로 방향에도 큰값이 있으면 안됨
					for(int l=1; l<=n; l++)
					{
						if(field[l][j] > cur)
						{
							res = false;
							goto TEST_END;
						}
					}
				}

			}
		}





TEST_END:
#ifdef DEBUG_REMOVE
		for(int i=1; i<=n; i++)
		{
			for(int j=1; j<=m; j++)
			{
				fout <<  field[i][j] << " " ;
			}
			fout << endl;
		}
#endif
		fout << "Case #" << p+1 << ": " << (res?"YES":"NO") << endl;
		cout << "Case #" << p+1 << ": " << (res?"YES":"NO") << endl;
	}

}

#endif