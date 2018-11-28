#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <math.h>

using namespace std;

#define toDigit(c) (c-'0')
int totalProblemNum;
vector<vector<int>>  problemArray;

vector<string> &split(const string &s, char delim, vector<string> &elems) {
	stringstream ss(s);
	string item;
	while (getline(ss, item, delim)) {
		elems.push_back(item);
	}
	return elems;
}

vector<string> split(const string &s, char delim) {
	vector<string> elems;
	split(s, delim, elems);
	return elems;
}

void readTxtFile(string fileName){
	string line;
	ifstream myfile (fileName);
	bool isOdd=true;
	if (myfile.is_open()){
		bool isFirstLine=true;		
		unsigned long stringLength=1;
		unsigned long stringRepeatNum=1;
		while ( getline (myfile,line) ){			
			if (isFirstLine){
				isFirstLine = false;
				totalProblemNum = atoi(line.c_str());				
			}else{
				if(isOdd){				
					isOdd = false;
					vector<string> tmpLine = split(line, ' ');
					//stringLength = atoi(tmpLine[0].c_str());
					//stringRepeatNum = atoi(tmpLine[1].c_str());					
				}else{
					isOdd=true;
					vector<int> subProblemArray;
					vector<string> tmpLine = split(line, ' ');					
					for (int i=0; i<tmpLine.size(); i++)
						subProblemArray.push_back(atoi(tmpLine[i].c_str()));
					problemArray.push_back(subProblemArray);
				}
			}
		}
		myfile.close();
	}

	else cout << "Unable to open file"; 
}

int main () {

	//read Problem txt file
	readTxtFile("A-large.in");
	cout << "\n" << "\n";

	ofstream myfile ("A-large_out.txt");
	if (myfile.is_open()){
		for(int i = 0 ; i< totalProblemNum ; i++){							
									
			int case1Result =0;
			int diffMax = 0;
			for (int j=0; j<problemArray[i].size()-1;j++){
				if (problemArray[i][j] > problemArray[i][j+1]){
					int tmpDIffmax = problemArray[i][j] - problemArray[i][j+1];
					case1Result += tmpDIffmax;
					if(tmpDIffmax > diffMax) diffMax = tmpDIffmax;
				}
			}

			int case2Result =0;
			for (int j=0; j<problemArray[i].size()-1;j++){
				if (problemArray[i][j] <= diffMax){
					case2Result += problemArray[i][j];
				}else {
					if(diffMax !=0)
						case2Result += diffMax;
				}
			}
			//myfile << "Case #" << i+1 << ": YES" << "\n";		
			myfile << "Case #" <<i+1 << ": "<<  case1Result << " " << case2Result<< "\n";		
		}
	}
	return 0;
}