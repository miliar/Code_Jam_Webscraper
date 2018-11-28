#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <cmath>
#include <fstream>

using namespace std;

double calcSeconds (int farms, double increment, double farmCost, double goal){
	
	double total = 0;
	double rate = 2;
	
	for (int i = 0; i<farms; i++){
		total += farmCost/rate;
		rate += increment;
	} 
	
	total += goal/rate;
	
	return total;
	
}

int main ()
{
	ifstream fin("B-large.in");
	ofstream fout("CookieResultsLarge.txt");
	
	if(!fin){
		cout<<"Unable to open file";
		cin.get();
		return EXIT_FAILURE;
	}
	
	fout<<fixed<<setprecision(7);
	
	int tests;
	fin>>tests;
	
	for (int i = 0; i<tests;i++){
		double C,F,X;
		fin>>C>>F>>X;
		int start = 0;
		double time = 0;
		while(true){
			double time1 = calcSeconds(start,F,C,X);
			double time2 = calcSeconds(start+1,F,C,X);
			
			if(time1<time2){
				time = time1;
				break;
			}
			else 
			{
				start++;
			}
		}
		
		fout<<"Case #"<<i+1<<": "<<time<<endl;
		
	}
	
}
