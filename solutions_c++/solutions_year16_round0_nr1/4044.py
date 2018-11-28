#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

bool finished(bool *found){
	bool output = true;
	for(int i = 0; i < 10; i++){
		output = output && found[i];
	}
	return output;
}

int main(){
	int t;
	scanf("%d",&t);
	for(int i = 0; i < t; i++) {
		printf("Case #%d: ", i+1);
		bool found[10];
		memset(found, false, 10);
		long long n, m;
		char buffer[64];
		scanf("%lld", &n);
		if(!n){
			printf("INSOMNIA\n");
			continue;
		}
		for(m = n; !finished(found); n += m){
			sprintf(buffer,"%lld",n);
			for(int j = 0; buffer[j]; j++){
				found[buffer[j]-48] = true;
			}
		}
		printf("%lld\n", n-m);
	}
	return 0;
}
