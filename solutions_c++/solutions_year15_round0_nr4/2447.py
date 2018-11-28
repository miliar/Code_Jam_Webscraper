#include<iostream>
using namespace std;

int T,X,R,C,m;

int main(){
	cin>>T;
	for(int test=1;test<=T;test++){
		cin>>X>>R>>C;
		switch(X){
			case 1:
				cout<<"Case #"<<test<<": GABRIEL\n";
				break;
			case 2:
				m = R*C;
				(!(m%2)) ? cout<<"Case #"<<test<<": GABRIEL\n" : cout<<"Case #"<<test<<": RICHARD\n";
					
				break;
			case 3:
					if((R==3 && C==3) || (R==3 && C==2) || (R==2 && C==3) || (R==3 && C==4) || (R==4 && C==3))
						cout<<"Case #"<<test<<": GABRIEL\n";
					else
						cout<<"Case #"<<test<<": RICHARD\n";
				break;
			case 4:
					if((R==4 && C==4) || (R==3 && C==4) || (R==4 && C==3))
						cout<<"Case #"<<test<<": GABRIEL\n";
					else
						cout<<"Case #"<<test<<": RICHARD\n";
				break;
		
		}
	
		
	}
	return 0;
}
