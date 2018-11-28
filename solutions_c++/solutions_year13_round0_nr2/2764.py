#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	int pelouse[100][100] = {0};

	for (int t = 0; t < T; t++)
	{
		int N;
		int M;
		cin >> N;
		cin >> M;
		
		for (int n = 0; n < N; n++)
		{
			for (int m = 0; m < M; m++)
			{
				cin >> pelouse[m][n];
			}
		}

		int m = 0;
		bool fin = false;
		bool res = true;

		// speed
		//if(M == 1 || N == 1)
		//{
		//	fin = true;
		//}

		// For each case, the value must be >= all values in its row OR >= all values in its col.
		while(m < M && !fin)
		{
			int n = 0;
			while(n < N && !fin)
			{
				int x;
				bool ok = true;

				x = pelouse[m][n];
				for (int k = 0; k < N; k++)
				{
					if(x < pelouse[m][k])
					{
						ok = false;
					}
				}

				if(ok == false)
				{
					ok = true;
					for (int k = 0; k < M; k++)
					{
						if(x < pelouse[k][n])
						{
							ok = false;
						}
					}
				}

				if (ok == false)
				{
					//cout << "m:" << m << " n:" << n <<  "x " << x << endl;
					fin = true;
					res = false;
				}

				n++;
			}
			m++;
		}

		cout << "Case #" << t+1 << ": ";
		if(res == false)
			cout << "NO" << endl;
		else 
			cout <<"YES" << endl;

	}

	return 0;
}

