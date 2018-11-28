#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#define FWD(a,b,c) for(int a=(b); a<(c); ++a)
#define BCK(a,b,c) for(int a=(b); a>(c); --a)
#define PII pair<int, int>
#define x first
#define y second

using namespace std;

typedef long long LL;

const LL mod = 1000002013;

int n, m, a, b, c;
vector<PII> V;
priority_queue<PII> tickets;
LL r;
PII t;

inline LL cost(LL d){
	return (d * (2LL*n-d+1LL) / 2LL) % mod;
}

int main(){
	int Z;
	scanf("%d", &Z);
	FWD(z,1,Z+1){
		r = 0;
		V.clear();
		while(!tickets.empty()) tickets.pop();
		scanf("%d %d", &n, &m);
		FWD(i,0,m){
			scanf("%d %d %d", &a, &b, &c);
			r = (r + (LL)c * cost(b-a)) % mod;
			V.push_back(PII(a,-c));
			V.push_back(PII(b,c));
		}
		sort(V.begin(), V.end());
		FWD(i,0,(int)V.size()){
			a = V[i].x;
			c = V[i].y;
			if(c < 0){
				//printf("in %d %d\n", a, -c);
				tickets.push(PII(a, -c));
			}else{
				//printf("out %d %d\n", a, c);
				while(c){
					t = tickets.top();
					tickets.pop();
					r = (r - ((LL)min(t.y, c)) * cost(a - t.x)) % mod;
					//printf("najlepiej to %d z %d za %d po %lld\n", t.y, t.x, min(t.y, c), cost(a - t.x));
					if(t.y > c){
						t.y -= c;
						tickets.push(t);
						c = 0;
					}else{
						c -= t.y;
					}
				}
			}
		}
		printf("Case #%d: %lld\n", z, (r+mod)%mod);
	}
}

