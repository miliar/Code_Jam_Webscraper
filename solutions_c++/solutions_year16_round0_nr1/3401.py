#include <bits/stdc++.h>
using namespace std;

int T, TC = 1, N;
bool isVis[15];
bool cek(){
	for(int i = 0; i < 10; i++)
		if(!isVis[i]) return 0;
	return 1;
}
void ubah(long long x){
	while(x > 0){
		isVis[x%10] = 1;
		x /= 10;
	}
}
int main(){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	while(T--){
		scanf("%d", &N);
		if(N == 0) printf("Case #%d: INSOMNIA\n", TC++);
		else{
			long long cur = N;
			memset((isVis), 0, sizeof(isVis));
			ubah(cur);
			while(!cek()){
				cur += (long long)N;
				ubah(cur);
			}
			printf("Case #%d: %lld\n", TC++, cur);
		}
	}
	return 0;
}
