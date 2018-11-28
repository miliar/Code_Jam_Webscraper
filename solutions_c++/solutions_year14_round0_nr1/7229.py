#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<list>
#include<cstdlib>
#include<ctime>
#include<cstring>

using namespace std;


int main() {
	int i, j, k, n, t, m;
	cin>>t;
	for(m = 1; m <= t; m++) {
		int a[5], b[5];
		cin>>n;
		j = 1;
		for(i = 1; i <= 16; i++) {
			cin>>k;
			if(i > 4*(n-1) && i <= 4*n) {
				a[j++] = k;
			}
		}
		cin>>n;
		j = 1;
		for(i = 1; i <= 16; i++) {
			cin>>k;
			if(i > 4*(n-1) && i <= 4*n) {
				b[j++] = k;
			}
		}
		int cnt = 0;
		for(i = 1; i <= 4; i++) {
			for(j = 1; j <= 4; j++) {
				if(a[i] == b[j]) {
					k = a[i];
					cnt++;
				}
			}
		}
		if(cnt > 1) {
			cout<<"Case #"<<m<<": Bad magician!\n";
		} else if(cnt < 1) {
			cout<<"Case #"<<m<<": Volunteer cheated!\n";
		} else {
			cout<<"Case #"<<m<<": "<<k<<"\n";
		}
	}
	return 0;
}