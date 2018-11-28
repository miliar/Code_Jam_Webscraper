#include <iostream>
#include <vector>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int x = 1;x<=t;x++){
	int n;
	cin>>n;
	string a;
	cin>>a;
	int numsum = 0;
	int ans = 0;
	for(int i=0;i<n+1;i++){
		if(numsum < i){
			ans += i-numsum;
			numsum += i-numsum;
		}
		numsum += a[i]-'0';
	}
	cout<<"Case #"<<x<<": "<<ans<<endl;
	}
	return 0;
}

