#include<iostream>

using namespace std;

int T;
long long r , t;

int main() {
	cin>>T;
	for(int ti=0;ti<T;ti++) {
		cin>>r>>t;
		long long up = 1000*1000*1000, low = 0 , mid;
		if (up * up / r < up) up = up * up / r ;
		while ( up - low > 1) {
			mid = (low + up) / 2 ;
			if( (mid * (2 * mid + 2 * r - 1)) > t)
				up = mid;
			else low = mid;
//			cout<< low << "-" << up<<endl;
		}
		cout<<"Case #"<<ti+1<<": "<<low<<endl;
	}
	return 0;
}