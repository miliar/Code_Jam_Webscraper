#include<cstdio>
#include<cstring>
unsigned long long num;
bool check[10];
int T;
bool chk(){
	for (int i = 0; i <= 9; i++){
		if (!check[i])
			return false;
	}
	return true;
}
void counting(int t, unsigned long long n){
	int j = 1;
	if (n == 0){
		printf("Case #%d: INSOMNIA\n", t);
		return;
	}
	while (1){
		unsigned long long temp = n * j;
		j++;
		while (temp / 10 != 0 || temp % 10 != 0){
			check[temp % 10] = true;
			temp /= 10;
		}
		if (chk() == true){
			printf("Case #%d: %llu\n",t, n * (j-1));
			return;
		}
	}
}
int main(){
	freopen("testcaseA.txt", "r", stdin);
	freopen("outputA.txt", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%llu", &num);
		memset(check, 0, sizeof(check));
		counting(i,num);
	}
}