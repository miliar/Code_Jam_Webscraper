#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdlib>
#define maxn 1010
#define mod 1000000007
using namespace std;

struct Node{
	int x1, x2, y1, y2;
}a[maxn];

int d[maxn], dui[maxn], first[maxn];
bool visit[maxn];
int nxt[maxn * maxn], en[maxn * maxn], q[maxn * maxn], tot;

void tjb(int x, int y, int z){
	nxt[++tot] = first[x];
	first[x] = tot;
	en[tot] = y;
	q[tot] = z;
}

int dis(int l1, int r1, int l2, int r2){
	int l = max(l1, l2), r = min(r1, r2);
	if(l <= r) return 0;
	return min(abs(l1 - r2), abs(l2 - r1));
}

int dis(const Node &n1, const Node &n2){
	int minx = dis(n1.x1, n1.x2, n2.x1, n2.x2);
	int miny = dis(n1.y1, n1.y2, n2.y1, n2.y2);
	return max(minx, miny);
}

void solve(){
	int w, n, s, t, head, tail, x, k, j;
	scanf("%d%*d%d", &w, &n);
	s = n + 1; 
	t = s + 1;
	for(int i = 1; i <= t; ++i) first[i] = 0;
	tot = 0;
	for(int i = 1; i <= n; ++i){
		scanf("%d%d%d%d", &a[i].x1, &a[i].y1, &a[i].x2, &a[i].y2);
		++a[i].x2; ++a[i].y2;
		tjb(s, i, a[i].x1);
		tjb(i, t, w - a[i].x2);
	}
	for(int i = 1; i <= n; ++i)
		for(int j = 1; j <= n; ++j) if(i != j) tjb(i, j, dis(a[i], a[j]));
	for(int i = 1; i <= t; ++i){
		d[i] = mod;
		visit[i] = false;
	}
	d[s] = 0;
	d[t] = w;
	visit[s] = true;
	head = 0; tail = 1;
	dui[tail] = s;
	while(head != tail){
		if(++head == t) head -= t;
		x = dui[head];
		k = first[x];
		while(k != 0){
			j = en[k];
			if(d[j] > d[x] + q[k]){
				d[j] = d[x] + q[k];
				if(!visit[j]){
					visit[j] = true;
					if(++tail == t) tail -= t;
					dui[tail] = j;
				}
			}
			k = nxt[k];
		}
		visit[x] = false;
	}
	printf("%d\n", d[t]);
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i){
		printf("Case #%d: ", i);
		solve();
	}
}