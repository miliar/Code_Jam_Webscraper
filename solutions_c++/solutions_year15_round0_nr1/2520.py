#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll solve() {
	ll n;
	string s;
	cin>>n>>s;
	
	int standing = s[0]-'0';
	int ret = 0;
	int cur;
	//cout<<"standing = "<<standing<<", ret = "<<ret<<"\n";
	for(int i=1;i<n+1;i++) {
		cur = s[i] - '0';
		if(standing >= i) {
			standing += cur;
		}
		else if(standing < i && cur > 0){
			ret += (i - standing);
			standing += (i - standing);
			standing += cur;
		}
		//cout<<"standing = "<<standing<<", ret = "<<ret<<"\n";
	}
	return ret;
}

int main() {
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		cout << "Case #"<<i<<": "<<solve()<<"\n";
	}
}
