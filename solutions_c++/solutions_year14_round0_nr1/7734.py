#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;
ifstream input;
ofstream output;
int numOfCases;
int yf;
int ys;
string tmp;
int cards[8][4];
vector<string> answers;
vector<int> first;
vector<int> second;

void solve(int currentCase){
	int repeating=0;
	int findDigit;
	
	for(int i=0;i<4;i++)
		first.push_back(cards[yf-1][i]);
	for(int i=0;i<4;i++)
		second.push_back(cards[3+ys][i]);
	
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(first[i]==second[j]){
				repeating++;
				findDigit = second[j];
			}
	if(repeating==1)
		output<<"Case #"+to_string(currentCase)+": "<<findDigit<<endl;
	if(repeating==0)
		output<<"Case #"+to_string(currentCase)+": "<<"Volunteer cheated!"<<endl;
	if(repeating>1)
		output<<"Case #"+to_string(currentCase)+": "<<"Bad magician!"<<endl;
	first.clear();
	second.clear();
}

void openFile(){	
	int currentCase=1;
	int k=1;
	input.open("c:\\input.in",ifstream::in);
	output.open("c:\\output.out",ofstream::out);
	input>>tmp;
	numOfCases = atoi(tmp.c_str());
	
	while(!input.eof()){
			input>>tmp;
			yf = atoi(tmp.c_str());
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					input>>tmp;
					cards[i][j]=atoi(tmp.c_str());
				}
			}
			input>>tmp;
			ys = atoi(tmp.c_str());
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					input>>tmp;
					cards[i+4][j]=atoi(tmp.c_str());
				}
			}
			if((k++)<=numOfCases)
				solve(currentCase++);

	}
}
int main(){
	openFile();
	cout<<"end";
	getchar();
	return 0;
}