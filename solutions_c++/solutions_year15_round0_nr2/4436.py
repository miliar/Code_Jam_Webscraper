#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
using namespace std;

//#define real long long
#define real int
real N;

vector<int> numVec;
int maxMunite;
int findMaxValue()
{
	int k = -1;
	for (int i = 0; i < numVec.size(); i++)
	{
		if (numVec[i]>k) k = numVec[i];
	}
	return k;
}

void DFS(int depth,int curr)
{
	int m = findMaxValue();
	if ((m + depth) < maxMunite) maxMunite = m + depth;
	if (depth >= maxMunite-1) return;
	if (curr >= numVec.size()) return;
	for (int i = 2; i <= numVec[curr]/2; i++)
	{
		int k = numVec[curr];
		numVec[curr] = i;
		numVec.push_back(k- i);
		DFS(depth + 1, curr);
		numVec[curr] = k;
		numVec.pop_back();
	}
	DFS(depth, curr + 1);
}

void process()
{
	maxMunite = findMaxValue();

	DFS(0, 0);

	printf("%d", maxMunite);
}


void main()
{
	freopen("11.in", "r", stdin);
	freopen("11.out", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int time = 0; time < times; time++)
	{
		scanf("%d", &N);
		numVec.clear();
		int k;
		for (int i = 0; i < N; i++)
		{
			scanf("%d", &k);
			numVec.push_back(k);
		}
		printf("Case #%d: ", time + 1);
		process();
		printf("\n");
		fflush(stdout);
	}
}