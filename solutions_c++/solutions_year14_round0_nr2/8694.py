#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
using namespace std;

void compare(const vector<int>& left, const vector<int>& right, ofstream& out);

int main ()
{  
	ifstream infile("B-large.in");
	ofstream outfile("out");
	
	int cases;
	infile >> cases;
	for(int i = 0; i < cases; i++) {
		double cost;
		double increase;
		double goal;
		infile >> cost >> increase >> goal;


		double currInc = 2.0;
		double currTime = 0.0;


		while(1) {
			double estGoal = goal / currInc;
			double estBuy = cost / currInc;
			double estBuyGoal = estBuy + goal / (currInc + increase);

			if(estGoal <= estBuyGoal) {
				double print = currTime + estGoal;
				outfile << "Case #" << i+1 << ": " << fixed << setprecision(7) << print << endl;
				break;
			} else {
				currInc += increase;
				currTime += estBuy;
			}
		}

	}

	return 0;
}

void compare(const vector<int>& left, const vector<int>& right, ofstream& outfile) {
	bool found = false;
	int ret = 0;
	for(int i = 0; i < left.size(); i++) {
		for(int j = 0; j < right.size(); j++) {
			if(left[i] == right[j]) {
				if(found) {
					outfile << "Bad magician!";
					return;
				}
				
				ret = left[i];
				found = true;
			}
		}
	}
	
	if(found) {
		outfile << ret;
	} else {
		outfile << "Volunteer cheated!";
	}
}
 
