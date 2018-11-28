#include <iostream>
#include <fstream>
#include <algorithm>
#include <time.h>

using namespace std;

int main()
{
	ifstream ifs("D-large.in");
	ofstream ofs("D-large.out");
	int T, N;
	double Naomi[1000];
	double Ken[1000];
	double temp;
	int score1, score2;

	cin.rdbuf(ifs.rdbuf());
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> N;
		for (int j = 0; j < N; j++)
		{
			cin >> temp;
			Naomi[j] = temp;
		}

		for (int j = 0; j < N; j++)
		{
			cin >> temp;
			Ken[j] = temp;
		}

		sort(Naomi, Naomi+N);
		sort(Ken, Ken+N);

		score1 = 0;
		int start1 = 0, start2 = 0;
		int end1 = N, end2 = N;
		while (start1 < end1 && start2 < end2)
		{
			if (Naomi[start1] > Ken[start2])
			{
				score1++;
				start1++;
				start2++;
			}
			else
			{
				start1++;
				end2--;
			}
		}

		ofs << "Case #" << i+1 << ":" << " " << score1;

		score2 = N;
		start1 = 0;
		start2 = 0;
		end1 = N;
		end2 = N;
		while (start1 < end1 && start2 < end2)
		{
			if (Naomi[start1] > Ken[start2])
				start2++;
			else
			{
				score2--;
				start1++;
				start2++;
			}
		}

		ofs << " " << score2 << endl;	
	}

	//clock_t start = clock();
	//clock_t end = clock();
	//cout << end-start;

	system("pause");
}