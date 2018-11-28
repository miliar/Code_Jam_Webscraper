#include <iostream>
using namespace std;



int main(){
	int T,N,J;
	cin>>T>>N>>J;
	//N is even always
	cout<<"Case #1:\n";
	for(int i=0;i<J;i++){
		int temp=i;
		cout<<"11";
		int n=2;
		while(temp>0){
			if(temp%2==0) cout<<"00";
			else cout<<"11";
			n+=2;
			temp=temp/2;
		}
		while(n < N-2){
			cout<<"00";
			n+=2;
		}
		cout<<"11";
		for(int j=3;j<=11;j++) {cout<<" "<<j;}
		cout<<"\n";
	}
}