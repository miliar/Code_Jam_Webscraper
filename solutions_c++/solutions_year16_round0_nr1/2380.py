#include <iostream>
using namespace std;

int main(){
	unsigned long long t;
	cin>>t;
	for(unsigned long long z=1;z<=t;++z){
		bool arr[] = {false, false, false, false, false, false, false, false, false, false};
		unsigned long long n, m, d, t;
		cin>>n;

		if(n == 0){
			cout<<"Case #"<<z<<": INSOMNIA"<<endl;
			continue;
		}
		
		for(t = n;t>0;t+=n){
			m = t;
			while(m){
				d = m%10;
				arr[d] = true;
				m/=10;
			}

			bool f = true;
			for(unsigned long long i=0;i<10;++i)
				f = f & arr[i];

			if(f){
				cout<<"Case #"<<z<<": "<<t<<endl;
				break;
			}
		}
	}
}