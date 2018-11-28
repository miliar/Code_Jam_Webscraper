#include <iostream>
#include <string>
using namespace std;
int main(){
	int T,K,C,S;
	cin>>T;
	int i=T;
	while(T>0){
		cin>>K>>C>>S;
		T--;
		cout<<"Case #"<<i-T<<": ";
		if(K>S) {
			cout<<"IMPOSSIBLE"<<"\n";
		} else{
			for(int j=0;j<K;j++){
				cout<<j+1<<" ";
			}
			cout<<"\n";
		}
	}
	return 0;
}