#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void fun()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i)
	{
		int N;
		cin >> N;
		vector<double> Naomi(N, 0.0);
		vector<double> Ken(N, 0.0);
		for(int j = 0; j < N; ++j)
			cin >> Naomi[j];
		for(int j = 0; j < N; ++j)
			cin >> Ken[j];
		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());
		int j = 0, k = N - 1, count = 0;
		cout << "Case #" << i << ": ";
		int bottom = 0;
		while(j < N && k >= bottom)
		{
			if(Naomi[j] > Ken[bottom])
			{
				++j;
				++bottom;
			}
			else if(Naomi[j] < Ken[k])
			{
				++j;
				--k;
				++count;
			}
			else
			{
				break;
			}
		}
		cout << (N - count) << " ";
		j = 0;
		k = 0;
		count = 0;
		while(j < N && k < N)
		{
			if(Naomi[j] > Ken[k])
			{
				++k;
			}
			else
			{
				++j;
				++k;
				++count;
			}
		}
		cout << (N - count) <<endl;
	}
}

int main()
{
	fun();
}
