#include<iostream>
#include<map>
#include<string>
#include<string.h>
#include<vector>
#include<stdio.h>
#include <cstdio>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <sstream>
#include <cmath>
#include <bitset>
#include <limits.h>
#include <limits>
#include <utility>
#include <set>
#include <numeric>
#include <functional>
#define R(i) freopen(i,"r",stdin)
#define W(i) freopen(i,"w",stdout)
#define R_W R("i.txt"),W("o.txt");
#define FOR(i,f,t) for(int i=f;i<t;i++)
#define r(e) for(int i=0;i<e;i++)
#define inf numeric_limits<int>::max()
#define minf numeric_limits<int>::min()
#define DFS_WHITE -1
#define DFS_BLACK 1
using namespace std;
int main(){
	R_W;
	int T;
	cin >> T;
	int c=1, result;
	while (T--)
	{
		map<int, int> m1, m2;
		int r;
		cin >> r;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int in;
				cin >> in;
				if (i == r - 1)
				{

					m1[in];
				}
			}
		}
		cin >> r;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int in;
				cin >> in;
				if (i == r - 1)
				{

					m2[in];
				}
			}
		}
		int val = -1;
		int count = 0;
		for (auto x : m1)
		{
			if (m2.count(x.first))
			{
				count++;
				val = x.first;
			}
		}
		if (count == 1)
		{
			printf("Case #%d: %d\n", c++, val);
		}
		else if (count == 0)
		{
			printf("Case #%d: Volunteer cheated!\n",c++);
		}
		else{
			printf("Case #%d: Bad magician!\n", c++);
		}
	}
	return 0;
}