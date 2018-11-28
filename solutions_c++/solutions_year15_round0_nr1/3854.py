#include <iostream>
#include <fstream>
using namespace std;

int main() {
	// your code goes here
	int testNum;
	ifstream infile;
	ofstream outfile;
	infile.open("A-large.in");
	outfile.open("A-large.out");
	infile>>testNum;
	
	for(int i = 0; i< testNum; i++){
		int length;
		char ch;
		int inviteNum = 0;
		int standNum = 0;
		infile>>length;
		for(int j = 0; j< length+1; j++){
			infile>>ch;
			standNum += (ch-'0');
			while(standNum<=j){
				standNum++;
				inviteNum ++;
			}
		}
		outfile<<"Case #"<<i+1<<": "<<inviteNum<<endl;
		
	}
	outfile.close();
	infile.close();
	return 0;
}
