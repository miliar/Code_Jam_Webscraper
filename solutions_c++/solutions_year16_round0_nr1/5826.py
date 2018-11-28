#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

bool numSeen[10];

void updateNumSeen(int K){
	while(K!=0){
		numSeen[K%10] = 1;
		K/=10;
	}
}

bool allFound(){
	bool all = true;
	for(int i = 0; i < 10; i++){
		all = all && numSeen[i];
	}
	return all;
}



int main(){
	int T, N;
	cin >> T;
	for(int k = 1; k <= T; k++){
		memset(numSeen, 0, sizeof(bool) * 10);
		cin >> N;
		if(N == 0){
			printf("Case #%d: INSOMNIA\n",k);
		}else{
			int i = 1;
			while(!allFound()){
				updateNumSeen(i * N);
				i++;
			}
			printf("Case #%d: %d\n",k,(i-1)*N);
		}
	}
	return 0;
}
