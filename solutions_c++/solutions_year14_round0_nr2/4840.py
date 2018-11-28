#include <iostream>
#include <fstream>
#include <set>
#include <iomanip>

using namespace std;
int T;
double C, F, X;

int main(){
	ifstream infile("input.txt");
	infile >> T;

	for(int i = 1; i <= T; i++){
		infile >> C >> F >> X;

		double curTime = 0;
		double curProd = 2;

		while(curTime < 600){
			double timeToX = X / curProd;
			double timeToCthenX = C / curProd + X / (curProd + F);
 			if(timeToX < timeToCthenX){
				curTime += timeToX;
				break;
			}

			curTime += C / curProd;
			curProd += F;
		}

		cout << "Case #" << i << ": " << fixed << setprecision(7) << curTime << endl;
	}
}