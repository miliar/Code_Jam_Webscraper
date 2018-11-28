#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <string>
using namespace std;

const int H = 0, B = 1, G = 2, D = 3;
const int MAX = 200;
char map[MAX][MAX];
bool has[4][MAX][MAX];

int result(int nbLines, int nbCols) {

    for(int iLine = 0; iLine < nbLines; iLine++) {
	for(int iCol = 0; iCol < nbCols; iCol++) {
	    for(int iDir = 0; iDir < 4; iDir++) {
		has[iDir][iLine][iCol] = false;
	    }
	}
    }

    for(int iLine = 0; iLine < nbLines; iLine++) {
	bool cur = false;
	for(int iCol = 0; iCol < nbCols; iCol++) {
	    has[G][iLine][iCol] = cur;
	    if(map[iLine][iCol] != '.') {
		cur = true;
	    }
	}
    }
    
    for(int iLine = 0; iLine < nbLines; iLine++) {
	bool cur = false;
	for(int iCol = nbCols-1; iCol >= 0; iCol--) {
	    has[D][iLine][iCol] = cur;
	    if(map[iLine][iCol] != '.') {
		cur = true;
	    }
	}
    }

    for(int iCol = 0; iCol < nbCols; iCol++) {
	bool cur = false;
	for(int iLine = 0; iLine < nbLines; iLine++) {
	    has[H][iLine][iCol] = cur;
	    if(map[iLine][iCol] != '.') {
		cur = true;
	    }
	}
    }

    for(int iCol = 0; iCol < nbCols; iCol++) {
	bool cur = false;
	for(int iLine = nbLines-1; iLine >= 0; iLine--) {
	    has[B][iLine][iCol] = cur;
	    if(map[iLine][iCol] != '.') {
		cur = true;
	    }
	}
    }    

    /*
    for(int iLine = 0; iLine < nbLines; iLine++) {
	for(int iCol = 0; iCol < nbCols; iCol++) {
	    cerr << map[iLine][iCol];
	}
	cerr << endl;
    }
    */

    for(int iLine = 0; iLine < nbLines; iLine++) {	
	for(int iCol = 0; iCol < nbCols; iCol++) {
	    if(map[iLine][iCol] != '.') {
		if(!has[0][iLine][iCol] && !has[1][iLine][iCol] && !has[2][iLine][iCol] && !has[3][iLine][iCol]) {
		    return -1;
		}
	    }
	}
    }

    int nbChanges = 0;
    for(int iLine = 0; iLine < nbLines; iLine++) {	
	for(int iCol = 0; iCol < nbCols; iCol++) {
	    if(map[iLine][iCol] == '<' && !has[G][iLine][iCol]) {
		nbChanges++;
	    }
	    if(map[iLine][iCol] == '>' && !has[D][iLine][iCol]) {
		nbChanges++;
	    }
	    if(map[iLine][iCol] == '^' && !has[H][iLine][iCol]) {
		nbChanges++;
	    }
	    if(map[iLine][iCol] == 'v' && !has[B][iLine][iCol]) {
		nbChanges++;
	    }
	}
    }
    return nbChanges;
}

int main() {
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
	int nbLines, nbCols;
	cin >> nbLines >> nbCols;

	for(int iLine = 0; iLine < nbLines; iLine++) {	
	    string str;
	    //cin.ignore();
	    cin >> str;
	    //cin.ignore();
	    for(int iCol = 0; iCol < nbCols; iCol++) {
		map[iLine][iCol] = str[iCol];
	    }
	}
		
	int res = result(nbLines,nbCols);

	if(res == -1) {
	    cout << "Case #" << t+1 <<": "
		 << "IMPOSSIBLE" << endl;
	    
	} else {
	    cout << "Case #" << t+1 <<": "
		 << res << endl;
	}
    }
    return 0;
}
