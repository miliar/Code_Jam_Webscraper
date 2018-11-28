#include<iostream>
#include<algorithm>
using namespace std;
int main() {
	int cn=1,T;
	cin>>T;
	while(cn<=T) {
		int x,r,c,ans=0;
		cin>>x>>r>>c;
		if(x<3 && (r*c)%x==0)ans=1;
		if(x==3 && (r*c)%x==0 && r>1 && c>1)ans=1;
		if(x>3 && (r*c)%x==0 && r>2 && c>2)ans=1;
		if(ans==1)cout<<"Case #"<<cn<<": GABRIEL"<<endl;
		else cout<<"Case #"<<cn<<": RICHARD"<<endl;
		cn++;
	}
	return 0;
}
