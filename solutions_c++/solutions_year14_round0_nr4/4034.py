#include<iostream>
#include<set>
#include<vector>
#include<algorithm>
#include<cstdio>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	int count = 0;
	while (T--)
	{
		if (count != 0)
			cout << endl;
		count++;
		cout << "Case #" << count << ": ";
		int n;
		scanf("%d", &n);
		vector<double> N(n),K(n);
		for (int i = 0; i < n; i ++ )
			scanf("%lf", &N[i]);
		for (int i = 0; i < n; i++)
			scanf("%lf", &K[i]);
		sort(N.begin(), N.end());
		sort(K.begin(), K.end());
		vector<double> NC(N.begin(), N.end());
		vector<double> KC(K.begin(), K.end());
		int NW=0,DW=0;
		for (int i = 0; i < n; i++)
		{
			double block = N[i];
			bool lost= false;
			double diff=10000;
			int index;
			for (int j = 0; j < n; j++)
			{
				if (K[j] == -1) continue;
				if (K[j]>N[i])
				{
					K[j] = -1;
					lost = true;
					break;
				}
				else
				{	
					if (diff > N[i] - K[j])
					{
						diff = N[i] - K[j];
						index = j;
					}					
				}
			}
			if (lost) continue;
			else
			{
				K[index] = -1;
				NW++;
			}
		}

		for (int i = 0; i < n; i++)
		{
			double diff = 10000;
			for (int j = 0; j < n; j++)
			{
				if (KC[j] == -1) continue;
				if (KC[j] < NC[i])
				{
					KC[j] = -1;
					DW++;
					break;
				}
			}
		}
		printf("%d %d", DW, NW);
	}
	return 0;
}