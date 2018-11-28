#include <algorithm>
#include <cstdio>
#include <cstring>
#define ms(a) memset(a, 0, sizeof a)
using namespace std;
int T, N, a[22], b[22], ans[22], tmp[22], hsh[22], lis[22], lds[22], flag, caseCnt;
void dfs(int x){
	if(x > N){
		for(int i= N;i>= 1;-- i){
			lds[i]= 1;
			for(int j= N;j> i;-- j) if(ans[i] > ans[j])
				lds[i]= max(lds[i], lds[j]+1);
			if(lds[i] != b[i])
				return;
		}
		flag= 1;
	}else{
		for(int i= 1;i<= N;++ i) if(!hsh[i]){
			hsh[i]= 1;
			ans[x]= i;
			lis[x]= 1;
			for(int j= 1;j< x;++ j)
				if(ans[x] > ans[j]){
					lis[x]= max(lis[x], lis[j]+1);
					if(lis[x] > a[x])
						break;
				}
//			puts("ori"); for(int j= 1;j<= x;++ j) printf("%d ", ans[j]); puts("");
//			puts("lis"); for(int j= 1;j<= x;++ j) printf("%d ", lis[j]); puts("");
			if(lis[x] == a[x]){
				dfs(x+1);
				if(flag)
					return;
			}
			hsh[i]= 0;
			lis[x]= 0;
			ans[x]= 0;
		}
	}
}
int main(){
	scanf("%d", &T);
	while(T --){
		ms(a); ms(b); ms(ans); ms(tmp); ms(hsh); ms(lis); ms(lds); flag= 0;
		scanf("%d", &N);
		for(int i= 1;i<= N;++ i)
			scanf("%d", a+i);
		for(int i= 1;i<= N;++ i)
			scanf("%d", b+i);
		dfs(1);
		printf("Case #%d: ", ++ caseCnt);
		for(int i= 1;i<= N;++ i)
			printf(i==N ? "%d\n" : "%d ", ans[i]);
	}
	return 0;
}
