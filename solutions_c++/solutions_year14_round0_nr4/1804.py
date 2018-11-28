#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define For(i,n) for (i=0; i<int(n); i++)
#define ForR(i,n) for (i=int(n)-1; i>=0; i--)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair
#define x first
#define y second

template<typename T> T Abs(T x) { return(x < 0 ? -x : x); }
template<typename T> T Sqr(T x) { return(x*x); }

const int INF = (int)1e9;
const LD EPS = 1e-9;
const LD PI = acos(-1.0);

#define DEBUG 0
#define NUM 1000
float input[2][NUM];
int cmp(const void *a, const void *b)
{
	float a1 = *(float *)a;
	float b1 = *(float *)b;
	return a1>b1?1:-1;
}
int main()
{
	FILE *fin;
	FILE *fout;
	//files
	freopen_s(&fin,"in.txt", "r", stdin);
	if (!DEBUG)
		freopen_s(&fout,"out.txt", "w", stdout);
	//vars
	int tt, TT;
	//testcase loop
	scanf_s("%d", &TT);
	For(tt, TT)
	{
		//init
		printf("Case #%d: ", tt + 1);
		//input
		int N;
		cin >>N;
		for (int i = 0; i < N; i++)
		{
			cin >> input[0][i];
		}
		for (int i = 0; i < N; i++)
		{
			cin >> input[1][i];
		}
	
		qsort(input[0], N, sizeof(input[0][0]), cmp);
		qsort(input[1], N, sizeof(input[1][0]), cmp);
		int ans1 = 0;
		int start1 = 0;
		int end1 = N-1;
		int start2 = 0;
		int end2 = N - 1;
		while (start1 <= end1)
		{
			if (input[0][end1] > input[1][end2])
			{
				ans1++;
				end1--;
				end2--;
			}
			else
			{
				start1++;
				end2--;
			}
		}
		int ans2 = 0;
		 start1 = 0;
		 end1 = N - 1;
		 start2 = 0;
		 end2 = N - 1;
		int large = 0;
		while (start1 <= end1)
		{
			if (end2<start2) break;
			if (input[0][end1] > input[1][end2])
			{
				if (large > 0)
				{
					large--;
					end1--;
					continue;
				}
				ans2++;
				end1--;
			}
			else
			{
				large++;
				end2--;
			}
		}
		printf("%d %d\n",ans1,ans2);
	}
	return(0);
}