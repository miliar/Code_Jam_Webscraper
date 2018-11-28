#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <math.h>

using namespace std;

#define toDigit(c) (c-'0')
int totalProblemNum;
vector<string>  problemArray;

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
					stringLength = atoi(tmpLine[0].c_str());
					stringRepeatNum = atoi(tmpLine[1].c_str());					
				}else{
					isOdd=true;
					vector<int> subProblemArray;
					vector<string> tmpLine = split(line, ' ');
					string tmpResultLine ="";
					for (int i=0; i<stringRepeatNum; i++)
						tmpResultLine += tmpLine[0];					
					problemArray.push_back(tmpResultLine);
				}
			}
		}
		myfile.close();
	}

	else cout << "Unable to open file"; 
}

string charConversion(string a_string, string b_string){
	string c;
	char a,b;
	bool a_negative = false;
	bool b_negative = false;
	bool sign_result = false;
	if(a_string.size() >1) { a = a_string[1]; a_negative=true;}
	else a = a_string[0];
	if(b_string.size() >1) {b = b_string[1]; b_negative=true;}
	else b = b_string[0];
	
	sign_result = a_negative^b_negative;

	if		(a == '1' && b == '1') c = "1";
	else if (a == '1' && b == 'i') c = "i";
	else if (a == '1' && b == 'j') c = "j";
	else if (a == '1' && b == 'k') c = "k";

	else if (a == 'i' && b == '1') c = "i";
	else if (a == 'i' && b == 'i') c = "-1";
	else if (a == 'i' && b == 'j') c = "k";
	else if (a == 'i' && b == 'k') c = "-j";

	else if (a == 'j' && b == '1') c = "j";
	else if (a == 'j' && b == 'i') c = "-k";
	else if (a == 'j' && b == 'j') c = "-1";
	else if (a == 'j' && b == 'k') c = "i";
	
	else if (a == 'k' && b == '1') c = "k";
	else if (a == 'k' && b == 'i') c = "j";
	else if (a == 'k' && b == 'j') c = "-i";
	else if (a == 'k' && b == 'k') c = "-1";
	

	if (c.size() > 1){
		if(sign_result)
			return string(1,c[1]);
		else
			return c;
	}else{
		if(sign_result)
			return "-"+c;
		else
			return c;
	}
}

int main () {
	
	//read Problem txt file
	readTxtFile("C-small-attempt1.txt");
	cout << "\n" << "\n";

	ofstream myfile ("problem3Result_small.txt");
	if (myfile.is_open()){
		for(int i = 0 ; i< totalProblemNum ; i++){							
			bool i_passed = false;
			bool j_passed = false;
			bool k_passed = false;
			int j=0;
			string currentChar(1, problemArray[i][j]);
			string nextChar;
			while(j <  problemArray[i].size()-1){			
				
				nextChar =  problemArray[i][j+1];
				
				if (!i_passed){
					if (currentChar.compare("i") == 0){
						i_passed = true;
						currentChar = nextChar;
					}else{
						currentChar = charConversion(currentChar,nextChar);						
					}					
				}else if(i_passed && !j_passed){
					if (currentChar.compare("j") == 0){
						j_passed = true;
						currentChar = nextChar;
					}else{
						currentChar = charConversion(currentChar,nextChar);						
					}
				}else if(i_passed && j_passed && !k_passed){					
					currentChar = charConversion(currentChar,nextChar);											
				}	
				j++;
			}
			if (currentChar.compare("k") == 0){
				k_passed = true;
			}
			
			if (i_passed && j_passed && k_passed)
				myfile << "Case #" << i+1 << ": YES" << "\n";		
			else
				myfile << "Case #" << i+1 << ": NO" << "\n";					
			
		}
	}
	return 0;
}