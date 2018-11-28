#include <iostream>
#include <vector>
using namespace std;
bool a[10];
void check(int n){
	while(n){
		if(!a[n%10]) a[n%10]=true;
		n=n/10;
	}
}
bool done(){
	for(int i=0;i<10;i++){
		if(!a[i]) return false;
	}
	return true;
}
int main() {
	int k=0;
	int t;
	cin>>t;
	while(t--){
	k++;
	int n;
	cin>>n;
	bool p=true;
	for(int i=0;i<10;i++) a[i]=false;
	int i=0;
	while(!done()){
		i++;
		check(i*n);
		if(i==1000){
			p=false;
			break;
		}
	}
	if(p) cout<<"Case #"<<k<<": "<<i*n<<endl;
	else cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
	}
}
