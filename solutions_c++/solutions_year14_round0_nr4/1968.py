#include <iostream>
#include <algorithm>

using namespace std;

int n,decieve,norm;
double a[1000],b[1000];
bool stata[1000],statb[1000];
void simulate() {
	decieve=0;
	norm=0;
	for(int i=0;i<n;++i) {
		double *up=upper_bound(a,a+n,b[i]);
		if(up-a==n) break;
		if(!stata[up-a]) {
			while(!stata[up-a] && (up-a)<n) ++up;
			if((up-a)==n) break;
		}
		++decieve,stata[up-a]=0;
	}
	for(int i=0;i<n;++i) {
		double *up=upper_bound(b,b+n,a[i]);
		if(up-b==n) break;
		if(!statb[up-b]) {
			while(!statb[up-b] && (up-b)<n) ++up;
			if((up-b)==n) break;
		}
		++norm,statb[up-b]=0;
	}
}

int main() {
	int t;
	cin>>t;
	for(int testcase=1;testcase<=t;++testcase) {
		cin>>n;
		for(int i=0;i<n;++i) cin>>a[i],stata[i]=1;
		for(int i=0;i<n;++i) cin>>b[i],statb[i]=1;
		sort(a,a+n);
		sort(b,b+n);
		simulate();
		cout<<"Case #"<<testcase<<": "<<decieve<<" "<<n-norm<<"\n";
	}
	return 0;
}
