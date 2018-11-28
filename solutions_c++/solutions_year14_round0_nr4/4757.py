#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>
using namespace std;

double KenStrat(double, vector<double>);
double NaomiStrat(vector<double>);

int main(){
	ifstream inputFile;
	const char *fileName = "D-large.in";
	inputFile.open(fileName);//change filename to input file
	ofstream outputFile("gcj2014_answer4.txt");
	int caseNumber = 0;
	int blockNumber = 0;
	double blockWeight = 0.0;
	vector<double> ken;
	vector<double> naomi;
	double kenChoice = 0.0;
	double naomiTrick = 1e-06;

	if (inputFile.is_open() && outputFile.is_open()){
	// read the case number first
	inputFile  >> caseNumber;
		for (int i=0; i<caseNumber; ++i){
			//case init
			int dScore = 0;//deceitful Naomi's score
			int rScore = 0;//regular Naomi's score
			inputFile >> blockNumber;
			//input the dice set to a vector<double>, and sort
			for (int j=0; j<blockNumber; ++j){
				inputFile >> blockWeight;
				naomi.push_back(blockWeight);
			}
			for (int j=0; j<blockNumber; ++j){
				inputFile >> blockWeight;
				ken.push_back(blockWeight);
			}
			sort(naomi.begin(),naomi.end());
			sort(ken.begin(),ken.end());

			vector<double> kenD;
			vector<double> naomiD;

			kenD = ken;
			naomiD = naomi;				
			//cheating
			while(blockNumber > 1){
				//lies
				while (*naomiD.begin() < *kenD.begin() && naomiD.begin()!= naomiD.end()-1){
					naomiD.erase(naomiD.begin());
					kenD.erase(kenD.end()-1);
					// cout<<*naomiD.begin()<<endl;
					// cout<<"cheated"<<endl;
					--blockNumber;
				}
				//surewin
				while(*(naomiD.end()-1) > *(kenD.end()-1) && naomiD.begin()!= naomiD.end()-1){
					naomiD.erase(naomiD.end()-1);
					kenD.erase(kenD.end()-1);
					++dScore;
					--blockNumber;
				}
				//another lie
				if (blockNumber > 1){
					naomiD.erase(naomiD.begin());
					kenD.erase(kenD.end()-1);
					--blockNumber;
				}
			}
			kenChoice = KenStrat(*naomiD.begin(), kenD);
			if (kenChoice != 0){
				kenD.erase(find(kenD.begin(), kenD.end(), kenChoice));
			}
			else{
				kenD.erase(kenD.begin());
				++dScore;
			}
			//Naomi's regular strategy, giving block weight sequentially
			naomiD.erase(naomiD.begin());
			//Calculate points
			while(naomi.begin()!=naomi.end()){
				//normal case
				kenChoice = KenStrat(*naomi.begin(), ken);
				if (kenChoice != 0){
					ken.erase(find(ken.begin(), ken.end(), kenChoice));
				}
				else{
					ken.erase(ken.begin());
					++rScore;
				}
				//Naomi's regular strategy, giving block weight sequentially
				naomi.erase(naomi.begin());
			}
			//Output the case into answer file under instruction
			outputFile << "Case #" << i+1 << ": " << dScore << " " << rScore << endl;
		}
		outputFile.close();
	}
	inputFile.close();
	return 0;
}

//Ken's strategy, find the lightest block that heavier than Naomi's block
double KenStrat(double naomi, vector<double> kenR){
	for (vector<double>::iterator iter = kenR.begin();iter != kenR.end();++iter){
		if (*iter > naomi){
			return *iter;
		} 
	}
	return 0;
}

					
//Point calculation

//Naomi's Deceitful Strategy, find out the best fit block
double NaomiStrat(vector<double> ken){
	return *(ken.end()-1);
}
