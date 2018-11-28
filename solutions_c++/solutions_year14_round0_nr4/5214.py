#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int t;
	cin>>t;

	for(int k=1; k<=t; k++) {
		int n;
		cin>>n;
		float *naomi = new float[n];
		float *ken = new float[n];

		for(int i=0; i<n; i++) {
			cin>>naomi[i];
		}
		for(int i=0; i<n; i++) {
			cin>>ken[i];
		}

		sort(naomi, naomi+n);
		sort(ken, ken+n);

		int c1=n, c2=0;
		for(int i=n-1, j=n-1; i>=0 && j>=0; ) {
			if(naomi[i] < ken[j]) {
				i--;
				j--;
				c1--;
			} else {
				i--;
			}
		}

		for(int i1=0, i2=n-1, j=n-1; i1<=i2 && j>=0; ) {
			if(naomi[i2] > ken[j]) {
				c2++;
				j--;
				i2--;
			} else {
				j--;
				i1++;
			}
		}

		cout<<"Case #"<<k<<": "<<c2<<" "<<c1<<endl;
	}

	return 0;
}