#include <bits/stdc++.h>

using namespace std;
int x,r,c;

string solve(){// kheeeeeee o.O
	// lelelelele :v :V :v :v super trulls
	if(x==1)return "GABRIEL";
	if(x==2){
		if(r*c%2)return "RICHARD";
		else return "GABRIEL";
	}
	if(x==3){
		if(r*c%3==0&&r*c>=6)return "GABRIEL";
		return "RICHARD";
	}
	if(x==4){
		if(r*c%4==0&&r*c>=12)return "GABRIEL";
		return "RICHARD";
	}
}
int main(){
	int T;
	cin>>T;
	for(int tc=1;tc<=T;tc++){
		cin>>x>>r>>c;
		cout<<"Case #"<<tc<<": "<<solve()<<"\n";
	}
	return 0;
}