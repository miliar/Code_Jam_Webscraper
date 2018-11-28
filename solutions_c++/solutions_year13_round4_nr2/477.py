#include<stdio.h>

typedef long long int LL;
int N;
LL P;

bool Independence(LL strongerConut, int gameCount, LL rank){
	if(strongerConut <= 0){
		return rank < P;
	}
	else{
		return Independence((strongerConut-1)/2, gameCount+1, rank | (1LL<<(N-1 - gameCount)));
	}
}

bool Dependence(LL weakerConut, int gameCount, LL rank){
	if(weakerConut <= 0){
		return rank < P;
	}
	else{
		return Dependence((weakerConut-1)/2, gameCount+1, rank ^ (1LL<<(N-1 - gameCount)));
	}
}

int main() {
	int T, caseNum;
	scanf("%d",&T);

	for(caseNum=1; caseNum<=T; ++caseNum) {
		scanf("%d%lld",&N,&P);

		printf("Case #%d: ", caseNum);

		LL low, hi, mid;
		low = 0, hi = (1LL<<N);
		while(low < hi){
			mid = (low+hi)/2;
			if(Independence(mid, 0, 0)){
				low = mid+1;
			}
			else{
				hi = mid;
			}
		}
		printf("%lld ", low-1);

		low = 0, hi = (1LL<<N);
		while(low < hi){
			mid = (low+hi)/2;
			if(Dependence(((1LL<<N)-1-mid), 0, (1LL<<N)-1)){
				low = mid+1;
			}
			else{
				hi = mid;
			}
		}
		printf("%lld\n", low-1);
	}
	return 0;
}
