#include <cstdio>

bool fg[1001];
inline bool isP(int k){
	int kk = 0;
	for(int i = k; i > 0; i /= 10){
		kk *= 10;
		kk += (i % 10);
	}
	return (k == kk);
}

int main(){
	for(int i = 1; i <= 1000; i++){
		fg[i] = false;
	}
	for(int i = 1; i * i <= 1000; i++){
		if(isP(i) && isP(i * i)){
			fg[i * i] = true;
		}
	}
	for(int a, b, T, t = (scanf("%d", &T), 1); t <= T; t++){
		scanf("%d %d", &a, &b);
		int ct = 0;
		for(int i = a; i <= b; i++){
			if(fg[i] == true){
				ct++;
			}
		}
		printf("Case #%d: %d\n", t, ct);
	}
	return 0;
}
