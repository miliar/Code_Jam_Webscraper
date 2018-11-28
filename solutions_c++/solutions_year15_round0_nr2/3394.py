#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;
typedef long long lld;
int main () {
	int t,T;
	cin>>t;
	T=t;
	while (t--) {
		lld d, res=INT_MAX, cnt = 0;
		cin>>d;
		vector<lld> a(d);
		for (int i = 0; i < d; i++)
			cin>>a[i];
		for (int i = 1; i <=1000; i++) {
			cnt = 0;
			for (int j = 0; j < d; j++) {
				if (a[j] %i == 0)
					cnt += a[j]/i - 1;
				else
					cnt += a[j]/i;
			}
			res = min (res, cnt + i);
		}
		cout<<"Case #"<<T-t<<": "<<res<<"\n";
	}
	return 0;
}
