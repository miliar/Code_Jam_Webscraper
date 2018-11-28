#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

int main() {
	int T;
	cin>>T;
	for(int k=1;k<=T;k++) {
		int n, a[5002], b[2502],j=0,c[52];
		for(int i=0;i<2502;i++) b[i] = 0;
		cin>>n;
		int total = ((2*n) - 1) * n;
		for(int i=0;i<total;i++) {
			cin>>a[i];
			b[a[i]]++;
		}
		
		cout<<"Case #"<<k<<": ";
		for(int i=0;i<2502;i++) {
			if(b[i]%2 != 0) {
				c[j++] = i;
			}
		}
		sort(c,c+j);
		for(int i=0;i<j;i++) {
			cout<<c[i]<<" ";
		}
		cout<<endl;
	}
	return 0;
}
