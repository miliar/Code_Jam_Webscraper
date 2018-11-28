#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(){
	//ifstream fin("simple.txt");
	ifstream fin("A-large.in.txt");
	//ofstream fout("s.txt");
	ofstream fout("large.txt");
	string line;
	getline(fin, line);
	int cases = stoi(line);
	for(int i=1;i<=cases;i++){
		int max;
		fin >> max;
		string input;
		fin >> input;
		istringstream iss(input);
		char c;
		int j=0;
		int count=0;
		int people=0;
		while(iss >> c){
			cout << c << " ";
			if ((int)c-48 !=0){
				if (j > count){
					people += j-count;
					count += j-count+(int)c-48;
				}
				else{
					count += (int)c-48;
				}
			}
			j++;
		}
		fout << "Case #" << i << ": " << people << endl;
	}

	return 0;
}