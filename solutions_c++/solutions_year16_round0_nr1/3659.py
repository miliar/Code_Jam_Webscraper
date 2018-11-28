#include <iostream>
#include <map>
#include <set>
using namespace std;

int main(){
	
	long t, n, k;
	cin>>t;

	for(long j = 1; j <= t; j++){
		cin>>n;
		long x = n;
		bool done = false;
		set<long> s;
		if(n == 0){
			cout<<"Case #"<<j<<": INSOMNIA"<<endl;
			continue;
		}
		for(long i = 1; n < LONG_MAX/i; i++){
			// cout<<"n is "<<n<<endl;
			k = n;
			while(k){
				s.insert(k%10);
				k = k/10;
			}
			if(s.size() == 10){
				done = true;
				break;
			}
			n = x*(i+1);
		}
		if(done) cout<<"Case #"<<j<<": "<<n<<endl;
		else cout<<"Case #"<<j<<": INSOMNIA"<<endl;
	}

}