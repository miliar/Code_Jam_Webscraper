#include <algorithm>
#include <stdio.h>
#include <vector>

using namespace std;

int main(){
	int T,N,S1,S2,rate;
	vector<int> mushroom(100,0);
	freopen("A-large.in.txt", "r", stdin);
	freopen("out", "w", stdout);
	scanf("%d",&T);
	for(int i=0; i<T; i++){
		S1 = S2 = rate = 0;
		printf("Case #%d: ",i+1);
		scanf("%d",&N);
		for(int j=0; j<N; j++){
			scanf("%d",&mushroom[j]);
			if(j>0 && mushroom[j-1]>mushroom[j]){
				S1 += mushroom[j-1]-mushroom[j];
				rate = max(rate,mushroom[j-1]-mushroom[j]);
			}
		}
		for(int j=0; j<N-1; j++){
			S2 += min(mushroom[j],rate);
		}
		printf("%d %d\n",S1,S2);
	}
	return 0;
}