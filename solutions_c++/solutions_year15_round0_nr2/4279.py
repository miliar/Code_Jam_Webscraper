#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <set>

using namespace std;

int t, n;
int a[1010];

int main() {
	// freopen("input.txt","r", stdin); 
	// freopen("output.txt","w", stdout);
	cin>>t;
	for (int x=0; x<t; x++) {
		cin>>n;
		for (int i=0; i<n; i++) {
			cin>>a[i];
		}
		sort(a,a+n);
		int res=a[n-1];
		for (int i=1; i<=a[n-1]; i++) {
			int sum=0;
			for (int j=0; j<n; j++) {
				if (a[j]>i) {
					sum+=a[j]/i-1;
					if (a[j]%i>0) sum++;
				}
			}
			res=min(res,sum+i);
		}
		printf("Case #%d: %d\n", x+1, res);
	}
	return 0;
}