#include<stdio.h>
#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int search(int a[], int n, int num, int mid)
{
	int f[1001];
	int index = 0;
	for(int i = 0;i < n;i++) {
		if(a[i] <= mid) {
			;
		}else {
			f[index] = a[i] - mid;
			index++;
		}
	}
	
	/*
	for(int i = 0;i < index;i++) {
		cout << f[i];
	}
	
	*/
	for(int i = 0;i < index;i++) {
		if(f[i] > 0 && num <= 0) {
			return 0;
		}
		if(f[i] <= mid) {
			num--;
		}else {
			f[i] -= mid;
			num--;
			i--;
		}
	}
	return 1;
}
int binary_search(int low, int high, int a[])
{
	int r;
	while(low < high) {
		int mid = low + (high - low)/2;
		if(a[mid] < r) {
			low = mid+1;
		}else if(a[mid] > r) {
			high = low-1;
		}else {
			return 1;
		}
	}
}
int main()
{
	//freopen("1.in", "r", stdin);
	//freopen("2.txt", "w", stdout);
	
	int cases;
	
	scanf("%d", &cases);
	
	for(int i1 = 1;i1 <= cases;i1++) {
		int d;
		scanf("%d", &d);
		int a[1001];
		int local = -1;
		
		int f[1001] = {0};
		
		for(int i = 0;i < d;i++) {
			scanf("%d", &a[i]);
			if(local < a[i]) {
				local = a[i];
			}
		}
		
		//cout << local << endl;
		int ans = 10000000;
		for(int i = 0;i <= 1000;i++) {
			int low = 1;
			int high = 1000;
			while(low < high) {
				int mid = low + (high-low)/2;
				int t = search(a, d, i, mid);
				//cout << t << endl;
				if(t == 1) {
					high = mid;
				}else {
					low =  mid+1;
				}
			}
			//cout << ans << endl;
			if(i + low < ans) {
				//cout << i << " " << low <<endl;
				ans = i + low;
			}
			//cout << high << endl;
		}
		printf("Case #%d: %d\n", i1, ans);
	}
}
