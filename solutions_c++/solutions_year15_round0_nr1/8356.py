#include<iostream>

using namespace std;

int main() {
	int t, n;
	char a[1002];

	cin>>t;

	for(int cs = 1; cs <= t; ++cs) {
		cin>>n>>a;

		int standing = a[0] - '0';

		int ans = 0;

		for(int i = 1; i <= n; ++i) {
			if(standing < i) {
				int added = i - standing;
				ans += added;

				standing += (added + a[i] - '0');
			} else {
				standing += (a[i] - '0');
			}
		}

		cout<<"Case #"<<cs<<": "<<ans<<endl;
	}

	return 0;
}
