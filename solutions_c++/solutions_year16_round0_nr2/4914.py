#include <iostream>
#include <fstream>
#include <string>
using namespace std;


char rev(char c){
	if(c=='+'){
		return '-';
	} 
	return '+';
}



int main() {
	ifstream fin("b.txt");
	ofstream fout("output.txt");
	int t;
	fin >> t;
	int n,i,j,result,shagy;
	string s;
	for(int test=1;test<=t;test++){
		fin >> s;
		shagy=0;
		for(i=0;i<s.size();i++){
			while(s[i] == s[i+1]){
				i++;
			}
			shagy++;
		}
		if(s[s.size()-1]=='-'){
			fout << "Case #" << test << ": " << shagy << endl;
		} else {
			fout << "Case #" << test << ": " << shagy-1 << endl;
		}
 		
	}
	return 0;
}
