
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <unordered_map>


using namespace std;


int main()
{
	freopen("input.txt","rt", stdin);
	freopen("output.txt","wt", stdout);			
	int tests;
	scanf("%d\n", &tests);	
	long long pp = 1000002013;
	int o, e, p;
	map <int, long long> enter;
	map <int, long long> leave;
	map <int, long long> ind;

	long long sum [10000];
	map<int , long long> loc;
	//for (int i = 0; i < 3000; i++)
	for (int test = 1; test <= tests; test++)
	{

		int n; int m;
		
		scanf("%d%d", &n, &m);		
		enter.clear();
		leave.clear();
		//loc.clear();
		ind.clear();
		long long anw2 = 0;
		for (int i = 0; i < m; i++)
		{
			scanf("%d%d%d", &o, &e, &p);
			enter[o] += p % pp;
			enter[e] += 0;

			leave[e] += p % pp;
			leave[o] += 0;
			ind[o] = 1;
			ind[e] = 1;
			//enter.push_back(make_pair(o, p));
			//leave.push_back(make_pair(e, p));
			//enter[loc]
			long long delta = e - o;
			long long s1 = ((long long)(n)*(n+1)/2) % pp;
			long long n2 = n-delta;
			long long s2 = n2*(n2+1)/2 % pp;
			anw2 = anw2 + (s1-s2)*p % pp;
			anw2 %= pp;


		}
		//sort(enter.begin(), enter.end());
		//sort(leave.begin(), leave.end());

		for (auto it = ind.begin(); it!= ind.end(); it++)
		{
			int i = it->first;
			long long minn = min (enter[i], leave[i]);
			enter[i] -= minn;
			leave[i] -= minn;
		}
		long long anw = 0;
		while(1)
		{
		long long s1 = 0;
		long long s2 = 0;
		long long amnt = 1000000100;		
		int i0 = -1;
		for (auto it = ind.begin(); it!= ind.end(); it++)
		{
			int i = it->first;
			if (enter[i] > 0)
			{
				i0 = i;
				break;
			}
			
		}
		if (i0 == -1)
			break;
		for (auto it = ind.begin(); it!= ind.end(); it++)
		{
			int i = it->first;
			if (enter[i] == 0 && leave[i] == 0)
				continue;
			s1 += enter[i];
			s2 += leave[i];
			if (s1 == s2  && leave[i] > 0)
			{
				// we need to make a move
				amnt = min (amnt, min(enter[i0], leave[i]) );
				// from i0 to i
				long long delta = i - i0;
				long long s1 = ((long long)(n)*(n+1)/2) % pp;
				long long n2 = n-delta;
				long long s2 = n2*(n2+1)/2 % pp;
				anw = anw + (s1-s2)*amnt % pp;
				enter[i0] -= amnt;
				leave[i] -= amnt;
				anw %= pp;

			}
			amnt = min(amnt, s1-s2);
			
		}

		}
		//reverse(leave.begin(), leave.end());
		/*
		long long s1, s2;



		int i1 = 0;
		int j1 = 0;

		while(i1 < enter.size() && j1 < leave.size())
		{
			long long amnt;
			if (enter[i1].second == leave[j1].second)
			{
				amnt = enter[i1].second;				
			}
			if (enter[i1].second > leave[j1].second)
			{
				amnt = leave[j1].second;				
			}
			if (enter[i1].second < leave[j1].second)
			{
				amnt = enter[i1].second;				
			}

			long long delta = leave[j1].first - enter[i1].first;
			long long s1 = ((long long)(n)*(n+1)/2) % pp;
			long long n2 = n-delta;
			long long s2 = n2*(n2-1)/2 % pp;
			anw = anw + (s1-s2)*amnt % pp;
			enter[i1].second -= amnt;
			if (enter[i1].second == 0)
				i1++;
			leave[j1].second -= amnt;
			if (leave[j1].second == 0)
				j1++;

		}
		*/
		long long aa = anw2 % pp - anw %pp;
		aa = (aa + pp + pp)%pp;

		printf("Case #%d: %I64d\n",test, aa);		

	}
		
	return 0;			
}     
