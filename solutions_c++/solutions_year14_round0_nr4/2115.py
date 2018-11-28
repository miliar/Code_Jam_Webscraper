#include <iomanip>
#include <iostream>
#include <algorithm>
using namespace std;

const int MaxN = 1000 + 10;

int main()
{
	int T, t;
	int N;
	int i, j;
	double Nao[MaxN];
	double Ken[MaxN];

	cin >> T;
	for(t = 1; t <= T; t++)
	{
		cin >> N;
		for(i = 0; i < N; i++)
			cin >> Nao[i];
		for(j = 0; j < N; j++)
			cin >> Ken[j];
		
		sort(Nao, Nao + N);
		sort(Ken, Ken + N);

		/*
		for(i = 0; i < N; i++)
			cout << setprecision(3) << fixed << Nao[i] << " ";
		cout << endl;
		for(i = 0; i < N; i++)
			cout << setprecision(3) << fixed << Ken[i] << " ";
		cout << endl;
		*/

		int cnt1 = 0;
		for(i = 0, j = 0; i < N && j < N;)
		{
			if(Ken[i] > Nao[j])
			{
				i++;
				j++;
				cnt1++;
			}
			else
			{
				i++;
			}
		}

		int cnt2 = 0;
		for(i = 0, j = 0; i < N && j < N;)
		{
			if(Nao[i] > Ken[j])
			{
				i++;
				j++;	
				cnt2++;
				//cout << "i = " << i << " j = " << j << endl;
				//cout << Nao[i] << " V " << Ken[j] << endl;
			}
			else
			{
				i++;
			}
		}
		cout << "Case #" << t << ": " << cnt2 << " " << N - cnt1 << endl;
	}
	return 0;
}
