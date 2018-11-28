#include <algorithm>

using namespace std;

int N,A[1010];

void solve_case(){
	scanf("%d",&N);
	for(int i=0;i<N;++i){
		scanf("%d",A+i);
	}
	int vys=0;
	for(int i=0;i<N;++i){
		int a=0,b=0;
		for(int j=0;j<i;++j){
			if (A[j]>A[i]) ++a;
		}
		for(int j=i+1;j<N;++j){
			if (A[j]>A[i]) ++b;
		}
		vys+=min(a,b);
	}
	printf("%d\n",vys);
}

int main(){
	int cases;
	scanf("%d",&cases);
	for(int t=1;t<=cases;++t){
		printf("Case #%d: ",t);
		solve_case();
	}
	return 0;
}

