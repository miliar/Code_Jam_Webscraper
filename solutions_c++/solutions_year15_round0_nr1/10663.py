#include <stdio.h>
#include <cstdlib>

using namespace std;

int main(){

	long long T, S, up, add, lack;
	char level[1001];

	scanf("%lld", &T);

	for(long long i = 1; i <= T; i++){
		scanf("%lld %s", &S, level);
		up = 0;
		add = 0;
		for(long long j = 0; j <= S; j++){
			if(level[j] != '0'){
				if(up >= j){
					up += (long long)(level[j] - 48);
				}else{
					lack = j - up;
					for(long long k = 0; k <= S; k++){
						if((9 - (long long)(level[k] - 48)) >= lack){
							add += lack;
							level[k] += lack;
							up += lack + (long long)(level[j] - 48);
							break;
						}else{
							lack -= (long long)(57 - level[k]);
							up += (long long)(57 - level[k]) + (long long)(level[j] - 48);
							add += (long long)(57 - level[k]); 
							level[k] = '9';
						}
					}
				}
			}
		}
		printf("Case #%lld: %lld\n", i, add);
	}


	return 0;
}