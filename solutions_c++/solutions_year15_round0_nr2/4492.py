#include<stdio.h>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<iomanip>
#include<functional>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<limits>
#include<climits>
using namespace std;

#define INF 9876543210
int tc, n;
vector<int> p;
void pre()
{
	for (int i = 0; i <= 32; i++)
		p.push_back(i*i);
}
int main()
{
#ifdef _CONSOLE
	//freopen("input.txt", "r", stdin);
	freopen("C:\\Users\\Sangyun\\Desktop\\input.in", "r", stdin);
	freopen("C:\\Users\\Sangyun\\Desktop\\out.out", "w+", stdout);
#endif
	////////////////////////////////////////////////////// 
	scanf("%d", &tc);
	pre();
	for (int i = 1; i <= tc; i++)
	{
		int res = INF;
		scanf("%d", &n);
		priority_queue <int> pq;
		priority_queue <int> pq2;
		for (int i = 0; i < n; i++)
		{
			int num; scanf("%d", &num);
			pq.push(num);
			pq2.push(num);
		}
		int cnt = 0;
		while (!pq.empty())
		{
			int here = pq.top();
			//cout << here << ' ' << cnt + here << endl;
			res = min(res, cnt + here);
			if (here == 1 || here == 0) break;
			pq.pop();
			int div = lower_bound(p.begin(), p.end(), here)- p.begin();
			//cout << *lower_bound(p.begin(), p.end(), here) << endl;
			//cout << here << ' ' << div << endl;
			pq.push(here - div);
			if (here-div > 0)
				pq.push(div);
			
			cnt++;
		}
		cnt = 0;
		while (!pq2.empty())
		{
			int here = pq2.top();
			res = min(res, cnt + here);
			if (here == 1) break;
			pq2.pop();
			int half = here / 2;
			pq2.push(half);
			if (here - half != 0)
				pq2.push(here - half);
			cnt++;
		}
		printf("Case #%d: %d\n", i, res);
	}
}