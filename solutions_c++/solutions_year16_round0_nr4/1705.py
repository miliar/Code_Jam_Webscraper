#include<cstdio>
#include<algorithm>

using namespace std;

int casos, K, C, S;

int main(){
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
		scanf(" %d %d %d", &K, &C, &S);
		if(K == S){
			printf("Case #%d:", inst);
			for(int i=1;i<=K;i++) printf(" %d", i); printf("\n");
		}
		else{
		}
	}
	return 0;
}