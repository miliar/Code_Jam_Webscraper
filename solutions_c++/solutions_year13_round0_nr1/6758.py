#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <regex.h>
using namespace std;

int main (int argc, char * const argv[]) {
	
    // HANDLE COMMAND-LINE ARGUMENTS
	freopen(argv[1], "rt", stdin);
//	freopen("example.in", "rt", stdin);
		
	if(argc == 3){
		freopen(argv[2], "wt", stdout);
	} else if(argc==2){
		string out = argv[1];
		out = out.substr(0, out.size() - 2);
		out += "out";
		cout << "Result file: " << out << endl;
		freopen(out.c_str(), "wt", stdout);
	} else {
		cout << "Input file required!\nUsage: ./" << argv[0] << " example.in [example.out]" << endl;
		return 0;	
	}
	
	
	int N = 0;	
	cin >> N;
	// for each test case
	for(int testCaseNum=0; testCaseNum<N; ++testCaseNum){		
		cout << "Case #" << testCaseNum+1 << ": ";
		
		char board[4][4];
		bool xwin=false, owin=false, completed=false;
		
		// input array
		int xtotal=0, ototal=0, ptotal=0; // Totals
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
				cin >> board[i][j];
				switch (board[i][j]) {
					case 'X': ++xtotal; break;
					case 'O': ++ototal; break;
					case '.': ++ptotal; break;
					default: break;
				}
			}
		}
		// if there's no periods, game has definitely completed
		if (ptotal == 0) completed = true;
		
		// Counts
		int x, o, p;
		
		// check rows
		for(int i=0;i<4;++i){
			x=0, o=0, p=0;
			for(int j=0;j<4;++j){
				switch (board[i][j]) {
					case 'X': ++x; break;
					case 'O': ++o; break;
					case '.': ++p; break;
					default: break;
				}
			}
			if (x>=3 && o==0 && p==0) {xwin = true; completed = true; goto RESULT;}
			else if (o>=3 && x==0 && p==0) {owin = true; completed = true; goto RESULT;}
		}
		
		// check cols
		for(int i=0;i<4;++i){
			x=0, o=0, p=0;
			for(int j=0;j<4;++j){
				switch (board[j][i]) {
					case 'X': ++x; break;
					case 'O': ++o; break;
					case '.': ++p; break;
					default: break;
				}
			}
			if (x>=3 && o==0 && p==0) {xwin = true; completed = true; goto RESULT;}
			else if (o>=3 && x==0 && p==0) {owin = true; completed = true; goto RESULT;}
		}
				
		// check diag 1
		x=0, o=0, p=0;
		for(int i=0;i<4;++i){
			switch (board[i][i]) {
				case 'X': ++x; break;
				case 'O': ++o; break;
				case '.': ++p; break;
				default: break;
			}
		}
		if (x>=3 && o==0 && p==0) {xwin = true; completed = true;}
		else if (o>=3 && x==0 && p==0) {owin = true; completed = true;}
		
		// check diag 2
		x=0, o=0, p=0;
		for(int i=0,j=3;i<4;++i,--j){
			switch (board[i][j]) {
				case 'X': ++x; break;
				case 'O': ++o; break;
				case '.': ++p; break;
				default: break;
			}
		}
		if (x>=3 && o==0 && p==0) {xwin = true; completed = true;}
		else if (o>=3 && x==0 && p==0) {owin = true; completed = true;}
		
		// Output result
		RESULT:
		if(xwin) cout << "X won" << endl;
		else if(owin) cout << "O won" << endl;
		else if(completed) cout << "Draw" << endl;
		else cout << "Game has not completed" << endl;
	}

	return 0;
}










