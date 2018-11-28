#include <iostream>
#include <algorithm>
using namespace std;
bool dig[10];
bool add(int x){
	dig[x%10] = true;
	while(x!=0){
		dig[x%10] = true;
		x = x/10;
	}
	for(int i=0;i<10;i++){
		if(!dig[i]) return false;
	}
	return true;
}
int main(){
	freopen("large","r",stdin);
	freopen("out","w",stdout);
	int t; cin>>t;
	int T = t;
	while(t--){
		int n; cin>>n;

		for(int i=0;i<100;i++) dig[i] = false;
		bool ans = true;
		for(int i=1;i<=100;i++){
			if(add(i*n)){
				cout<<"Case #"<<T - t<<": "<<i*n<<endl;
				ans = false;
				break;
			}
		}
		if(ans) cout<<"Case #"<<T - t<<": INSOMNIA"<<endl;
	}
}