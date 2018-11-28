#include<bits/stdc++.h>
using namespace std;

int main() {
	int t,m,n;
	int a[5][5],b[5][5];
	cin>>t;
	int temp = 1;
	while(t--) {
		int n;
		cin>>n;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				cin>>a[i][j];
			}
		}
		cin>>m;
		for(int i = 0 ;i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				cin>>b[i][j];
			}
		}
		int count = 0;
		int ans = 0;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(a[n-1][i] == b[m-1][j]) {
					count++;
					ans = a[n-1][i];
					break;
				}
			}
		}
		if(count == 1) {
			printf("Case #%d: %d\n",temp,ans);
		} else if(count > 1) {
			printf("Case #%d: Bad magician!\n",temp);
		} else {
			printf("Case #%d: Volunteer cheated!\n",temp);
		}
		temp++;
	}
	return 0;
}
