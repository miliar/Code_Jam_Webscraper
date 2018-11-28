#include <string>
#include <sstream>
#include <vector>
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    string s;
    ios::sync_with_stdio(false);
    
    getline(cin, s);
    int n = atoi(s.c_str());
    for (int i = 0; i < n; i++) {
        getline(cin, s);

	istringstream ss(s);
	string stmp;
	getline(ss, stmp, ' ');
	int n_omino = atoi(stmp.c_str());
	getline(ss, stmp, ' ');
	int rsize = atoi(stmp.c_str());
	getline(ss, stmp, ' ');
	int csize = atoi(stmp.c_str());

	bool isRichardWin = false;
	if ((n_omino >= 7) ||
	    (rsize * csize < n_omino) ||
	    ((rsize * csize) % n_omino != 0)) {
	    isRichardWin = true;
	}
	else {
	    if (n_omino == 1) {
	    }
	    else if (n_omino == 2) {
	    }
	    else if (n_omino == 3) {
		if (rsize <= 1 || csize <= 1) {
		    isRichardWin = true;
		}
	    }
	    else {
		if (rsize <= 2 || csize <= 2) {
		    isRichardWin = true;
		}
	    }
	}
        cout << "Case #" << i+1 << ": " << 
                (isRichardWin ? "RICHARD" : "GABRIEL")
             << endl;
    }
    return 0;
}