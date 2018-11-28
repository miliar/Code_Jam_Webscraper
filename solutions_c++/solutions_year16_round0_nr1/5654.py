#include <iostream>
#include <set>

using namespace std;

int testcase = 0;

void solve(){
	testcase++;
	long long n;
	cin>>n;
	if(n==0){
		cout<<"Case #"<<testcase<<": "<<"INSOMNIA"<<endl;
	} else {
		set <long long> ms;
		long long k = 1;
		long long tmp;
		while(ms.size()!=10){
			tmp = k*n;
			while(tmp){
				ms.insert(tmp%10);
				tmp /= 10;
			}
			k++;
		}
		cout<<"Case #"<<testcase<<": "<<n*(k-1)<<endl;
	}
}

int main(){
	int t;
	cin>>t;
	while(t--) solve();
	return 0;
}