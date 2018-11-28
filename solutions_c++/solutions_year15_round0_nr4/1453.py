#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;
int T;

int main(){
	int X,R,C;
	cin>>T;
	for(int cs=1; cs<=T; ++cs){
		cout<<"Case #"<<cs<<": ";
		cin>>X>>R>>C;
		switch(X){
			case 1:
				cout<<"GABRIEL"<<endl;
				break;
			case 2:
				if(R*C&1)
					cout<<"RICHARD"<<endl;
				else
					cout<<"GABRIEL"<<endl;
				break;
			case 3:
				if(min(R,C) == 1){
					cout<<"RICHARD"<<endl;
				}else if(R*C%3==0)
					cout<<"GABRIEL"<<endl;
				else
					cout<<"RICHARD"<<endl;
				break;
			case 4:
				if(R*C%4){
					cout<<"RICHARD"<<endl;
					break;
				}else{
					if(min(R,C)<3){
						cout<<"RICHARD"<<endl;
						break;
					}
				}
				cout<<"GABRIEL"<<endl;
				break;
		}
	}
	
	return 0;
}



