#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

void flip(vector<int> &pancakes){
	//cout<<"Flipping range: 0 - "<<bottomToFlip<<endl;
	for(int i = 0; i <= pancakes.size() - 1; i++){
		if(pancakes[i] == 1){
			pancakes[i] = 0;
		}
		else{
			pancakes[i] = 1;
		}
	}
}

void removeHappyFacesAtBottom(vector<int> &pancakes){
	int i;
	for(i = pancakes.size() - 1; i >=0; i--){
		if(pancakes[i] == 0){
			break;
		}
	}
	pancakes.erase(pancakes.begin() + i+1,pancakes.end());

}


int main(){
	ifstream input;
	input.open("B-large.in");
	ofstream output;
	output.open("B-large-output.txt");
	int cases,currentCase = 1,total,firstHappy;
	string pancakeStack;
	input>>cases;
	while(currentCase <= cases){
		total = 0;
		vector<int> pancakes;
		input>>pancakeStack;
		for(int i = 0; i < pancakeStack.length(); i++){
			if(pancakeStack[i] == '+')
				pancakes.push_back(1);
			else
				pancakes.push_back(0);
		}
		
		while(pancakes.size() > 0){
			removeHappyFacesAtBottom(pancakes);
			if(pancakes.size() > 0){
				flip(pancakes);
				removeHappyFacesAtBottom(pancakes);
				total++;
			}	
		}
		output<< "Case #" << currentCase << ": " << total << endl;
		currentCase++;
	}
}
//--+-