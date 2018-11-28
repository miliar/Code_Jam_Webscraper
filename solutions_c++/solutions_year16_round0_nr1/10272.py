// A. counting sheep

#include <bits/stdc++.h>

using namespace std;

int main() {

	long long t, i, j;
	long long n, temp;
	set<int> digits;

	cin>>t;
	for(i=1; i<=t; i++) {

		digits.clear();
		cin>>n;

		if(n==0) {
			cout<<"Case #"<<i<<": INSOMNIA\n";
			continue;
		}

		for(j=1; ; j++) {

			temp = n*j;
			//cout<<temp<<endl;
			while(temp!=0) {
				digits.insert(temp%10);
				temp/=10;
			}

			if(digits.size()==10) {
				temp=n*j;
				break;
			}
		}

		cout<<"Case #"<<i<<": "<<temp<<"\n";
	}

	return 0;
}