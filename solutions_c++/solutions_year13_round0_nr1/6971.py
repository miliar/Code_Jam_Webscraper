#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
bool inline isHorizontalOf(const vector<string>& vs,char c) {
	for(int i=0;i<4;i++){
		if(vs[i][0] == c || vs[i][0] == 'T')
		if(vs[i][1] == c || vs[i][1] == 'T')
		if(vs[i][2] == c || vs[i][2] == 'T')
		if(vs[i][3] == c || vs[i][3] == 'T')
		return 1;
	}
	return 0;	
}
bool inline isVerticalOf(const vector<string> &vs,char c) {
	for(int i=0;i<4;i++){
		if(vs[0][i] == c || vs[0][i] == 'T')
		if(vs[1][i] == c || vs[1][i] == 'T')
		if(vs[2][i] == c || vs[2][i] == 'T')
		if(vs[3][i] == c || vs[3][i] == 'T')
		return 1;
	}
	return 0;
}
bool inline isDiagonalOf(const vector<string>& vs,char c) {
	
	if(vs[0][0] == c || vs[0][0] == 'T')
	if(vs[1][1] == c || vs[1][1] == 'T')
	if(vs[2][2] == c || vs[2][2] == 'T')
	if(vs[3][3] == c || vs[3][3] == 'T')
	return 1;
	if(vs[0][3] == c || vs[0][3] == 'T')
	if(vs[1][2] == c || vs[1][2] == 'T')
	if(vs[2][1] == c || vs[2][1] == 'T')
	if(vs[3][0] == c || vs[3][0] == 'T')
	return 1;
	return 0;
}
bool inline didXwin(const  vector<string> &vs) {
	return  isHorizontalOf(vs,'X') || isVerticalOf(vs,'X') || isDiagonalOf(vs,'X');
}
bool inline didYwin(const  vector<string>& vs) {
	return  isHorizontalOf(vs,'O') || isVerticalOf(vs,'O') || isDiagonalOf(vs,'O');
}
bool inline isGameEnd(const vector<string>& vs) {
	for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(vs[i][j] == '.') return 0;
	return 1;
}
void determine(const  vector<string>& vs,ofstream & out) {
	bool didX = didXwin(vs);
	bool didY = didYwin(vs);
	if(didX) {
		out << "X won" << endl;
		return;
	}
	if(didY) {
		out << "O won" << endl;
		return;
	}
	if(isGameEnd(vs)) {
		out << "Draw" << endl;
		return;
	}
	out << "Game has not completed" << endl;
}
int main() {
	vector<string> vs;
	int T;
	ifstream in("A-large.in");
	ofstream out("out.txt");
	
	in >> T;
	string tmp;
	for (int i=1;i<=T;i++) {
		vs.clear();
		tmp  ="";
		for (int j=0;j<4;j++) {
			in >> tmp;
			vs.push_back(string(tmp));
		}	
		out << "Case #" << i << ": ";
		determine(vs,out);
	}
	in.close();
	out.close();
	return 0;
}
