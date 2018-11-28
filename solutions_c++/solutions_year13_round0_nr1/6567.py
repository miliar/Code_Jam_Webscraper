// Anders M.L.

#include <math.h>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <vector>
#include <set>
#include <string>

using namespace std;

struct possible {
	bool x, o;
	possible() : x(true), o(true) {};
};

void update_possible(possible *p, char c) {
	if (c == 'X')
		p->o = false;
	
	if (c == 'O')
		p->x = false;
		
	if (c == '.') {		
		p->o = false; 
		p->x = false;
	}
	
}

void enter_game(int n) {
	char c;
	
	possible cols[4];
	possible TL_diag, TR_diag;
	
	int row_x, row_o;
	int num_entered=0;
	
	string s;
	
	for (int i=0; i<4; i++) {	// Row
		row_x=0; row_o=0;
		cin >> s;
		
		for (int j=0; j<4; j++) {	// Col
			c = s[j];
			update_possible(&(cols[j]), c);
			
			if (i == j)
				update_possible(&(TL_diag), c);
			
			if (j == (3 - i))
				update_possible(&(TR_diag), c);			
			
			if (c == 'T') {
				row_x++; row_o++;
			} else if (c == 'X') {
				row_x++;
			} else if (c == 'O') {
				row_o++;
			}
			if (c != '.') num_entered++;
		}
			if (row_o == 4) {
				cout << "Case #"<< n << ": O won" << endl;
				for (int flush=0; flush<3-i; i++)
					cin >> s;
				return;			
			}
			if (row_x == 4) {
				cout << "Case #"<< n << ": X won" << endl;
				for (int flush=0; flush<3-i; i++)
					cin >> s;
				return; 
			
			}		
		
				
	}
	
	possible winner;
	if (TL_diag.x || TR_diag.x || cols[0].x || cols[1].x || cols[2].x || cols[3].x) {
		cout << "Case #"<< n << ": X won" << endl;
		
	} else if (TL_diag.o || TR_diag.o || cols[0].o || cols[1].o || cols[2].o || cols[3].o) {
		cout << "Case #"<< n << ": O won" << endl;
	
	} else if (num_entered != 16) {
		cout << "Case #"<< n << ": Game has not completed" << endl;
	} else {
		cout << "Case #"<< n << ": Draw" << endl;
	}	
}

int main(){
	int c;
	cin >> c;
	for (int i=1; i<=c; i++) {
		enter_game(i);
	}

	return 0;
}
