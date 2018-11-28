#include<iostream>
using namespace std;
int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int t; cin>>t;
	for(int k=1;k<=t;k++){
		int x,r,c; cin>>x>>r>>c;
		if(r>c) swap(r,c);
		bool flag;  //gƒ‹∑Ò”Æ
		if(x==1) flag=true;
		if(x==2) {
			if(r*c%2==1) flag=false;
			else flag=true;
		}
		if(x==3) {
			if(r==2 && c==3 || r==3 && c==4 || r==3 && c==3) flag=true;
			else flag=false;
		}
		if(x==4) {
			if(r==3 && c==4 || r==4 && c==4) flag=true;
			else flag=false;
		}
		cout<<"Case #"<<k<<": ";
		if(flag) cout<<"GABRIEL"<<endl;
		else cout<<"RICHARD"<<endl;
	}
	return 0;
}