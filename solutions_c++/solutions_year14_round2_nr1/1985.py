#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <numeric>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		int N;
		cin >> N;

		vector<string> in(N),shin(N);
		vector<vector<int> > cal(N); 
	
		for (int i = 0; i < N; ++i)
		{
			cin >> in[i];

			shin[i] = "";
			int m = 0;
			for (int j = 0; j < in[i].size();)
			{
				shin[i] += in[i][j];
				char c = in[i][j];
				cal[i].push_back(0);
				while(in[i][j] == c)
				{
					++cal[i][m];
					++j;
				}
				m++;
			}

			/*cout << shin[i] << "\n";
			for (int j = 0; j < cal[i].size(); ++j)
			{
				cout << cal[i][j] << " ";
			}
			cout << "\n";*/
		}
		bool flag = true;
		for (int i = 1; i < N; ++i)
		{
			if(shin[i] != shin[0])
			{
				flag = false;
				break;
			}
		}
		cout << "Case #" << t <<": ";
		if(!flag)
		{
			cout << "Fegla Won\n";
		}
		else
		{
			vector<int> mincal(cal[0].size(),1000);
			vector<int> calsum(N,0);
			for (int j = 0; j < cal[0].size(); ++j)
			{
				for (int k = 0; k < cal.size(); ++k)
				{
					if(cal[k][j] < mincal[j])
						mincal[j] = cal[k][j];
				}
			}
			int minsum = accumulate(mincal.begin(), mincal.end(),0);
			int mcount = 0;
			for (int i = 0; i < N; ++i)
			{
				calsum[i] = accumulate(cal[i].begin(), cal[i].end(),0);
				mcount += (calsum[i] - minsum);
			}
			
			int minx = 1000;
			for (int i = 0; i < N; ++i)
			{
				int count = 0;
				for (int j = 0 ; j < N; ++j)
				{
					for (int k = 0; k < cal[0].size(); ++k)
					{
						count += abs((cal[i][k]-cal[j][k]));
					}
				}
				if(count < minx)
					minx = count;
			}
			cout << min(minx,mcount) << "\n";
		}
	}
	return 0;
}