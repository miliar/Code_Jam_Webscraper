#include <iostream>
using namespace std;
#define ull unsigned long long
#define pi 3.141
int main() {
	int T;
	ull t,r;
	cin>>T;

	for(int i=1;i<=T;++i){
		cin>>r>>t;
		int count=0;
		//t=(double)t/( double)pi;
		//cout<<"("<<r<<", "<<t<<" )"<<endl;
		ull diff;
		for(int j=0;;j+=2){
			diff = (r+1+j)*(r+1+j) - (r+j)*(r+j);
		//	cout<<"diff = "<<diff<<endl;
			//cout<<"t = "<<t<<endl;
			if( diff <= t ){
				count++;
			}else{
				break;
			}
			t=t-diff;
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}
