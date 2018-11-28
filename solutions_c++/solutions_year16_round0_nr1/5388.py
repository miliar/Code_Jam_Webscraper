#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	int i,j,T,N,ans,tp,rem;
	cin>>T;
	for(i=1;i<=T;i++) {
		unordered_set<int> foo = {0,1,2,3,4,5,6,7,8,9};
		cin>>N;
		if(N==0) {
			cout<<"Case #"<<i<<": INSOMNIA\n";
			continue;
		}
		j=1;
		while(1) {
			ans=j*N;
			tp=ans;
			while(tp) {
				rem=tp%10;
				foo.erase(rem);
				tp/=10;
			}
			if(foo.size()==0)
				break;
			j++;
		}
		cout<<"Case #"<<i<<": "<<ans<<"\n";
	}
	return 0;
}