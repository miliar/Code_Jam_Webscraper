#include <fstream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <functional>
#define MIN(a,b) ((a)<(b))?(a):(b)

using namespace std;

int main()
{
	ofstream fout("D-large.out");
	ifstream fin("D-large.in");

	int t, count = 0;
	fin >> t;
	while(count++ < t)
	{
		int N;
		fin >> N;

		vector<double> girl(N, 0);
		vector<double> boy(N, 0);

		for(int i = 0; i < N; i++)
			fin >> girl[i];
		sort(girl.begin(), girl.end());
		for(int i = 0; i < N; i++)
			fin >> boy[i];
		sort(boy.begin(), boy.end());

		int normalwin = 0;
		int decitwin = 0;
		vector<double> playboy(boy);
		for(int i = 0; i < N; i++)
		{
			bool win = true;
			for(int j = 0; j < N; j++)
			{
				if(playboy[j] > girl[i])
				{
					playboy[j] = -1;
					win = false;
					break;
				}
				else if(j == N - 1)
				{
					for(int k = 0; k < N; k++)
					{
						if(playboy[k] != -1)
						{
							playboy[k] = -1;
							break;
						}
					}
				}
			}
			if(win)
				normalwin++;
		}

		playboy = boy;
		int begin = 0;
		for(int i = 0; i < N; i++)
		{
			bool win = true;
			for(int j = 0; j < N; j++)
			{
				if(playboy[j] == -1)
					continue;

				if(girl[i] > playboy[j])
				{
					playboy[j] = -1;
					win = true;
					break;
				}
				else
				{
					for(int k = N - 1; k >= 0; k--)
					{
						if(playboy[k] == -1)
							continue;
						playboy[k] = -1;
						win = false;
						break;
					}
				}
				if(!win)
					break;
			}
			if(win)
				decitwin++;
		}

		/*fout.setf(ios::showpoint);
		fout.precision(7);
		fout.setf(ios::fixed);*/

		fout << "Case #" << count << ": " << decitwin << " " << normalwin << endl;
	}
	return 0;
}
