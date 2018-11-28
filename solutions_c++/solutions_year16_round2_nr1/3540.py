#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

int A[26];

bool ok(int A[26]){
	for(int i=0;i<26;i++){
		if(A[i]!=0)
			return false;
	}
	return true;
}

bool invailid(int A[26]){
	for(int i=0;i<26;i++){
		if(A[i]<0)
			return true;
	}
	return false;
}

std::string calc(int A[26], int last, std::string result){
	if(invailid(A)){
		return "X";
	}
	if(ok(A))
		return result;
	else{
		string found="";
		for(int i=last;i<=9;i++){
			int C[26];
			for(int j=0;j<26;j++)
				C[j]=A[j];
			if(i==0){
				//cout << "hell" << endl;
				C[int('Z')-65]--;
				C[int('O')-65]--;
				C[int('R')-65]--;
				C[int('E')-65]--;
				found = calc(C, 0,"0");
			}
			if(i==1){
				C[int('O')-65]--;
				C[int('N')-65]--;
				C[int('E')-65]--;
				found = calc(C, 1,"1");
			}
			if(i==2){
				C[int('T')-65]--;
				C[int('W')-65]--;
				C[int('O')-65]--;
				found = calc(C, 2,"2");
			}
			if(i==3){
				C[int('T')-65]--;
				C[int('H')-65]--;
				C[int('R')-65]--;
				C[int('E')-65]--;
				C[int('E')-65]--;
				found = calc(C, 3,"3");
			}
			if(i==4){
				C[int('F')-65]--;
				C[int('O')-65]--;
				C[int('U')-65]--;
				C[int('R')-65]--;
				found = calc(C, 4,"4");
			}
			if(i==5){
				C[int('F')-65]--;
				C[int('I')-65]--;
				C[int('V')-65]--;
				C[int('E')-65]--;
				found = calc(C, 5,"5");
			}
			if(i==6){
				C[int('S')-65]--;
				C[int('I')-65]--;
				C[int('X')-65]--;
				found = calc(C, 6,"6");
			}
			if(i==7){
				C[int('S')-65]--;
				C[int('E')-65]--;
				C[int('V')-65]--;
				C[int('E')-65]--;
				C[int('N')-65]--;
				found = calc(C, 7,"7");
			}
			if(i==8){
				C[int('E')-65]--;
				C[int('I')-65]--;
				C[int('G')-65]--;
				C[int('H')-65]--;
				C[int('T')-65]--;
				found = calc(C, 8,"8");
			}
			if(i==9){
				C[int('N')-65]--;
				C[int('I')-65]--;
				C[int('N')-65]--;
				C[int('E')-65]--;
				found = calc(C, 9,"9");
			}
			if(found.find("X")==std::string::npos)
				return result+found; //break;
		}
		return result+found;
	}
}


int main(){
	//cout << int('A') << endl;65
	int TC;
	cin >> TC;
	cin.ignore();
	for(int tc=1;tc<=TC;tc++){
		cout << "Case #" << tc <<": ";
		string line;
		getline(cin, line);
		memset(A, 0, sizeof(A));
		for(int i=0;i<line.size();i++)
			A[int(line[i])-65]++;
		cout << calc(A, 0, "") << endl;
	}
}