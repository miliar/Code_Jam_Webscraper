#include <iostream>
#include <iomanip>
#include <vector>
#include <fstream>
using namespace std;
double produce(double buyfarm, double totalproduction,double farmproduction,double limit){	
		double total=0;
	while(true){
		if(limit/totalproduction < (buyfarm/totalproduction)+(limit/(totalproduction+farmproduction))){
			total+=limit/totalproduction; break;
		}
		else{
			total+= (buyfarm/totalproduction);
			totalproduction+=farmproduction;
		}
	}
	return total;

}
main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int time; 
	fin >> time;
	for(int c=1; c<=time; c++){
		double buyfarm, totalproduction=2, farmproduction, limit;
		fin >> buyfarm >> farmproduction >> limit;
		fout << "Case #" << c << ": ";
		fout <<fixed<<setprecision(7)<< produce(buyfarm, totalproduction, farmproduction, limit) << endl;
	}
	
}
