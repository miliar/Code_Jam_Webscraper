#include<iostream>
#include<string>
using namespace std;
int main(){
	int t,x,r,c,cas;
	cin>>t;
	cas=0;
	string g,ri;
	g="GABRIEL\n";
	ri="RICHARD\n";	
	while(t--){
		cas++;
		cin>>x>>r>>c;
		cout<<"Case #"<<cas<<": ";
		switch(x){
			case 1: 
				cout<<g;
				break;
			case 2:
				if((r*c)%2==0)
					cout<<g;
				else cout<<ri;
				break;
			case 3:
				if(((r*c)==6)||((r*c)==9)||((r*c)==12))
					cout<<g;
				else cout<<ri;
				break;
			case 4:
				if(((r*c)==12)||((r*c)==16))
					cout<<g;
				else cout<<ri;
				break;

		}
	}
}
