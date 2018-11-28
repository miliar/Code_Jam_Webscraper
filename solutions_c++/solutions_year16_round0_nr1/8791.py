#include <bits/stdc++.h>
using namespace std;

int main() {

	freopen("A-large.in","r",stdin);
	freopen("output_file.out","w",stdout);
	int t;
	scanf ("%d", &t);
	int a;
	for (a = 1; a <= t; a++) {
		long long num;
		scanf("%lld",&num);
		map<int , int > M;
		int count = 0 ;
		long long tmp;
		long long d;
		long long ct = 1;
		long long j = 0 ;
		for (tmp = num; 1; tmp = ct * num) {
			count = 0 ;
			while (tmp) {
				d = tmp % 10;
				tmp = tmp/10;
				M[d]++;
			}
			
			for (j = 0; j < 10; j++) {
				if(M[j] == 0){
					count++;
					break;
				}
			}
			//printf("%d\n", count);
			if (count == 0) {
				printf("Case #%d: %lld\n",a, ct*num);
				break;
			}else {
				if (ct*num > 100000000000000000 || ct*num == 0){
					printf("Case #%d: INSOMNIA\n", a);
					break;
				}
			}
			
			ct++;
		}
		
		M.clear();
		
	}
	return 0;
}
