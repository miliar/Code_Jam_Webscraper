#include <iostream>
#include <cstdio>
#include <queue>

#define MAXN 1024

using namespace std;

int N, a[MAXN];

void read()
{
	scanf("%d", &N);
	
	for(int i = 0; i < N; i++)
		scanf("%d", &a[i]);
}

priority_queue<int> Q;
int ans, mxK;

void rec(int k)
{
	priority_queue<int> bak = Q;
	int top = Q.top();

	ans = min(ans, top + k);

	/*while(!bak.empty())
		printf("%d ", bak.top()), bak.pop();
	printf("   ----->   %d(K) + %d(top) = %d \n", k, top, top + k);
	bak = Q;*/

	if(k >= mxK) 
		return;
	
	if(top == 1)
		return;

	for(int i = 1; i <= top - top / 2; i++)
	{
		Q.pop();
		Q.push(top - i);
		Q.push(i);

		rec(k + 1);

		Q = bak;
	}
}

void solve()
{
	priority_queue<int> newQ;
	Q = newQ;

	for(int i = 0; i < N; i++)
		Q.push(a[i]);

	ans = Q.top();
	mxK = Q.top();

	rec(0);

	printf("%d\n", ans);
}

int main()
{
	int T;
	scanf("%d", &T);

	for(int test = 1; test <= T; test++)
	{
		read();
		printf("Case #%d: ", test);
		solve();
	}	
	return 0;
}
