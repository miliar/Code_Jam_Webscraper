#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

int main(){
	using namespace std;
	ofstream ofile;
	ifstream ifile;

	ifile.open("A-small-attempt0.in");
	ofile.open("output.txt");

	if (ifile.is_open()){
		string line;
		getline(ifile, line);
		int casen = stoi(line);

		for (int CASE = 0; CASE < casen; CASE++){
			getline(ifile, line);
			int firstq = stoi(line);
			vector<int> firstRow;
			vector<int> secondRow;
			for (int i = 1; i <= 4; i++){
				getline(ifile, line);
				if (i == firstq){
					string one, two, three, four;
					stringstream ss(line);
					ss >> one;
					ss >> two;
					ss >> three;
					ss >> four;
					firstRow.push_back(stoi(one));
					firstRow.push_back(stoi(two));
					firstRow.push_back(stoi(three));
					firstRow.push_back(stoi(four));
				}
			}
			getline(ifile, line);
			int secondq = stoi(line);
			for (int i = 1; i <= 4; i++){
				getline(ifile, line);
				if (i == secondq){
					string one, two, three, four;
					stringstream ss(line);
					ss >> one;
					ss >> two;
					ss >> three;
					ss >> four;
					secondRow.push_back(stoi(one));
					secondRow.push_back(stoi(two));
					secondRow.push_back(stoi(three));
					secondRow.push_back(stoi(four));
				}
			}
			int cardn;
			int totalSimilarities = 0;
			for (int a = 0; a < firstRow.size(); a++){
				for (int b = 0; b < secondRow.size(); b++){
					if (firstRow[a] == secondRow[b]){
						totalSimilarities++;
						cardn = firstRow[a];
					}
				}
			}
			string o;
			if (totalSimilarities == 1) o = to_string(cardn);
			else if (totalSimilarities == 0) o = "Volunteer cheated!";
			else if (totalSimilarities > 1) o = "Bad magician!";
			ofile << "Case #" << to_string(CASE+1) + ": " << o << endl;
		}
	}

	ofile.close();
}