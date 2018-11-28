#include <iostream>
#include <cstdio>
#define NAME "b-small-attempt0"
using namespace std;
typedef long long ll;
int T;
int main(){
	freopen(NAME".in","rt",stdin);
	freopen(NAME".out","wt",stdout);
	cin>>T;
	for(int I=1;I<=T;I++) {
		printf("Case #%d: ",I);
		int a,b,k;
		cin>>a>>b>>k;
		int ans=0;
		for(int i=0;i<a;i++) {
			for(int j=0;j<b;j++) {
				if((i&j)<k) ans++;
			}
		}
		cout<<ans<<'\n';
	}
	return 0;
}