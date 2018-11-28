#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const int MAX = 100;

int main() {
	freopen("inputB.in", "r", stdin);
	freopen("outputB", "w", stdout);
	int t; cin>>t;
	int n, m;
	int a[MAX][MAX], rowmax[MAX], columnmax[MAX];
	for(int i1 = 1; i1 <= t; ++i1) {
		memset(rowmax, 0, sizeof(int) * MAX);
		memset(columnmax, 0, sizeof(int) * MAX);
		cout<<"Case #"<<i1<<": ";
		bool yes = true;
		int n, m;
		cin>>n>>m;
		for(int i2 = 0; i2 < n; ++i2) 
			for(int i3 = 0; i3 < m; ++i3) {
				scanf("%d", &a[i2][i3]);
				rowmax[i2] = rowmax[i2] > a[i2][i3] ? rowmax[i2] : a[i2][i3];
				columnmax[i3] = columnmax[i3] > a[i2][i3] ? columnmax[i3] : a[i2][i3];
			}
		for(int i2 = 0; i2 < n; ++i2) 
			for(int i3 = 0; i3 < m; ++i3) {
				if(a[i2][i3] < rowmax[i2] && a[i2][i3] < columnmax[i3]) {
					yes = false;
				}
			}
label: 
		if(yes) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
}
