#include<cstdio>
#include<cstring>
char A[110];
int T;
void flip(int a){
	for (int i = 0; i <= a; i++){
		if (A[i] == '+')
			A[i] = '-';
		else
			A[i] = '+';
	}
}
void pan(int t, int k, int cnt){
	if (k < 0){
		printf("Case #%d: %d\n",t, cnt);
		return;
	}
	if (A[k] == '+')
		pan(t, k - 1, cnt);
	else{
		flip(k);
		pan(t, k - 1, cnt+1);
	}
}
int main(){
	freopen("testcaseB.txt", "r", stdin);
	freopen("outputB.txt", "w", stdout);
	scanf("%d", &T);
	for(int i=1;i<=T;i++){
		scanf("%s", A);
		pan(i, strlen(A) - 1, 0);
	}
}