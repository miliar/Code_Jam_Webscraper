// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main () {
	const bool HAPPY = true;
	
	string line;
	ifstream myfile ("B-large.in");
	ofstream outfile;
	outfile.open ("output.txt");
	
	if (myfile.is_open())
	{
		getline (myfile,line);
		int caseNum = 1;
		
		while ( getline (myfile,line))
		{
			vector<bool> pancakeStack;
			int lowestDiffIndex = 0, flips = 0;
			
			for(int i = 0; i < line.size(); i++) {
				
				if(line[i] == '+') {
					pancakeStack.insert(pancakeStack.begin(), HAPPY);
				} else if(line[i] == '-') {
					pancakeStack.insert(pancakeStack.begin(), !HAPPY);
				}
			}
			
			lowestDiffIndex = pancakeStack.size() - 1;
			for(int i = lowestDiffIndex; i >= 0; i--) {
				if(pancakeStack[i] == HAPPY) {
					cout << "+";
				} else {
					cout << "-";
				}
			}
			
			while(lowestDiffIndex > 0) {
				if(pancakeStack[lowestDiffIndex] != pancakeStack[lowestDiffIndex-1]) {
					for(int i = lowestDiffIndex; i < pancakeStack.size(); i++) {
						pancakeStack[i] = !pancakeStack[i];
					}
					flips++;
				}
				else {
					lowestDiffIndex--;
				}
			}
			
			if(lowestDiffIndex == 0 && pancakeStack[0] == !HAPPY) {
				flips++;
			}
			
			outfile << "Case #" << caseNum << ": " << flips << "\n";
			cout << "Case #" << caseNum << ": " << flips << "\n";
			caseNum++;
		}
		myfile.close();
	}
	else cout << "Unable to open file"; 
	
	return 0;
}
