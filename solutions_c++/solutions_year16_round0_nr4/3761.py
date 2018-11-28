#include <iostream>

using namespace std;

int testcase = 0;

long long power(long long a, long long b){
	if(b==0) return 1;
	if(b==1) return a;
	if(b%2) return power(a*a,b/2)*a;
	return power(a*a,b/2);
}

void solve(){
	testcase++;
	long long k,c,s;
	cin>>k>>c>>s;
	cout<<"Case #"<<testcase<<": ";
	long long ans = power(k,c-1);
	for(int i = 0; i<k; i++) cout<<ans*i+1<<" ";
	cout<<endl;
}

int main(){
	int t;
	cin>>t;
	while(t--) solve();
	return 0;
}