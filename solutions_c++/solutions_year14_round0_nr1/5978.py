#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char* argv[]){
	ifstream data(argv[1]);
	if(!data){cerr << "Couldn't open file." << endl; return -1;}

	ofstream output("problemA.out");

	int cases;
	data >> cases;

	for(int c = 1; c <= cases; c++){
		vector<int> possible;
		
		int row1;
		data >> row1;

		for(int sB = 1; sB < row1; sB++){
			for(int w = 0; w <= 3; w++){int t; data >> t;}
		}

		for(int r = 0; r <= 3; r++){
			int temp;
			data >> temp;
			possible.push_back(temp);
		}
		
		for(int sA = 4; sA > row1; sA--){
			for(int w = 0; w <= 3; w++){int t; data >> t;}
		}

		int row2;
		data >> row2;

		for(int sB = 1; sB < row2; sB++){
			for(int w = 0; w <= 3; w++){int t; data >> t;}
		}

		for(int r = 0; r <= 3; r++){
			int temp;
			data >> temp;
			possible.push_back(temp);
		}
		
		for(int sA = 4; sA > row2; sA--){
			for(int w = 0; w <= 3; w++){int t; data >> t;}
		}

		sort(possible.begin(), possible.end());

//		cout << "case is " << c << endl;
//		for(int x = 0; x < possible.size(); x++){
//			cout << possible.at(x) << endl;
//		}

		int card = 0;

		for(int i = 1; i < possible.size(); i++){
			if(possible.at(i) == possible.at(i-1)){
				if(card != 0){output << "Case #" << c << ": Bad Magician!" << endl; card = -1; break;}
				else{card = possible.at(i);}
			}
		}

		if(card == -1){continue;}
		else if(card == 0){output << "Case #" << c << ": Volunteer cheated!" << endl;}
		else{output << "Case #" << c << ": " << card << endl;}
	}

	data.close();
	output.close();
}
