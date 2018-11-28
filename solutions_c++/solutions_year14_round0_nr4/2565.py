//authr : wiragotama@gmail.com    prob D deceitful war
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int n, t;
	scanf("%d",&t);
	for (int z=1; z<=t; z++) {
		scanf("%d",&n);
		double arr[n];
		bool flag1[n];
		memset(flag1,true,sizeof(flag1));
		double brr[n];
		bool flag2[n];
		memset(flag2,true,sizeof(flag2));
		
		for (int i=0; i<n; i++) {
			scanf("%lf",&arr[i]);
		}
		for (int i=0; i<n; i++) {
			scanf("%lf",&brr[i]);
		}
		
		sort(arr,arr+n);
		sort(brr,brr+n);
		
		long d_win = 0;
		for (int i=0; i<n; i++) {
			bool stop = false;
			for (int j=0; j<n && !stop; j++) {
				if (arr[i]>brr[j] && flag2[j]) {
					flag2[j] = false;
					stop = true;
				}
			}
			if (stop) d_win++;
		}
		
		long w_win = 0;
		for (int i=0; i<n; i++) {
			bool stop = false;
			for (int j=0; j<n && !stop; j++) {
				if (brr[i]>arr[j] && flag1[j]) {
					flag1[j] = false;
					stop = true;
				}
			}
			if (stop) w_win++;
		}
		w_win = n - w_win;
		
		printf("Case #%d: %ld %ld\n",z,d_win,w_win);
	}
	return 0;
}
