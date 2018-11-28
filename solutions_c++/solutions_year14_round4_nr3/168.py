#include <bits/stdc++.h>

#define FWD(a,b,c) for(int a=(b); a<(c); ++a)
#define SIZE(a) ((int)a.size())
#define pb push_back
#define PII pair<int, int>
#define x first
#define y second

using namespace std;

typedef long long LL;
const int INF = 1000000000;

struct building{
	int x0, y0, x1, y1;
	void read(){
		scanf("%d %d %d %d", &x0, &y0, &x1, &y1);
		++x1;
		++y1;
	}
	PII corner(int k) const {
		return PII((k&1)?x1:x0, (k&2)?y1:y0);
	}
};

int dist(const PII &a, const PII &b){
	return max(abs(a.x-b.x), abs(a.y-b.y));
}

int dist(const building &a, const building &b){
	int d = INF;
	FWD(i,0,4)
		FWD(j,0,4)
			d = min(d, dist(a.corner(i), b.corner(j)));
	FWD(i,0,4){
		PII c = a.corner(i);
		if(b.x0 <= c.x && c.x <= b.x1)
			d = min(d, min(abs(b.y0 - c.y), abs(b.y1 - c.y)));
		if(b.y0 <= c.y && c.y <= b.y1)
			d = min(d, min(abs(b.x0 - c.x), abs(b.x1 - c.x)));
	}
	FWD(i,0,4){
		PII c = b.corner(i);
		if(a.x0 <= c.x && c.x <= a.x1)
			d = min(d, min(abs(a.y0 - c.y), abs(a.y1 - c.y)));
		if(a.y0 <= c.y && c.y <= a.y1)
			d = min(d, min(abs(a.x0 - c.x), abs(a.x1 - c.x)));
	}
	return d;
}

int w, h, b;
building B[1010];
int D[1010][1010];
priority_queue<PII> Q;
int R[1010];

int main(){
	int Z; scanf("%d", &Z); FWD(z,1,Z+1){
		scanf("%d %d %d", &w, &h, &b);
		B[0] = building({0,0,0,h});
		FWD(i,1,b+1) B[i].read();
		B[b+1] = building({w,0,w,h});
		b += 2;
		FWD(i,0,b)
			FWD(j,0,b){
				D[i][j] = dist(B[i], B[j]);
			}
		FWD(i,0,b) R[i] = INF;
		Q.push(PII(0,0));
		while(!Q.empty()){
			int u = Q.top().y;
			int d = -Q.top().x;
			Q.pop();
			if(R[u] != INF) continue;
			R[u] = d;
			FWD(v,0,b)
				Q.push(PII(-d-D[u][v], v));
		}
		printf("Case #%d: %d\n", z, R[b-1]);
	}
	return 0;
}
