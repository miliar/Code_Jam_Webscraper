#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

static int caseNum = 1;

int main(){
	string temp;
	ifstream file("D-small-attempt0.in");
	ofstream out("D-output.out");
	int T;
	file >> temp;
	T=stoi(temp);
	int K, C, S;
	while(T!=0){
		file >> temp;
		K=stoi(temp);
		file >> temp;
		C=stoi(temp);
		file >> temp;
		S=stoi(temp);
		cout << "Case #" << caseNum << ": ";
		out << "Case #" << caseNum << ": ";
		for(int i=0; i<S; i++){
			cout << i+1 << ' ';
			out << i+1 << ' ';
		}
		cout << endl;
		out << endl;
		T--;
		caseNum++;
	}
}