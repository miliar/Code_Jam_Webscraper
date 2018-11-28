#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <list>
#include <stack>
#include <algorithm>
#include <queue>
#include <map>
#include <cstdlib>
#include <set>
#include <string>
#include <cstring>
#include <memory>

#pragma comment(linker, "/STACK:104857600,104857600")

using namespace std;

#define FILE_IO

class A
{
public:
	void Run();

private:
	void Input();
	void Do();
	void Output();

private:
	static const int MAX_M = 10000;
	long long BASE;
	int caseNum, caseIndex;
	int stationNum;
	int pathNum;
	int pointNum;
	pair<int, int> points[MAX_M * 2];
	long long oriTotal;
	long long total;
	long long result;
};

void A::Run()
{
	BASE = 1000002013LL;
	scanf("%d", &caseNum);
	for(caseIndex = 1; caseIndex <= caseNum; ++caseIndex)
	{
		Input();
		Do();
		Output();
	}
}

void A::Input()
{
	scanf("%d %d", &stationNum, &pathNum);
	pointNum = 0;
	oriTotal = 0;
	for(int i = 0; i < pathNum; ++i)
	{
		int start, end, p;
		scanf("%d %d %d", &start, &end, &p);
		points[pointNum].first = start;
		points[pointNum].second = -p;
		++pointNum;
		points[pointNum].first = end;
		points[pointNum].second = p;
		++pointNum;

		long long dis = end - start;
		oriTotal += ((((2LL * stationNum - dis + 1) * dis / 2) % BASE) * p) % BASE;
		oriTotal %= BASE;
	}
}

void A::Do()
{
	sort(points, points + pointNum);
	vector<pair<int, int> > people;
	total = 0LL;
	for(int i = 0; i < pointNum; ++i)
	{
		if(points[i].second < 0)
		{
			people.push_back(pair<int, int>(-points[i].second, points[i].first));
		}
		else
		{
			int n = points[i].second;
			while(n)
			{
				if(people.back().first > n)
				{
					int dis = points[i].first - people.back().second;
					total += ((((2LL * stationNum - dis + 1) * dis / 2) % BASE) * n) % BASE;
					total %= BASE;
					people.back().first -= n;
					n = 0;
				}
				else
				{
					int dis = points[i].first - people.back().second;
					total += ((((2LL * stationNum - dis + 1) * dis / 2) % BASE) * people.back().first) % BASE;
					total %= BASE;
					n -= people.back().first;
					people.pop_back();
				}
			}
		}
	}
	result = oriTotal - total;
	if(result < 0) result += BASE;
	result %= BASE;
}

void A::Output()
{
	printf("Case #%d: %lld\n", caseIndex, result);
}

A instance;
int main()
{
	#ifdef FILE_IO
	freopen("C:\\Users\\Administrator\\Desktop\\data\\in.txt", "r", stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\data\\out.txt", "w", stdout);
	#endif

	instance.Run();
	return 0;
}
