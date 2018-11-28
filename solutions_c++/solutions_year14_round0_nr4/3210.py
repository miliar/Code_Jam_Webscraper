#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main()
{
	ifstream fin("test.in");
	ofstream fout("test.out");
	int T = 0;
	fin >> T;
	for(int t = 1;t <= T;t++)
	{
		int N = 0;
		fin >> N;
		float a[1010], b[1010];
		int labelB[1010];

		for(int i = 0;i < N;i++)
			fin >> a[i];
		for(int i = 0;i < N;i++)
			fin >> b[i];

		sort(a, a + N);
		sort(b, b + N);
		int ans1 = 0, ans2 = 0;
		memset(labelB, 0, N * sizeof(int));
		for(int i = 0;i < N;i++)
		{
			bool flag = false;
			for(int j = 0;j < N;j++)
			{
				if(b[j] < a[i] && labelB[j] == 0)
				{
					labelB[j] = 1;
					ans1++;
					flag = true;
					break;
				}
			}
			if(flag == false)
			{
				for(int j = N - 1;j >= 0;j--)
				{
					if(b[j] > a[i] && labelB[j] == 0)
					{
						labelB[j] = 1;
						break;
					}
				}
			}
		}

		memset(labelB, 0,N * sizeof(int));
		for(int i = 0;i < N;i++)
		{
			for(int j = 0;j < N;j++)
			{
				if(b[j] > a[i] && labelB[j] == 0)
				{
					labelB[j] = 1;
					ans2++;
					break;
				}
			}
		}

		fout << "Case #"<< t << ": " << ans1 << " " << N - ans2;
		if(t != T)
			fout << endl;
	}

	return 0;
}