#include <iostream>
#include <iomanip>

using namespace std;

#define EPSILON 0.00000001


bool alessthanb(double a, double b){
	double diff = a-b;
	return (-diff >= EPSILON);
}

int main(){
	int testcases,counter=1;
	double farmcost,farmproduction,totalcookies;
	double actualproducion=2.0f,totaltime=0.0f;


	cin >> testcases;
	while(testcases-- > 0){
		cin >> farmcost >> farmproduction >> totalcookies;

		/*while buying a farm is better*/
		while(alessthanb( (double)farmcost/actualproducion + (double)totalcookies/(actualproducion+farmproduction) , (double)totalcookies/actualproducion ) ){
			
			totaltime += (double)farmcost/actualproducion;
			actualproducion += farmproduction;
		}
		totaltime += (double)totalcookies/actualproducion;

		cout << "Case #" << counter++ << ": " << fixed << setprecision(7) << totaltime << endl;
		totaltime = 0.0f;
		actualproducion =2.0f;
	}

	return 0;
}