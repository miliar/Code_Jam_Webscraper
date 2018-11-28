#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

double timeTowin(double rate,double X){
	   return X/rate;
}

int main(){
	int t = 1;
	int j = 1;
	ifstream ifile("B-large.in");
	ofstream ofile("output.txt");
	ifile>>t;
	while(t--){
		double C=500.0,F=4.0,X=2000.0;
		ifile>>C>>F>>X;
		double curr = 2.0;
		double timer = 0.0;
		while(true){
			double currTime = timeTowin(curr,X);
			double currTime2 = timeTowin(curr,C);
			double nextTime = currTime2 + timeTowin(curr+F,X);
			if(currTime>nextTime){
				curr += F;
				timer += currTime2;
			}else{
				timer += currTime;
				break;
			}
		}
		ofile<<"case #"<<j++<<": "<<setprecision(14)<<timer<<endl;
	}
}
