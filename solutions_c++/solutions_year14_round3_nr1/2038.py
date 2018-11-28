#include <iostream>
#include <string>
#include <vector>
#include <limits.h>
#include <cmath>

using namespace std;

void solveCase(int caseNum){
	
	long int top, bot;

	cin >> top;
	cin.ignore(1);
	cin >> bot;


	double power = log2(bot);

	int powerint = (int)power;

	if(powerint != power){
		cout << "Case #" << caseNum << ": impossible" << endl;
		return;
	}



	if(top % 2 == 0){
		cout << "Case #" << caseNum << ": impossible" << endl;
		return;
	}

	int parent = 1;

	while(true)
	{
		
		if(top >= bot/2 ){	
			break;
		}
		
		bot/=2;
		parent++;			

	}






	cout << "Case #" << caseNum << ": " << parent << endl;
}



int main(void){

	int numCases;
	cin >> numCases;

	for(int i=1; i<=numCases;i++){
		solveCase(i);
	}

}