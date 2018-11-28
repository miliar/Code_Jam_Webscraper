#include <iostream>
using namespace std;

int main()
{
	int T, N, M;
	cin >> T;
	int a[200][200], cMax[200], rMax[200];
	for (int t = 1 ; t <= T ; t ++)
	{
		cin >> N >> M;
		for (int i = 0 ; i < N ; i ++)
			for (int j = 0 ; j < M ; j ++)
				cin >> a[i][j];

		for (int i = 0 ; i < N ; i ++)
		{
			rMax[i] = 0;
			for (int j = 0 ; j < M ; j ++)
				if (rMax[i] < a[i][j])
					rMax[i] = a[i][j];
		}
		
		for (int j = 0 ; j < M ; j ++)
		{
			cMax[j] = 0;
			for (int i = 0 ; i < N ; i ++)
				if (cMax[j] < a[i][j])
					cMax[j] = a[i][j];
		}
		
		bool ans = 1;
		for (int i = 0 ; ans && i < N ; i ++)
			for (int j = 0 ; ans && j < M ; j ++)
				if (a[i][j] != rMax[i] && a[i][j] != cMax[j])
					ans = 0;
		cout << "Case #" << t << ": " << (ans ? "YES" : "NO") << endl;
	}
	return 0;
}
