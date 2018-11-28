#include<iostream>

using namespace std;

int t,x,n,m;
string s1,s2,ans;
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>t;
	s1 = "Gabriel";
	s2 = "Richard";
	for (int i = 1;i <= t;i++) {
		cin>>x>>n>>m;
		if (n > m) swap(m,n);
		if (x == 1) ans = s1;
		if (x == 2) {
			if ((n * m) % x == 0) ans = s1; else ans = s2;
		}
		if (x == 3) {
			if (n == 1 || (n * m) % x != 0) ans = s2; else ans = s1;
		}
		if (x == 4) {
			if (n < 3 || (n * m) % x != 0) ans = s2; else ans = s1;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	
	return 0;
}
