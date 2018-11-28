//C is the cost of the farm, F is how much extra the farm gives, and X is the goal
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
ifstream in("B-large.in");
ofstream out("o2BIG2.txt");
double solve(double C, double F, double X){
	double rate = 2;//Essentially how many cookies per unit of time.
	double time = C/rate;
	double fromPSV = 0;
	double fromAGR = 0;
	double amt = 0;
	while(amt<X){
		fromPSV = (X-C)/rate;
		fromAGR = X/(rate+F);
		if(fromPSV<=0){
			amt = X;
			time = X/rate;
			break;
		}
		if(fromPSV<=fromAGR && fromPSV>0){
			time += fromPSV;
			amt = X;
		}else if(fromAGR<fromPSV){
			//Here we buy another farm.
			rate += F;
			time += (C)/rate;
		}
	}
	return time;
}
int main(){
	int T;
	in >> T;
	double C = 0;
	double F = 0;
	double X = 0;
	for(int i = 1;i<=T;i++){
		out << "Case #" << i << ": ";
		in >> C;
		in >> F;
		in >> X;
		out.precision(10); 
		out << solve(C,F,X) << "\n";
	}
	return 0;
}
