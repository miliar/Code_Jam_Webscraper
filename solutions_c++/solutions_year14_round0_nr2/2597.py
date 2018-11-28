#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <iomanip>
#include <utility>
using namespace std;



ifstream fin ("B-large.in");
ofstream fout ("B-large.out");

//ifstream fin ("test.in");
//ofstream fout ("test.out");

int t;
double c,f,x;
double cs = 2.0;
double cc = 0.0;


double make(){
	double secondsPassed = 0.0;
	double numberOfFarm = 0.0;
	while(true){
		double secondsToWin = x/(cs+(f*numberOfFarm));
		double secondsToWinWithBuildFarm = c/(cs+(f*numberOfFarm)) + x/(cs+(f*(numberOfFarm+1)));

		if(secondsToWin < secondsToWinWithBuildFarm)
			return (secondsPassed + secondsToWin);
		else
		{			
			secondsPassed+=c/(cs+(f*numberOfFarm));
			numberOfFarm+= 1.0;
		}

	}
	
	return secondsPassed;

}


int main() { 
	int t;
	
	fin >> t;
	
	
	for (int i = 0; i < t; i++){
		fin >> c >> f >> x;
		fout<<"Case #"<<i+1<<": "<<setprecision(51)<<make()<<endl;
		
	}
	
	return 0;
}
