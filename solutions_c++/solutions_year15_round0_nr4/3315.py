#include "bits/stdc++.h"
using namespace std;
int main(){
	int t; cin>>t;
	int j = 0;
	for(j = 1; j <= t; j++){
		printf("Case #%d: ", j);
		int x, r, c; cin>>x>>r>>c;
		int a = min(r,c), b = max(r,c);
		if(x == 1) cout<<"GABRIEL"<<endl;
		else if(x == 2){
			if(a == 1){
				if(b == 1 || b == 3) cout<<"RICHARD"<<endl;
				else cout<<"GABRIEL"<<endl;
			}
			else if(a == 2 || a == 4){
				cout<<"GABRIEL"<<endl;
			}
			else{
				if(b == 3) cout<<"RICHARD"<<endl;
				else cout<<"GABRIEL"<<endl;
			}
		}
		else if(x == 3){
			if(a == 1 || a == 4){
				cout<<"RICHARD"<<endl;
			}
			else if(a == 2){
				if(b == 3) cout<<"GABRIEL"<<endl;
				else cout<<"RICHARD"<<endl;
			}
			else{
				cout<<"GABRIEL"<<endl;
			}
		}
		else{
			if(a == 1 || a == 2){
				cout<<"RICHARD"<<endl;
			}
			else if(a == 3){
				if(b == 3) cout<<"RICHARD"<<endl;
				else cout<<"GABRIEL"<<endl;
			}
			else{
				cout<<"GABRIEL"<<endl;
			}
		}
	}
}
