#include<iostream>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	int t; cin>>t;
	for(unsigned int t1 = 1; t1<=t; t1++){
		cout<<"Case #"<<t1<<": ";
		int x,r,c;
		cin>>x>>r>>c;
		if(r*c % x != 0){
			cout<<"RICHARD\n";
			continue;
		}
		if(x == 1 || x == 2){
			cout<<"GABRIEL\n";
			continue;
		}
		if(min(r,c) == 1){
			cout<<"RICHARD\n";
			continue;
		}
		if(x == 3){
			cout<<"GABRIEL\n";
			continue;
		}
		if(min(r,c) == 2){
			cout<<"RICHARD\n";
			continue;
		}
		cout<<"GABRIEL\n";
	}
	return 0;
}
