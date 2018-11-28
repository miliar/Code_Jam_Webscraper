#include<bits/stdc++.h>

using namespace std;

int main() {
	int tCase;
	cin>>tCase;
	for (int i=1; i<=tCase; ++i) {
		unsigned long long n=0;
		cin>>n;
		if (n == 0) {
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            continue;
		}
		else {
			vector<int> digitSeen (10);
			long  multiplier = 0;
            unsigned long long tempN = n;
			while(accumulate(digitSeen.begin(),digitSeen.end(),0) != 10){
				string s = to_string(n);
				for (int j = 0, sz = s.size(); j < sz; ++j) {
					digitSeen[s[j]-'0'] = 1;
				}
				n = tempN * (++multiplier);
                
			}
			cout<<"Case #"<<i<<": "<<n-tempN<<endl;
		}
	}
	return 0;
}