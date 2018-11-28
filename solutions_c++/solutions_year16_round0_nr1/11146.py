//Google CodeJam

#include <iostream>
#include <fstream>
#include <climits>

using namespace std;

bool checkarraypart (bool array[] ) {
	bool temp = true;
	
	for (int i = 0; i < 10; i++) {
		if (array[i] == false) temp = false;
	}

	return temp;
}

int main ( ) {
	
	ifstream infile;
	ofstream outfile;
	int inputnumb = 0;
	int ccount = 1;
	int ncount = 1;
	int calcnumb = 1;
	int temp = 0;
	bool insomnia = false;
	bool first = true;
	bool numbers[10];
	
	//set bool array to false 
	for (int i = 0; i < 10; i++) numbers[i] = false;
	
	infile.open("A-large.in", ios::in);
	outfile.open ("sheep.txt");
	
	//get input file
	if (!infile) cout << "This file can't be opened." << endl;
	
 //loop through this for every case
 while (infile >> inputnumb ) {
 if (first) first = false;
 else {
 //loop through the checker while not true	
	 	while (!checkarraypart(numbers)){
				//count how many digits the number exists of
				calcnumb = ncount * inputnumb;
		
				//check for insomnia
				if ((calcnumb - INT_MAX) > 0 || calcnumb == 0 ) { //check
					insomnia = true;
					break;
				}

				//get digits and add to array
				while (calcnumb != 0) { //check
					temp = calcnumb % 10;
					calcnumb /= 10;
	
					numbers[temp] = true;
				}	
				//return number to its original value

				ncount++;
			}//while
			outfile << "Case #" << ccount << ": ";
			if (insomnia) {
				outfile << "INSOMNIA";
				insomnia = false;
			}
			else { outfile << (ncount-1) * inputnumb;}
			
			ncount = 1;
			
			outfile << "\n";
			ccount++;
		}//else
		//set bool array to false 
		for (int i = 0; i < 10; i++) numbers[i] = false;
	}//while
	outfile.close();
	return 0;
	
}
