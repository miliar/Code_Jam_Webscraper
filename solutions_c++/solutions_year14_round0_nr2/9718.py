#include <iostream>
#include <fstream>
#include <iomanip> 

using namespace std;
int main(){
	ifstream fin("B-small-attemptB-2014.in");
	ofstream fout("B-small-attemptB-2014.out");

	int dataNumber;
	fin>>dataNumber;

	for(int i=1;i<=dataNumber;i++){
	
		double C;
		double F;
		double X;

		fin>>C;
		fin>>F;
		fin>>X;

		
		double consumTime = 0.0;
		double currentSpeed = 2.0;

		double direct = X/currentSpeed;
		double buildOne = C/currentSpeed + X/(F+currentSpeed); 

		while(direct >= buildOne){
			
			consumTime += C/currentSpeed;
			currentSpeed += F;
			
			direct = X/currentSpeed;
			buildOne = C/currentSpeed + X/(F+currentSpeed);

		}

		fout<<"Case #"<<i<<": "<<setprecision(7)<<(direct+consumTime)<<endl;
	
	}


	return 0;
}