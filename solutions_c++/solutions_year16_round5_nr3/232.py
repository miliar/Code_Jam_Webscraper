#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cmath>
#define MAXN 101000

using namespace std;

struct Node{
	int x, y, z;
}a[MAXN];

int q[MAXN], dis[MAXN];
bool visit[MAXN], touch[MAXN];

int dis2(Node &n1, Node &n2){
	int x = n1.x - n2.x;
	int y = n1.y - n2.y;
	int z = n1.z - n2.z;
	return (x * x + y * y + z * z);
}

void solve(){
	int n,l;
	cin >> n >> l;
	for (int i = 1; i <= n; ++i)
	{
		cin >> a[i].x >> a[i].y >> a[i].z;
		cin >> a[0].x >> a[0].y >> a[0].z;
	}
	for (int i = 1; i <= n; ++i){
		touch[i] = false;
		visit[i] = false;
	}
	int head = 0, tail = 1;
	q[head] = 1;
	touch[1] = true;
	dis[1] = 0;
	while (head != tail){
		int x = q[head];
		head = head + 1;
		if (head >= n) head = 0;
		for(int j = 1; j <= n; ++j) {
			int tmp = max(dis[x], dis2(a[j], a[x]));
			if(!touch[j] || dis[j] > tmp){
				dis[j] = tmp;
				touch[j] = true;
				if(!visit[j]){
					q[tail] = j;
					visit[j] = true;
					if(++tail >= n) tail = 0;
				}
			}
		}
		visit[x] = false;
	}
	printf("%.10f\n", sqrt((double)dis[2]));
}


int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i){
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
