#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(int argc, char* argv[]) {
	string fName=argv[1];
	string fNameOut=fName;
	fNameOut.insert(fName.rfind('.'),"_r");
	ifstream rFile(fName.c_str());
	ofstream wFile(fNameOut.c_str());
	int T;
	rFile >> T;
	for(int t=0;t<T;++t) {
		vector<string> mat(4,"");
		for(int i=0;i<4;++i){
			rFile >> mat[i];
		}
		int c=0;
		bool done=false;
		for(int i=0;i<4;++i) {
			c=0;
			for(int j=0;j<4;++j) {
				if(mat[i][j]=='X' || mat[i][j]=='T') {
					c++;
				}
			}
			if(c==4) {
				done=true;
				break;
			}
		}
		for(int i=0;i<4;++i) {
			c=0;
			for(int j=0;j<4;++j) {
				if(mat[j][i]=='X' || mat[j][i]=='T') {
					c++;
				}
			}
			if(c==4) {
				done=true;
				break;
			}
		}
		c=0;
		for(int i=0;i<4;++i) {
			if(mat[i][i]=='X' || mat[i][i]=='T') {
				c++;
			}
		}
		if(c==4)
			done=true;
		c=0;
		for(int i=0;i<4;++i) {
			if(mat[i][4-i-1]=='X' || mat[i][4-i-1]=='T') {
				c++;
			}
		}
		if(c==4)
			done=true;
		if(done) {
			wFile << "Case #" << (t+1) << ": X won" << endl;
			continue;
		}
		c=0;
		for(int i=0;i<4;++i) {
			c=0;
			for(int j=0;j<4;++j) {
				if(mat[i][j]=='O' || mat[i][j]=='T') {
					c++;
				}
			}
			if(c==4) {
				done=true;
				break;
			}
		}
		for(int i=0;i<4;++i) {
			c=0;
			for(int j=0;j<4;++j) {
				if(mat[j][i]=='O' || mat[j][i]=='T') {
					c++;
				}
			}
			if(c==4) {
				done=true;
				break;
			}
		}
		c=0;
		for(int i=0;i<4;++i) {
			if(mat[i][i]=='O' || mat[i][i]=='T') {
				c++;
			}
		}
		if(c==4)
			done=true;
		c=0;
		for(int i=0;i<4;++i) {
			if(mat[i][4-i-1]=='O' || mat[i][4-i-1]=='T') {
				c++;
			}
		}
		if(c==4)
			done=true;
		if(done) {
			wFile << "Case #" << (t+1) << ": O won" << endl;
			continue;
		}
		c=0;
		for(int i=0;i<4;++i) {
			for(int j=0;j<4;++j) {
				if(mat[i][j]=='.') {
					c++;
				}
			}
		}
		if(c>0)
			wFile << "Case #" << (t+1) << ": Game has not completed" << endl;
		else
			wFile << "Case #" << (t+1) << ": Draw" << endl;
	}
	rFile.close();
	wFile.close();
	return 0;
}
