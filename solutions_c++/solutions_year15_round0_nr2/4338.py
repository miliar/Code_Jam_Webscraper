#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int T;
	cin>>T;

	for(int N = 1 ; N <= T ; N++) {
		int D; 
		cin>>D;
		
		vector<int> a(D);
		for(int i = 0 ; i < D ; i++) {
			cin>>a[i];
		}

		int ret = 1001;
		for(int i = 10; i > 0 ; i--) {
			int cnt = 0;
			for(int j = 0 ; j < D ; j++) {
				if( a[j] > i ) {
					if(a[j] % i == 0)	cnt += a[j]/i - 1 ;
					else				cnt += a[j]/i;
				}
			}
			ret = min(cnt+i, ret);
		}
		cout<<"Case #"<<N<<": "<<ret<<endl;
	}
	return 0;
}