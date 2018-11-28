#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
#include <ctime>
using namespace std;

#define LL long long

const int MAXN = 102;

LL inp[MAXN];

struct node{
	LL sum;
	int idx, stp;
};
node cur, nxt;

struct cmp{
	bool operator() (const struct node &a, const struct node &b){
		//if(a.stp == b.stp) return (a.sum < b.sum);
		//return (a.stp > b.stp);
		return a.sum < b.sum;
	}
};
priority_queue<struct node, vector<struct node>, cmp>que;

set<LL>stx;

inline int getmin(int a, int b){
	return a < b ? a : b;
}

inline int getmax(int a, int b){
	return a > b ? a : b;
}

bool cmp(const int a, const int b){
	return a > b;
}


int main(){
	//freopen("in.txt", "r", stdin);
	freopen("A-small-attempt4.in", "r", stdin);
	freopen("A-small-attempt4.out", "w", stdout);
	//LL time1 = clock();

	int T, cases;
	LL x0;
	int N, ret;
	LL sum;
	int idx, stp;
	scanf("%d", &T);
	for(cases=1; cases<=T; ++cases){
		scanf("%lld%d", &x0, &N);
		for(int i=0; i<N; ++i){
			scanf("%lld", &inp[i]);
		}
		if(x0 == 1){
			printf("Case #%d: %d\n", cases, N);
			continue;
		}
		sort(inp, inp+N);
		ret = N;

		while(!que.empty())que.pop();
		//stx.clear();
		cur.sum = x0;
		cur.idx = -1;
		cur.stp = 0;
		que.push(cur);
		//stx.insert(cur.sum);
		while(!que.empty()){
			cur = que.top();
			que.pop();
			sum = cur.sum;
			idx = cur.idx;
			stp = cur.stp;
			if(idx == N-1){
				ret = getmin(ret, stp);
				continue;
			}
			if(sum > inp[idx+1]){
				nxt.sum = sum + inp[idx+1];
				nxt.stp = stp;
				nxt.idx = idx + 1;
				//if(stx.find(nxt.sum) == stx.end()){
					que.push(nxt);
					//stx.insert(nxt.sum);
				//}
			}else{
				nxt.sum = sum;
				nxt.stp = stp + 1;
				nxt.idx = idx + 1;
				//if(stx.find(nxt.sum) == stx.end()){
					que.push(nxt);
					//stx.insert(nxt.sum);
				//}

				nxt.sum = sum + sum - 1;
				nxt.stp = stp + 1;
				nxt.idx = idx;
				//if(stx.find(nxt.sum) == stx.end()){
					que.push(nxt);
					//stx.insert(nxt.sum);
				//}

			}
		}
		printf("Case #%d: %d\n", cases, ret);
	}

	//printf("total time = %lld ms\n", clock()-time1);
	return 0;
}