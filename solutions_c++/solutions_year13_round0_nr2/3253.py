#include <assert.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <time.h>

using namespace std;

/*
int ElapsedTime(const vector<int>& vecButtons, int index) {
	return abs(vecButtons[index] - vecButtons[index - 1]);
}
*/

struct S {
    bool bl, bc; 
    int h; 
    S() : bl(true), bc(true), h(0) {}
    void init(int ih) {
        bl = true; bc = true; h = ih; 
    }
};

S s[200][200]; 


int main(int argc, char* argv[]) {
    
	if (argc != 2) {
		cerr << "wrong number of parameter" << endl;
		return -1;
	}

	ifstream inf(argv[1]);
	if (!inf) {
		cerr << "cannot open file " << argv[1] << endl;
		return -1;
	}

    // srand(time(NULL));

	string ln;  
    inf >> ln;

    int number = atoi(ln.c_str());
    
	for (int cases=0; cases<number; cases++) 
    {
        int n, m; 
        inf >> ln; n = atoi(ln.c_str()); 
        inf >> ln; m = atoi(ln.c_str()); 

        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                inf >> ln; 
                s[i][j].init(atoi(ln.c_str())); 
            }
        }

        // check line
        for (int i=0; i<n; i++) {
            int iMax = 0; 
            for (int j = 0; j<m; j++) {
                if (s[i][j].h > iMax) iMax = s[i][j].h; 
            }

            for (int j=0; j<m; j++) {
                if (s[i][j].h < iMax) s[i][j].bl = false; 
            }
        }

        // check column
        for (int i=0; i<m; i++) {
            int iMax = 0; 
            for (int j=0; j<n; j++) {
                if (s[j][i].h > iMax) iMax = s[j][i].h; 
            }

            for (int j=0; j<n; j++) {
                if (s[j][i].h < iMax) s[j][i].bc = false; 
            }
        }

        string result = "YES"; 
        for (int i=0; i<n; i++) 
            for (int j=0; j<m; j++) {
                if (s[i][j].bc == false && s[i][j].bl == false) {
                    result = "NO";
                    break;
                }
            }

        // print result
        cout << "Case #" << (cases + 1) << ": " << result << endl;
	}

	return 0;
}
