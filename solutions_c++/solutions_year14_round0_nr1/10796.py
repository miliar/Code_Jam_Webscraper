//By Colin Watson

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool flag = true;

void CompareArrays(int cards[][4][4],int volnum[], int count){
	bool correct = false;
	bool badmage = false;
	int correctnum;

	for(int i = 0; i < 4; i++){															//
		for(int j = 0; j < 4; j++){														// 
			if(cards[0][volnum[0] - 1][i] == cards[1][volnum[1] - 1][j]){				// Checks for a correct answer. Take one from volnum, row wasn't accounting for array starting at 0.
				if(correct == false){													// Checks if there's already been a correct answer.
					correct = true;														// 
					correctnum = cards[0][volnum[0] - 1][i];							//
				}																		//
				else																	// Multiple possible answers. Magician made a mistake, bad magician!
					badmage = true;														//
			}																			//
		}																				//
	}

	ofstream ofile;

	if(flag){
		ofile.open("output.txt");
		flag = false;
	}
	else{
		ofile.open("output.txt", ofstream::app);
	}

	ofile << "Case #" << count << ": ";

	if(badmage)
		ofile << "Bad magician!";
	else
		if(correct)
			ofile << correctnum;
		else
			ofile << "Volunteer cheated!";
	ofile << '\n';
	
	ofile.close();
}

int main(){
	int casenum,volnum[2],cards[2][4][4];
	string answer;

	ifstream myfile("input.txt");

	if(myfile.is_open())
	{
		myfile >> casenum;
		myfile.get();								//Flush for newline

		for(int i = 0; i < casenum; i++){			//Checks every case
			for(int j = 0; j < 2; j++){				//Checks both instances of a case
				myfile >> volnum[j];				//gets Volunteers row number.
				for(int k = 0; k < 4; k++){			//Refer below
					for(int l = 0; l < 4; l++){		//Gets 4 columns in 4 rows
						myfile >> cards[j][k][l];	//Stores cards in 3D array. First dimension is the question #, second and third are columns/rows for cards.
					}
				}
			}
			CompareArrays(cards, volnum, i + 1);
		}
		myfile.close();
	}
	else cout << "Unable to open file \n";

	return(0);
}