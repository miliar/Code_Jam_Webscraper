#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <queue>
using namespace std;
int minResult;
void dfs(int g, int b, priority_queue<short> pq){
	int m = pq.top();
	int count = 0;
	while (pq.top() == m){
		pq.push(pq.top() - b);
		pq.push(b);
		pq.pop();
		count++;
	}
	g += count;
	minResult = min(minResult, pq.top() + g);
	if (pq.top() == 1)
		return;
	int c = (pq.top()+ 1) / 2;
	for (int i = 1; i < pq.top(); ++i)
		dfs(g, i, pq);
}
void main(){
#ifdef TRAINING
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int T, D, a;
	scanf("%d", &T);
	for(int t = 1; t<=T; ++t){
		scanf("%d", &D);
		priority_queue<short> pq;
		for (int i = 0; i < D; ++i){
			scanf("%d", &a);
			pq.push(a);
		}
		//int minResult = pq.top(), count = 0;
		minResult = pq.top();
		for (int i = 1; i < pq.top(); ++i)
			dfs(0, i, pq);
		/*while (pq.top() != 1){
			int b = pq.top() / 2;
			if (pq.top() & 1 && !(b & 1)){
					pq.push(b - 1);
					pq.push(pq.top() - b + 1);
			}
			else{
				pq.push(pq.top() - b);
				pq.push(b);
			}
			pq.pop();
			count++;
			minResult = min(minResult, count + pq.top());
		}*/
		printf("Case #%d: %d\n", t, minResult);
	}
	
}