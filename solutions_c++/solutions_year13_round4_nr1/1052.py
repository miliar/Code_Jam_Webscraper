#include <cstdio>
#include <algorithm>

typedef long long ll;

struct travel {
	ll start, end, cnt;

	bool operator < (const travel &t) const {
		return start < t.start;
	}
};

struct ep {
	ll end, cnt;

	bool operator < (const ep &t) const {
		return end < t.end;
	}
};

const int MAX=1020;
travel data[MAX];
ep end[MAX];

ll n;
int m;

ll get(ll dist){
	return n*(n+1)/2 - (n-dist)*(n-dist+1)/2;
}

void input(){
	scanf("%lld%d", &n, &m);

	int i;
	for(i=0; i<m; i++){
		scanf("%lld%lld%lld", &data[i].start, &data[i].end, &data[i].cnt);
		end[i].end = data[i].end;
		end[i].cnt = data[i].cnt;
	}
}

void solve(){
	std::sort(end, end+m);
	std::sort(data, data+m);

	ll res=0;

	int i, j;
	for(i=0; i<m; i++){
		for(j=m-1; j>=0 && end[i].cnt; j--){
			if(data[j].start <= end[i].end){
				ll t = std::min(data[j].cnt, end[i].cnt);
				data[j].cnt -= t;
				end[i].cnt -= t;

				res += (get(data[j].end-data[j].start)-get(end[i].end-data[j].start))*t;
			}
		}
	}

	printf("%lld\n", res);
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, cc;
	scanf("%d", &cc);
	for(t=1; t<=cc; t++){
		printf("Case #%d: ", t);

		input();
		solve();
	}

	return 0;
}