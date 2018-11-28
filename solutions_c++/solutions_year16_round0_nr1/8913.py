#include <bits/stdc++.h>

using namespace std;

bool arr[10];

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t, n, x, p;
	cin>>t;
	for(int i=1; i<=t; i++) {
		cin>>n;
		p=n;
		memset(arr, 0, sizeof(arr));
		if(!n) {
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		set<int> s;
		while(s.size()!=10) {
			x = p;
			while(x) {
				s.insert(x%10);
				x/=10;
			}
			p+=n;
		}
		p-=n;
		cout<<"Case #"<<i<<": "<<p<<endl;
		
	}

	return 0;
}