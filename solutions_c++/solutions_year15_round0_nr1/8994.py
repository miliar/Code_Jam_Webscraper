#include <iostream>
#include <string>
using namespace std;

int main() {
freopen("input.txt", "rt", stdin);
freopen("output.txt", "wt", stdout);

long long testz;
long long k, sumpeo=0, n, sumfr=0;
string s;
cin>>testz;
for(long long t=0; t<testz; t++) {
	sumpeo=0;
	sumfr=0;
	cin>>k;
	cin>>s;
	for(long long i=0; i<=k; i++) {
		if(i > sumpeo) {
			sumfr+=i-sumpeo;
			sumpeo+=i-sumpeo;
		}
		n=s[i]-'0';
		sumpeo+=n;
	}
cout<<"Case #"<<t+1<<": "<<sumfr<<endl;
}
}