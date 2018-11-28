#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

int main(){
	int T;
	fin >> T;
	for(int t=0;t<T;t++){
		string s;
		fin >> s;
		s+="+";
		int flip=0;
		for(int i=0;i<s.size()-1;i++){
			if(s[i]!=s[i+1]) flip++;
		}
		
		fout << "Case #" << t+1 << ": " << flip << endl;
	}

	return 0;
}
