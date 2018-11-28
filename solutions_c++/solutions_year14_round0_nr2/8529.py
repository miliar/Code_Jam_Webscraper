#include <fstream>
#include <iostream>
using namespace std;
float timing(float farm, float speed, float target){
	
}
int main(){
	int T;
	ifstream input;
	input.open("B-large.in");
	ofstream output;
	output.open("output.txt");
	input>>T;
	output.precision(15);
	for(int i=1;i<=T;i++){
		float C,F,X;
		input>>C>>F>>X;
		double speed=2;
		double time=0;
		
		if(X<=C){
			time+=X/speed;
		}
		else{
			
			while(true){
				double timeA=(X-C)/speed;
				double timeB=X/(speed+F);
				if(timeA<=timeB){
					time+=C/speed;
					break;
				}
				else{
					time+=C/speed;
					speed = speed +F;
				}
			}
			time+=(X-C)/speed;
		}
		output<<"Case #"<<i<<": "<<time<<endl;
	}
}
