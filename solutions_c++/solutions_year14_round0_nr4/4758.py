#include <assert.h>
#include <cstring>
#include <iostream>
#include <fstream>
#include <climits>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
using namespace std;

double MAX_V = numeric_limits<double>::max();

int getElement(const vector<double> &p1, const vector<double> &p2, const int N)
{
	double tmp;
	int score = 0;
		
	unordered_set<double> hash1;
	
	for (int i = 0; i < N; i++)
	{
		hash1.insert(p1[i]);
	}

	for (int i = 0; i < N; i++) 
	{
		double tmp = p2[i];
		double greaterMinW = MAX_V;
		double minW = MAX_V;
		//printf("%lf\n", MAX_V);
		for (auto x : hash1) 
		{
			if (x > tmp) 
			{
				greaterMinW = min(greaterMinW, x);
			}
			
			{
				minW = min(minW, x);
			}
		}
		if (greaterMinW != MAX_V)
		{
			hash1.erase(greaterMinW);
			//printf("!!%lf\n", greaterMinW);
			score++;
		}
		else 
		{
			hash1.erase(minW);
			//printf("**%lf\n", minW);
		}
	}
	return score;
}

int main() {
	int cases;
	int N;
	double tmp;
	cin >> cases;
	for (int t = 1; t <= cases; t++)
	{
		vector<double> p1, p2;
		
		cin >> N;

		for (int i = 0; i < N; i++) 
		{
			cin >> tmp;
			p1.push_back(tmp);
		}
		for (int i = 0; i < N; i++) 
		{
			cin >> tmp;
			p2.push_back(tmp);
		}

		printf("Case #%d: %d %d\n", t, getElement(p1, p2, N), N - getElement(p2, p1, N));
	}
	return 0;
}