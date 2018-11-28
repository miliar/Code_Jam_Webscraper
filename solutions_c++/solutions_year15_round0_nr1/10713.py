#include <stack>
#include <iostream>
#include <fstream>
using namespace std;

int findReq(int level, int aud){
	stack<int> auds;
	while (aud > 0){
		auds.push(aud % 10);
		aud = aud / 10;
	}
	while (auds.size() < level + 1){
		auds.push(0);
	}
	int req = 0;
	int clev = 0;
	int ctot = 0;
	while (auds.size() > 0 && ctot < level){
		int p = auds.top();
		if (clev > ctot){
			req += 1;
			ctot += 1;
		}
		else{
			ctot += p;
			clev++;
			auds.pop();
		}
	}
	return req;
}

int main(){
	int count;
	ifstream rfile;
	rfile.open("A-small-attempt0.in");
	rfile >> count;
	ofstream output("output.txt");
	for (int i = 0; i < count; ++i){
		int level;
		rfile >> level;
		int aud;
		rfile >> aud;
		output << "Case #" << (i + 1) << ": " <<  findReq(level, aud) << endl;
	}
}