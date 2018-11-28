#include <bits/stdc++.h>

using namespace std;

long long get_res(int n){
	int t = 0, check = 0;
	long long res;

	while (true){
		t ++;
		res = (long long) n * t;
		while (res != 0){
			check = (check | (1 << (res % 10)));
			res /= 10;
		}
		if (check == 1023){
			return (long long) t * n;
		}
	}
	return 0;
}

int main(){
	
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int test;
	int n;
	scanf("%d", &test);

	for (int i = 0; i < test; i++){
		scanf("%d", &n);

		if (n == 0)
			printf("Case #%d: INSOMNIA\n", i+1);
		else
			printf("Case #%d: %lld\n", i+1, get_res(n));
	}	
}