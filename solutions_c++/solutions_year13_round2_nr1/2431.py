using namespace std;
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
int main() {
	int x,T,a,ans,y,N,c;
	long long int A;	
	cin>>T;
	for(x=0;x<T;x++) {
		cin>>A>>N;
		vector<int> mote;
		for(y=0;y<N;y++) {
			cin>>a;
			mote.push_back(a);
		}
		sort(mote.begin(),mote.end());
		ans = 0;
		for(y=0;y<N && A<=mote[N-1];y++) {
			if (A==1) {
				ans = N;
				break;
			}
			if(A>mote[y]) {
				// cout<<A<<" "<<mote[y]<<endl;
				A+=mote[y];
			} else {
				c=0;
				while (A<=mote[y]) {
					A+=A-1;
					c++;
				}
				if (c<N-y) {
				// cout<<A<<" "<<mote[y]<<" "<<c<<" "<<ans<<endl;
					ans+=c;
					A+=mote[y];
				// cout<<"Add "<<A<<" "<<mote[y]<<" "<<c<<" "<<ans<<endl;
				} else {
					ans+=N-y;
					break;
				}
			}
		}
		cout<<"Case #"<<x+1<<": "<<ans<<endl;
	}
	return 0;
}
