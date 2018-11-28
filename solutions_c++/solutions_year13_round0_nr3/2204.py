#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define NUM 10000001
//2500000001ll
using namespace std;

vector<int> res;

bool is_pal(unsigned long long x){
	unsigned long long y=0ll, p=x;
	while(p){ y*=10; y+=p%10; p/=10; }
	return x==y;
}
int main(void){
	for(unsigned long long i=1;i<NUM;i++){
		if(is_pal(i) && is_pal(i*i) ){
			//cout << i << " " <<  i*i << endl;
			res.push_back(i*i);
		}
	}
	int T;
	long long a,b;
	cin >> T;
	for(int t=1;t<=T;t++){
		cin >> a >> b;
		cout << "Case #"<<t<<": " << upper_bound(res.begin(),res.end(),b) - lower_bound(res.begin(),res.end(),a) << endl;
	}
}