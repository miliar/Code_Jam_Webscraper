#include <iostream>
#include <string>
#include <vector>
#include <limits.h>
#include <cmath>

using namespace std;

void solveCase(int caseNum){

	int xa,xb,xk;
	cin >> xa >> xb >> xk;
	
//	cout << xa << " "<< xb << " "<< xk << " "<< endl;

	int winnings = 0;
	for(int a = xa-1;a>=0;a--){
		for(int b = xb-1;b>=0;b--){
			for(int k =xk-1;k>=0;k--){
				if(k == (a&b)){
					winnings++;					
				}
			}
		}
	}

	cout << "Case #" << caseNum << ": " << winnings << endl;
}


int main(void){

	int numCases;
	cin >> numCases;

	for(int i=1; i<=numCases;i++){
		solveCase(i);
	}

}