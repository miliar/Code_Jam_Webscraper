#include <algorithm>
#include <stdio.h>
#include <vector>

using namespace std;

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out", "w", stdout);
	int N,S,c,M;
	scanf("%d",&N);

	for(int i=0; i<N; i++){
		printf("Case #%d: ", i+1);
		scanf("%d",&S);
		vector<int> audience(S+1,0);
		vector<int> count(S+1,0);
		c = 0;
		M = 0;
		for(int j=0; j<S+1; j++){
			scanf("%1d", &audience[j]);
			c+=audience[j];
			if(c >= 1000 || audience[j] >= 1000){
				break;
			}
			count[j] = c;
			if(j>0) M = max(M,j-count[j-1]);
		}
		printf("%d\n",M);
	}
	return 0;
}