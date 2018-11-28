#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;

int main(){
	int times;
	scanf("%d", &times);
	for (int t=0; t<times; t++){
		int base;
		long long now = 0;
		int arr[100], cnt;
		memset(arr, 0, sizeof(arr));
		cnt = 10;
		scanf("%d", &base);
		for (int k=0; k<10000 && cnt>0; k++){
			now += base;
			long long tmp = now;
			while (tmp > 0){
				int dig = tmp % 10;
				tmp /= 10;
				if (arr[dig]++==0){
					cnt--;
				}
			}
		}
		if (cnt > 0)
			printf("Case #%d: INSOMNIA\n", t+1, now);
		else
			printf("Case #%d: %lld\n", t+1, now);
	}
	return 0;
}
