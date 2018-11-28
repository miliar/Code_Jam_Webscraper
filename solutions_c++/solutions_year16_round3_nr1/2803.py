#include<stdio.h>
#include<queue>
#include<vector>
#include<functional>
using namespace std;

class M{
public:
	int val;
	int p;
	M(int a, int b){
		val = a; p = b;
	}
	
	bool operator<(const M& other) const{
		return val < other.val;
	}
};

priority_queue<M> pq;

int main(){
	int t;	
	scanf("%d", &t);
	
	for(int T = 1; T <= t; T++){
		int n, p, sum = 0;
		scanf("%d", &n);
		
		for(int i = 0; i < n; i++){
			scanf("%d", &p);
			pq.push(*new M(p, i));
			sum += p;
		}
		
		printf("Case #%d: ", T);
		
		while(!pq.empty()){
			int tv = pq.top().val, tp = pq.top().p; pq.pop();
			
			tv--;
			sum--;
			printf("%c", tp + 'A');
			if(tv > 0)
				pq.push(*new M(tv, tp));
			
			if(!pq.empty()){
				tv = pq.top().val, tp = pq.top().p; pq.pop();
				if(pq.empty() || 1.0 * pq.top().val / (sum - 1) <= 0.5 || pq.top().val == (sum - 1)){
					tv--;
					sum--;
					printf("%c ", tp + 'A');
					if(tv > 0)
						pq.push(*new M(tv, tp));
				}
			}
		}
		
		printf("\n");
	}
}