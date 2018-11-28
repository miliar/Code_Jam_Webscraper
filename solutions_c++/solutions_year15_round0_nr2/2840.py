#include <stdio.h>
#include <queue>
#include <algorithm>

int T,D,P[1010];

int main(){
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		scanf("%d",&D);
		for(int i=0;i<D;++i){
			scanf("%d",P+i);
		}
		int res=1010;
		for(int k=1;k<=1000;++k){
			std::priority_queue<int> vela;
			for(int i=0;i<D;++i){
				if (P[i]>k) vela.push(P[i]-k);
			}
			int total=k;
			while(vela.size()){
				++total;
				int x=vela.top();
				vela.pop();
				if (x>k) vela.push(x-k);
			}
			if (total<res) res=total;
		}
		printf("Case #%d: %d\n",t,res);
	}
	return 0;
}
