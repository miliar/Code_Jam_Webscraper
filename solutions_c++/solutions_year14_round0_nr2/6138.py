#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <fstream>
using namespace std;

int main(){

	double diff=1e-7;
	double cookies,two=2.000000,c,f,x,slope,time,improvedTime,cost2Improve;
	int testC,caseN=1;
	
	ifstream fin("bbig.in");
	ofstream fout("bout.txt");
	fin>>testC;
	                  
	while(testC--){
		cookies=0.000000;
		slope=2.0000000;
		time=0.0000000;
		fin>>c>>f>>x;
	
		improvedTime=improvedTime=x/slope-x/(slope+f);
		cost2Improve=c/slope;
		
		while(improvedTime>cost2Improve){
			
			time+=cost2Improve;
			//printf("delta: %.7f \t time: %.7f\n",cost2Improve,time);
			
			slope+=f;
			improvedTime=x/slope-x/(slope+f);
			cost2Improve=c/slope;
			
			//buy new farm -> advance necessary time
			//cookies=cookies + two*(c/slope);
		}
		
		time=time+(x)/slope;
		
		fout<<"Case #"<<caseN++<<": "<<fixed<<setprecision(7)<<time<<endl;
		//printf("Case #%d: %.7f\n",caseN++,time);
	}









	return 0;
	
}
