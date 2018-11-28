#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main()
{
	int T;
	cin >> T;
	int cases = 0;
	for(int i = 0; i < T; i++)
	{
		cases++;
		int N, M;
		cin >> N >> M;
		vector<vector<int> > lawn(N);
		vector<int> maxl(N);
		vector<int> maxc(M);
		for(int j = 0; j < N; j++)
		{
			int maxh;
			cin >> maxh;
			lawn[j].push_back(maxh);
			for(int k = 1; k < M; k++)
			{
				int height;
				cin >> height;
				lawn[j].push_back(height);
				if(height > maxh)
					maxh = height;
			}
			maxl[j] = maxh;
		}
		for(int k = 0; k < M; k++)
		{
			int maxh;
			maxh = lawn[0][k];
			for(int j = 1; j < N; j++)
			{
				if(lawn[j][k] > maxh)
					maxh = lawn[j][k];
			}
			maxc[k] = maxh;
		}
		bool oker = true;
		for(int j = 0; j < N; j++)
		{
			for(int k = 0; k < M; k++)
			{
				bool vert = false, hor = false;
				if(lawn[j][k] < maxc[k])
					vert = true;
				if(lawn[j][k] < maxl[j])
					hor = true;
				if(hor && vert)
					oker = false;
			}
		}
		cout << "Case #" << cases << ": ";
		if(oker)
			cout << "YES\n";
		else
			cout << "NO\n";
	}
}
