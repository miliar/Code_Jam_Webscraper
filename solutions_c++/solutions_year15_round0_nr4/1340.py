#include<iostream>
#include<string>

using namespace std;

int main(){
	int kases; cin>>kases;
	for(int kase = 1; kase <= kases;kase++){
		int X, R, C;
		string winner = "";
		cin>>X>>R>>C;
		if(X == 1) winner = "GABRIEL";
		else if(X == 2){
			if( ((R*C) & 1) ) winner = "RICHARD";
			else winner = "GABRIEL";
		}
		else if(X == 3){
			if( R == 3 && C == 3 ) winner = "GABRIEL";
			else if( (R == 3 || C == 3) && (R == 2 || R == 4 || C == 2 || C == 4) ) winner = "GABRIEL";
			else winner = "RICHARD";
		}
		else if(X == 4){
			if( (R == 4 && C>=3) || (C == 4 && R >= 3) ) winner = "GABRIEL";
			else winner = "RICHARD"; 
		}
		else winner = "RICHARD";
		cout<<"Case #"<<kase<<": "<<winner<<endl;	
	}
}
