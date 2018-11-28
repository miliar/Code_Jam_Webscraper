#include <iostream>

using namespace std;

int M, N;

bool check(int y, int x, int* d)
{
	int maxHeight = d[y*M+x];

	bool goodH = true;
	bool goodV = true;
	//cout << "Checking " << y << "," << x << endl;
	
	//Check l&r
	for(int l = (x-1); l >= 0; l--)
		if(d[y*M+l] > maxHeight)
		{
			goodH = false;
			break;
		}

	if(goodH)
	{
		for(int r = (x+1); r < M; r++)
			if(d[y*M+r] > maxHeight)
			{
				goodH = false;
				break;
			}
	}


	//Check u&d
	for(int u = (y-1); u >= 0; u--)
		if(d[u*M+x] > maxHeight)
		{
			goodV = false;
			break;
		}

	if(goodV)
	{
		for(int dwn = (y+1); dwn < N; dwn++)
			if(d[dwn*M+x] > maxHeight)
			{
				goodV = false;
				break;
			}
	}

	return (goodV || goodH);

}

int main()
{
	int T;

	cin >> T;

	for(int t = 0; t < T; t++)
	{
		cin >> N;
		cin >> M;

		int d[N*M];

		for(int n = 0; n < N; n++)
		{
			for(int m = 0; m < M; m++)
			{
				cin >> d[n*M+m];
			}
		}

		bool fine = true;
		for(int n = 0; n < N; n++)
		{
			for(int m = 0; m < M; m++)
			{
				if(check(n,m, d) == false)
				{
					fine = false;
					break;
				}
			}
			if(!fine)
				break;
		}

		cout << "Case #" << (t+1) << ": " << (fine ? "YES" : "NO") << endl;
	}
}