#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;


unsigned long long mypow(int value, int base) {
	unsigned long long ans = 1;
	while(base--) {
		ans *= value;
	}
	return ans;
}


int main() {

	int tcs = 0;
	scanf("%d", &tcs);
	for(int k=1;k<=tcs;k++) {
		int K, C, S;
		cin >> K >> C >> S;
		cout<<"Case #"<<k<<": ";
		if( C == 1 || K == 1 ) {
			for(int i=0;i<K;i++) {
				if(i > 0)
					cout<<" ";
				cout<<i+1;
			}
		}
		else {
			unsigned long long step = mypow(K, C-1);
			unsigned long long x = 2;
			unsigned long long px = x;
			for(int i=0;i<K-1;i++) {
				if(i > 0)
					cout<<" ";
				cout<<x;
				x += step + 1;
				px = x;
			}
		}
		cout<<endl;
		
	}

	return 0;
} 


