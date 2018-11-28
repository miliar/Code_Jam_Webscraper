#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
	// your code goes here
	freopen("A-large.in","r",stdin);
	freopen("submit.txt","w",stdout);
	long long int i, j, k, n, t, ans, a[1002];
	char s[1002];
	cin>>t;
	k=1;
	while(t--) {
		j = 0;
		ans = 0;
		cin>>n>>s;
		for(i=0;i<=n;i++) {
			a[i] = s[i] - 48;
		}
		j = a[0];
		for(i=1;i<=n;i++) {
			if(j<i) {
				ans+=(i-j);
				j+=(i-j);
			}
			j+=a[i];
		}
		
		cout<<"Case #"<<k<<": "<<ans<<endl;
		k++;
	}
	return 0;
}
