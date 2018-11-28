#include <iostream>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <stdio.h>
#include <iomanip>

using namespace std;


int main(){
	ofstream outfile;
	outfile.open("output.txt");
	ifstream infile;
	infile.open("B-large.in");

	int K;
	infile>>K;

	for (int numcase=1;numcase<=K;numcase++){
		double C;
		double F;
		double X;
		infile>> C;
		infile>> F;
		infile>> X;
		
		double maxtotal=X/2.0;
		double oldrate=2.0;
		double newrate=0.0;
		double curtotal=0.0;
		double prevfixed=0;
		
		while (1)
		{	
				
				newrate=oldrate+F;
				curtotal=prevfixed+C/oldrate+X/newrate;
				prevfixed=prevfixed+C/oldrate;
				oldrate=newrate;
				if(maxtotal>curtotal){
					maxtotal=curtotal;
				}else{
					break;
				}
				
		}


			outfile<<"Case #" <<numcase <<": "<< fixed<<setprecision(7)<< maxtotal <<endl; 
	}


	outfile.close();
	return 0;

}