#include <iostream>

using namespace std;

int main(){
	int T;

	cin>>T;

	for(int TCN = 1; TCN<=T; TCN++){
		int A, B, K;

		cin>>A>>B>>K;

		long long winpair=0;

		for(int i = 0; i<A; i++){
			for(int j = 0; j<B; j++){
				if((i&j)<K){
					winpair++;
				}
			}
		}

		cout<<"Case #"<<TCN<<": "<<winpair<<endl;


	}

	return 0;
}
