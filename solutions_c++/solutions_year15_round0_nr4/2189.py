#include <iostream> 

using namespace std;

int main ()
{
	int num_test, X, R, C;

	cin>> num_test;

	string result [64];

	for( int i=0; i< num_test; i++){

	cin>>X>>R>>C;

	if(X==1){
		cout<<"Case #"<<(i+1)<<": "<<"GABRIEL"<<endl;
	}

	else if(X==2){
			if(R*C==1 || R*C==3 || R*C==9){
				cout<<"Case #"<<(i+1)<<": "<<"RICHARD"<<endl;
			}
			else{
					cout<<"Case #"<<(i+1)<<": "<<"GABRIEL"<<endl;
			}
		}

	else if(X==3){
			if(R*C==6 || R*C==12 || R*C ==9){
				cout<<"Case #"<<(i+1)<<": "<<"GABRIEL"<<endl;
			}
			else{
					cout<<"Case #"<<(i+1)<<": "<<"RICHARD"<<endl;
			}
		}

	else if(X==4){
			if(R*C==16 || R*C==12){
				cout<<"Case #"<<(i+1)<<": "<<"GABRIEL"<<endl;
			}
			else{
					cout<<"Case #"<<(i+1)<<": "<<"RICHARD"<<endl;
			}
		}	

	}		

	/*
	
	for(int n=0; n<num_test; n++)
	{
		cout<<"Case #"<<(n+1)<<": "<< result[n]<<endl;
	}
	*/

	return 0; 
}