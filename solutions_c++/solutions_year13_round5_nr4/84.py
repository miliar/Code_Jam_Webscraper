#include <cstdio>
#include <cstring>

double dp[1<<20];
bool done[1<<20];

inline int nex(int i, int len){
	return i == 0? len - 1: i - 1;
}

double mkdp(int sta, int len){

	if(sta == (1 << len) - 1) return 0;
	if(done[sta]) return dp[sta];

	double ret = 0;

	int to[20];
	for(int i = 0; i < len; i++){
		if(sta & (1 << i)) continue;
		to[i] = i;
		for(int j = nex(i, len); sta & (1 << j); j = nex(j, len)) to[j] = i;
	}
	for(int i = 0; i < len; i++){
		int cst = to[i] - i;
		if(cst < 0) cst += len;
		ret += cst + mkdp(sta | (1 << to[i]), len);
	}

	done[sta] = 1;
	return dp[sta] = ret / len;

}

int main(){

	int T;
	scanf("%d" ,&T);

	for(int t = 1; t <= T; t++){

		char buf[123];
		scanf("%s" ,buf);

		int init = 0, len = 0, cnt = 0;
		while(buf[len]){
			if(buf[len] == 'X') init |= (1 << len);
			else cnt++;
			len++;
		}
		memset(done, 0, sizeof(bool) * (1 << len));

		printf("Case #%d: %.9f\n" ,t,cnt * len - mkdp(init, len));

	}

}
