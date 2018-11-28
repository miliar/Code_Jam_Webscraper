#include <iostream>

using namespace std;
int x,r,c;

string solve(){
	if(x==1)return "GABRIEL";
	if(x==2){
		if(r==1&&c==1)return "RICHARD";
		if(r==1&&c==2)return "GABRIEL";
		if(r==1&&c==3)return "RICHARD";
		if(r==1&&c==4)return "GABRIEL";
		if(r==2&&c==1)return "GABRIEL";
		if(r==2&&c==2)return "GABRIEL";
		if(r==2&&c==3)return "GABRIEL";
		if(r==2&&c==4)return "GABRIEL";
		if(r==3&&c==1)return "RICHARD";
		if(r==3&&c==2)return "GABRIEL";
		if(r==3&&c==3)return "RICHARD";
		if(r==3&&c==4)return "GABRIEL";
		if(r==4&&c==1)return "GABRIEL";
		if(r==4&&c==2)return "GABRIEL";
		if(r==4&&c==3)return "GABRIEL";
		if(r==4&&c==4)return "GABRIEL";
	}
	if(x==3){
		if(r==1&&c==1)return "RICHARD";
		if(r==1&&c==2)return "RICHARD";
		if(r==1&&c==3)return "RICHARD";
		if(r==1&&c==4)return "RICHARD";
		if(r==2&&c==1)return "RICHARD";
		if(r==2&&c==2)return "RICHARD";
		if(r==2&&c==3)return "GABRIEL";
		if(r==2&&c==4)return "RICHARD";
		if(r==3&&c==1)return "RICHARD";
		if(r==3&&c==2)return "GABRIEL";
		if(r==3&&c==3)return "GABRIEL";
		if(r==3&&c==4)return "GABRIEL";
		if(r==4&&c==1)return "RICHARD";
		if(r==4&&c==2)return "RICHARD";
		if(r==4&&c==3)return "GABRIEL";
		if(r==4&&c==4)return "RICHARD";
	}
	if(x==4){
		if(r==1&&c==1)return "RICHARD";
		if(r==1&&c==2)return "RICHARD";
		if(r==1&&c==3)return "RICHARD";
		if(r==1&&c==4)return "RICHARD";
		if(r==2&&c==1)return "RICHARD";
		if(r==2&&c==2)return "RICHARD";
		if(r==2&&c==3)return "RICHARD";
		if(r==2&&c==4)return "RICHARD";
		if(r==3&&c==1)return "RICHARD";
		if(r==3&&c==2)return "RICHARD";
		if(r==3&&c==3)return "RICHARD";
		if(r==3&&c==4)return "GABRIEL";
		if(r==4&&c==1)return "RICHARD";
		if(r==4&&c==2)return "RICHARD";
		if(r==4&&c==3)return "GABRIEL";
		if(r==4&&c==4)return "GABRIEL";
	}
	return "CH";
}
int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	int cases;
	cin>>cases;
	int tc=1;
	while(cases--){
		cin>>x>>r>>c;
		cout<<"Case #"<<tc++<<": "<<solve()<<"\n";
	}
	return 0;
}

