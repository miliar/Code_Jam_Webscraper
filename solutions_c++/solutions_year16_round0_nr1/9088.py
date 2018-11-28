#include<cstdio>

using namespace std;

int t, n;
int ch[10];

bool check(long long a){
	while(a){
		ch[a%10]=1;
		a/=10;
	}
	for (int i = 0; i < 10; i++)
		if (ch[i]==0) return false;
	return true;
}

int main(){
	scanf("%d", &t);
	for (int tt = 1; tt<=t; tt++) {
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", tt);
			continue;
		}
		long long nn = n;
		for (int i = 0; i <10; i++)
			ch[i]=0;
		while(1){
			if (check(nn)){
				printf("Case #%d: %lld\n", tt, nn);
				break;
			}
			nn += n;
		}
	}
	return 0;
}
