#include<iostream>
#include<string>
#include <fstream>

#include<stack>
#include<queue>

using namespace std;

int main(){
	ifstream myfile;
	myfile.open("input.in");
	ofstream out;
	out.open("output.txt");
	int rot = 0, counter = 0;
	myfile >> rot;
	int theCard;

	while (counter != rot){
		vector<int> theStack;
		vector<int> the;
		myfile >> theCard;
		for (int i = 1; i <= 4; i++){
			if (i == theCard){
				int a;
				myfile >> a;
				for (int j = 1; j <= 4; j++){
					theStack.push_back(a);
					if (j!=4)
					myfile >> a;
				}
			}
			else {
			
				string s;
				for (int j = 1; j <= 4; j++){
					myfile >> s;
				}
			}
		}
		myfile >> theCard;
		for (int i = 1; i <= 4; i++){
			if (i == theCard){
				int a;
				myfile >> a;
				for (int j = 1; j <= 4; j++){
					the.push_back(a);
					if (j != 4)
					myfile >> a;
				}
			}
			else {
				string s;
				for (int j = 1; j <= 4; j++){
					myfile>>s;
				}
			}
		}
		int card = 0, counter1 = 0;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				if (theStack[i] == the[j]){
					card = theStack[i];
					counter1++;
				}
			}


		}
		out << "Case #" << counter << ": ";
		if (counter1 == 1){

			out << card << endl;
		}
		else if (counter1 < 1){
			out << "Volunteer cheated!" << endl;
		}
		else
			out << "Bad magician!" << endl;

		counter++;
		theStack.clear();
		the.clear();
	}
	out.close();
}