#include <bits/stdc++.h>
using namespace std;
const int N=1000000+1;
long long mask[N],ans[N];
int t,n;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	for(int i=1;i<N;++i) {
		
		int j=1;
		long long k=i;
		while(mask[i]!=(1<<10)-1) {
			k=i*j;
			j++;
			long long ck=k;
			while(ck) {
				int d=ck%10;
				ck/=10;
				mask[i]|=(1<<d);
			}
		}
		//cout << i << " " << mask[i] << "\n";
		ans[i]=1LL*i*(j-1);

	}
	cin>>t;
	int ti=1;
	while(t--) {
		cout<<"Case #"<<ti<<": ";
		ti++;
		cin>>n;
		if(!n) {
			cout<<"INSOMNIA\n";
		} else {
			cout<<ans[n]<<"\n";
		}
	}
	return 0;
}
