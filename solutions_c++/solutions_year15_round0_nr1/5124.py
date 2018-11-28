#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>


using namespace std;

int main(){
	//ifstream infile("test.txt");
	//ifstream infile("A-small-attempt1.in");
	//ofstream outfile("A-small-out1.out");
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");

	int T;
	string instr;
	getline(infile, instr);
	T = stoi(instr);
	cout<<"T: "<<T<<endl;

	int Smax, culSum, addT;

	for(int t=0; t!=T; t++){
		getline(infile, instr);
		//cout<<instr<<endl;
		unsigned pos = instr.find(' ');
		//cout<<"pos: "<<pos<<"; pos char:"<<instr[pos]<<"."<<endl;
		Smax = stoi(instr.substr(0, pos));
		culSum = 0;
		addT = 0;

		for(int sIdx = 0; sIdx != Smax+1; sIdx++){
			int curN = instr[pos+1+sIdx]-'0';
			if (curN && culSum < sIdx){
				int addN = (sIdx-culSum);
				addT += addN;
				culSum += addN;
				//cout<<addN<<" people should be added"<<endl;
			}
			culSum += curN;
			//cout<<"sIdx: "<<sIdx<<"; current num: "<<curN<<"; already stand up: "<<culSum<<endl;
		}
		//cout<<"Case #"<<t+1<<": "<<addT<<endl;
		outfile<<"Case #"<<t+1<<": "<<addT<<endl;
	}
	
	infile.close();
	outfile.close();
	cout<<"haha"<<endl;
	cin.get();
	return 0;
}