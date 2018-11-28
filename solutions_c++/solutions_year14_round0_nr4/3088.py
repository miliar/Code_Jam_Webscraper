#include<bits/stdc++.h>
using namespace std;

int main() {
	freopen("inn", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	int n;
	int temp = 1;
	
	while(t--) {
		cin>>n;
		double a[n + 1], b[n + 1];
		for(int i = 0; i < n; i++) {
			cin>>a[i];
		}
		for(int i = 0; i < n ; i++) {
			cin>>b[i];
		}
		sort(a,a+n);
		sort(b,b+n);
		/*for(int i = 0; i < n; i++) {
			cout<<a[i]<<" ";
		}printf("\n");
		for(int i = 0; i < n ; i++) {
			cout<<b[i]<<" ";
		}*/
		int count = 0;
		int i = 0; 
		int j = 0;
		while(i < n && j < n) {
			if(a[i] > b[j]) {
				count++;
				i++;
				j++;				
			} else  {
				i++;
			}
		}
		int count2 =0;
		int front1 = 0, end1 = n-1;
		int front2  = 0,end2 = n-1;
		for(i = 0; i < n; i++) {
			if(a[end1] > b[end2]) {
				count2++;
				end1--;
				front2++;
			} else {
				end2--;
				end1--;
			}
		}
		printf("Case #%d: %d %d\n",temp,count,count2);
		temp++;
	}
	return 0;
}
