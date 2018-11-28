#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int method1(vector<int>& mushrooms)
{
	int eat = 0;

	for(int i = 1; i < mushrooms.size(); i++) {
		if (mushrooms[i-1] > mushrooms[i]) 
			eat += (mushrooms[i-1] - mushrooms[i]);
	}

	return eat;
}

int getRate(vector<int>& mushrooms)
{
	int rate = 0;

	for(int i = 1; i < mushrooms.size(); i++) {	
		if (mushrooms[i-1] > mushrooms[i])
			rate = max(rate, mushrooms[i-1] - mushrooms[i]);
	}

	return rate;
}

int method2(vector<int>& mushrooms)
{
	int eat = 0;
	int rate = getRate(mushrooms);

	for(int i = 1; i < mushrooms.size(); i++) {
		eat += min(mushrooms[i-1], rate);
	}

	return eat;
}

int main()
{
	int T;

	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		int N;

		cin >> N;
		vector<int> mushrooms;

		for(int i = 0; i < N; i++) {
			int m;
			
			cin >> m;
			mushrooms.push_back(m);
		}

		cout << "Case #" << t << ": " << method1(mushrooms) << " " << method2(mushrooms) << endl;
	}
	return 0;
}
