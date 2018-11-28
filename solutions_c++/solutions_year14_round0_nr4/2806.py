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
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<double> vi;
int d1[1010], d2[1010];
int main(){
	R_W;
	int T;
	cin >> T;
	int cases = 1;
	while (T--)
	{
		int n;
		float in;
		cin >> n;
		r(n)
		{

			cin >> in;
			in *= 100000;
			d1[i] = in;
		}
		r(n)
		{
			cin >> in;
			in *= 100000;
			d2[i] = in;
		}
		sort(d1, d1 + n);
		sort(d2, d2 + n);
		int start = 0, end = n;
		int score1 = n;
		for (int i = 0; i < n; i++)
		{
			for (; start < n; start++)
			{
				if (d2[start]>d1[i])
				{
					score1--;
					start++;
					break;
				}
			}
		}
		start = 0;
		int score2 = 0;
		for (int i = 0; i < n; i++)
		{
			if (d2[start]<d1[i])
			{
				score2++;
				start++;
			}
			else{
				end--;
			}
			if (start >= end) break;
		}
		printf("Case #%d: %d %d\n", cases++ ,score2, score1);
	}
	return 0;
}