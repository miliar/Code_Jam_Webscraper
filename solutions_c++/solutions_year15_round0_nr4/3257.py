#include <iostream>
using namespace std;


int main(){
	int cases;
	cin>>cases;
	for(int c=1;c<=cases;c++){
		int x,r,t;
		cin>>x>>r>>t;
		if(x>r*t || (x>r && x>t))
			cout<<"Case #"<<c<<": RICHARD"<<endl;
		else if((r*t)%x!=0)
			cout<<"Case #"<<c<<": RICHARD"<<endl;
		else if(x==5 && (r<3 || t<3))
			cout<<"Case #"<<c<<": RICHARD"<<endl;
		else if(x==4 && (r<3 || t<3))
			cout<<"Case #"<<c<<": RICHARD"<<endl;
		else if(x==3 && (r<2 || t<2))
			cout<<"Case #"<<c<<": RICHARD"<<endl;
		else
			cout<<"Case #"<<c<<": GABRIEL"<<endl;
	}

	return 0;
}