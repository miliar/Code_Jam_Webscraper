#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int INF = numeric_limits<int>::max();

int n, N, r, p, s;
int c[3];
int lineup[10];
bool found;
int ans[10];

char st[] = {'P', 'R', 'S'};

int winner(int a, int b)
{
	if (a > b)
		swap(a, b);
	if(a == b - 1)
		return a;
	return b;
}

void rec(int i)
{
	if(i==N)
	{
		int q[10];
		for(int j=0;j<N;j++)
			q[j] = lineup[j];
		int m = N;
		for(int r=0;r<n;r++)
		{
			for(int j=0;j<m/2;j++)
			{
				if(q[2*j] == q[2*j+1])
					return;
				q[j] = winner(q[2*j], q[2*j+1]);
			}
			m /= 2;
		}
		found=true;
		memcpy(ans, lineup, sizeof(lineup));
		return;
	}
	for(int j=0;j<3;j++)
		if(c[j] > 0)
		{
			c[j]--;
			lineup[i] = j;
			rec(i+1);
			if(found) return;
			c[j]++;
		}
}

int main(int argc,char* argv[])
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1; test_case<=num_test_cases; test_case++)
	{
		scanf("%d%d%d%d", &n, &r, &p, &s);
		N = 1<<n;
		c[0]=p; c[1]=r; c[2]=s;
		found=false;
		rec(0);
		printf("Case #%d: ", test_case);
		if(found)
		{
			for(int i=0;i<N;i++)
				printf("%c", st[ans[i]]);
			printf("\n");
		}
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
