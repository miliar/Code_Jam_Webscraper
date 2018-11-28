#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

template<typename T>
void print(const vector<T> &vec){
	for (int j=0; j!=vec.size(); ++j)
		cout<<vec[j]<<" ";
	cout<<endl;
}

template<typename T>
void print(const vector<vector<T>> &mat){
	for (int j=0; j!=mat.size(); ++j)
		print(mat[j]);
	cout<<endl;
}

void multiplyCheck(vector<vector<char>> &cTable, vector<vector<int>> &sTable);

void createTable(vector<vector<char>> &charTable, vector<vector<int>> &signTable){
	vector<char> rowVec(4, '0');
	vector<int> sVec(4, true);
	for(int r=0; r!=4; r++){
		switch(r){
		case 0:
			rowVec[0]='1'; rowVec[1]='i'; rowVec[2] = 'j'; rowVec[3] = 'k'; 
			sVec[0] = 1; sVec[1] = 1; sVec[2] = 1; sVec[3] =1; 
			break;
		case 1:
			rowVec[0]='i'; rowVec[1]='1'; rowVec[2] = 'k'; rowVec[3] = 'j'; 
			sVec[0] = 1; sVec[1] = -1; sVec[2] = 1; sVec[3] = -1; 
			break;
		case 2:
			rowVec[0]='j'; rowVec[1]='k'; rowVec[2] = '1'; rowVec[3] = 'i'; 
			sVec[0] = 1; sVec[1] = -1; sVec[2] = -1; sVec[3] = 1; 
			break;
		case 3:
			rowVec[0]='k'; rowVec[1]='j'; rowVec[2] = 'i'; rowVec[3] = '1'; 
			sVec[0] = 1; sVec[1] = 1; sVec[2] = -1; sVec[3] = -1; 
			break;
		}
		charTable.push_back(rowVec);
		signTable.push_back(sVec);
	}
}

void concatStr(string &myStr, string &segmentStr, int n){
	if(n>1){
		string newSegStr(segmentStr);
		newSegStr.append(newSegStr);
		concatStr(myStr, newSegStr, n/2);
		if (n%2)
			myStr.append(segmentStr);
	}else if(n==1){
		myStr = segmentStr;
	}
}

void readString(ifstream &infile, string &myStr){
	string instr;
	getline(infile, instr);
	int L, X;
	stringstream sstr = stringstream(instr);
	sstr>>L;
	sstr>>X;	
	getline(infile, instr);
	cout<<"L: "<<L<<"; X: "<<X<<endl;
	//cout<<"template: "<<instr<<endl;
	concatStr(myStr, instr, X);
}

bool CorrectSpelling(string &myStr, vector<vector<char>> &cTable, vector<vector<int>> &sTable);

int main(){
	//ifstream infile("test.txt");
	ifstream infile("C-small-attempt1.in");
	ofstream outfile("C-small-out1.out");
	
	int testNtot;
	string instr;
	getline(infile, instr);
	testNtot = stoi(instr);
	cout<<"total number of tests: "<<testNtot<<endl;

	vector<vector<char>> cTable;
	vector<vector<int>> sTable;
	createTable(cTable, sTable);
	//print(cTable);
	//print(sTable);
	//multiplyCheck(cTable, sTable);

	for(int testN=0; testN != testNtot; testN++){
		string myStr;
		readString(infile, myStr);
		if (myStr.size()<10)
			cout<<"length "<<myStr.size()<<" str: "<<myStr<<endl;
	
		bool flag = CorrectSpelling(myStr, cTable, sTable);
		if(flag){
			cout<<"Case #"<<testN+1<<": YES"<<endl;
			outfile<<"Case #"<<testN+1<<": YES"<<endl;
		}else{
			cout<<"Case #"<<testN+1<<": NO"<<endl;
			outfile<<"Case #"<<testN+1<<": NO"<<endl;
		}
		
	}
	
	cin.get();
	return 0;
}

int myConverter(char c){
	switch(c){
	case '1':
		return 0;
	case 'i':
		return 1;
	case 'j':
		return 2;
	case 'k':
		return 3;
	default:
		return -1;
	}
}

void stripStr(string &str, char &c, int &sign){
	sign = str[0]=='-'?-1:1;
	c = sign==1?str[0]:str[1];
}
string Multiplier(char c1, char c2, int sign, vector<vector<char>> &cTable, vector<vector<int>> &sTable){	
	int ridx = myConverter(c1);
	int cidx = myConverter(c2);
	char c = cTable[ridx][cidx];
	int sign2 = sTable[ridx][cidx];
	string str = "";
	if(sign*sign2<0)
		str.push_back('-');
	str.push_back(c);
	return str;
}

bool CorrectSpelling(string &myStr, vector<vector<char>> &cTable, vector<vector<int>> &sTable){
	string lstr="1", mstr="1", rstr="1";
	char c; int sign;
	int idx1, idx2;
	for(idx1=0; idx1+2<myStr.size(); idx1++){
		stripStr(lstr, c, sign);
		lstr = Multiplier(c, myStr[idx1], sign, cTable, sTable);
		if (lstr=="i")
			break;
	}
	if(idx1+2==myStr.size())
		return false;
	for(idx2 = int(myStr.size())-1; idx1+2 <= idx2; idx2--){
		stripStr(rstr, c, sign);
		rstr = Multiplier(myStr[idx2], c, sign, cTable, sTable);
		if (rstr=="k")
			break;
	}
	if(idx1+2 > idx2)
		return false;
	for(int idx = idx1+1; idx!=idx2; idx++){
		stripStr(mstr, c, sign);
		mstr = Multiplier(c, myStr[idx], sign, cTable, sTable);
	}
	if(mstr=="j")
		return true;
	else
		return false;
}

void multiplyCheck(vector<vector<char>> &cTable, vector<vector<int>> &sTable){
	string str1 = "1ijk";
	string str2 = "1ijk";
	for(int i=0; i!=str1.size(); i++){
		for(int j=0; j!=str2.size(); j++){
			cout<<str1[i]<<"*"<<str2[j]<<"="<<Multiplier(str1[i], str2[j], 1, cTable, sTable)<<endl;
		}
	}
}