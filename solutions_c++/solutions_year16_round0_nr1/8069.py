#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

typedef long long LL;

int b[10];

int check(LL x){
	while (x) {
		b[x%10] = 1;
		x /= 10;
	}
	for (int i = 0; i < 10; ++i) {
		if (!b[i]) return 0;
	}
	return 1;
}

void resolve(int id){
	LL x;
	cin >> x;
	memset(b, 0, sizeof(b));
	if (x == 0) {
		printf("Case #%d: INSOMNIA\n", id);
		return ;
	}
	for (int i = 1; i < 1000; ++i) {
		LL y = i * x;
		if (check(y)) {
			printf("Case #%d: ", id);
			cout << y << endl;
			return;
		}
	}
}

int main(){
	freopen("A-large.in", "r", stdin);
	
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		resolve(i);
	}
	fclose(stdout);
	fclose(stdin);
	return 0;
}
