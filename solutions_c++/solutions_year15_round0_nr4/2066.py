#include <bits/stdc++.h>
using namespace std;

int main(){
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		int x,r,c;
		cin>>x>>r>>c;
		if(x==1){
			cout<<"Case #"<<t+1<<": "<<"GABRIEL"<<endl;
		}
		if(x==2){
			if(r%2==1&&c%2==1){
				cout<<"Case #"<<t+1<<": "<<"RICHARD"<<endl;
			}
			else{
				cout<<"Case #"<<t+1<<": "<<"GABRIEL"<<endl;
			}
		}
		if(x==3){
			if((r%3==0||c%3==0) && (r!=1&&c!=1)){
				cout<<"Case #"<<t+1<<": "<<"GABRIEL"<<endl;
			}
			else{
				cout<<"Case #"<<t+1<<": "<<"RICHARD"<<endl;
			}
		}
		if(x==4){
			if(r==4&&c==4 ||(r+c)==7){
				cout<<"Case #"<<t+1<<": "<<"GABRIEL"<<endl;
			}
			else{
				cout<<"Case #"<<t+1<<": "<<"RICHARD"<<endl;
			}
		}
	}
}
	
