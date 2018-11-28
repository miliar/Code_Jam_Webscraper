#include<iostream>
#include<fstream>
#include <iomanip>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main(){
	
	ifstream fin;
  	fin.open ("input.txt");
	
	ofstream fout;
  	fout.open( "output.txt");
	
	int t;
	fin>>t;
	
	int result;
	
	for(int p=1; p<=t; p++){
		
		double farmGoal,rate,goal;
		double initRate = 2;
		
		fin>>farmGoal;
		fin>>rate;
		fin>>goal;
		
		double time = 0;
		double prevTime = goal/initRate;
		double currTime = 0;
		
		//cout<<prevTime<<endl;
		
		while(true){
			time = time + farmGoal/initRate;
			initRate=initRate+rate;
			double p = goal/initRate;
			
			//cout<<time << " " << p<<endl;
			
			currTime = time + p;
			
			if(currTime > prevTime){
				break;
			}else{
				prevTime = currTime;
			}
		}
		//fprintf(fout,"Case #%d: %.7f\n",p,prevTime);
		fout<<"Case #"<<p<<": "<<setprecision(7) << setiosflags(ios::fixed)<<prevTime<<endl;
	}

}
