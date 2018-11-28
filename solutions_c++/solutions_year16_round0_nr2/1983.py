#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
	ifstream fin("test.in");
	ofstream fout("test.out");
	int T;
	fin >> T;
	for (int i=1;i<T+1;i++){
		string temp;
		fin >> temp;
		int count=0;
		for (int j=0;j<(temp.length()-1);j++){
			if (temp[j]!=temp[j+1]) count++;
		}
		if (temp[temp.length()-1]=='-') count++;
		
		fout << "Case #" << i << ": " << count << endl;
	}
	system("pause");
}