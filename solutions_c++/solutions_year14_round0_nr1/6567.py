#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
#include <time.h>
#include <fstream>
using namespace std;

int main()
{
    ifstream infile("A.in");
    int cases; int row1; int row2;
	int cards1[4][4]; int cards2[4][4];
    infile >> cases;
   for(int iter=1; iter<=cases; iter++) {
        infile >> row1;
        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                infile >> cards1[i][j];
            }
        }
        infile >> row2;
        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                infile >> cards2[i][j];
            }
        }

        bool match = false; bool dupflag = false;
        int card;
        for(int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
				//cout << cards1[row1-1][i] << "\t" << cards2[row2-1][j] << endl;
                if(cards1[row1-1][i] == cards2[row2-1][j]) {
                    if(match == false) {
                        match = true;
                        card = cards1[row1-1][i];
                    }
                    else {
                        dupflag = true;
                        break;
                    }
                }
            }
        }
	
		string response;
        if(match == true && dupflag == false) {
            cout << "Case #" << iter << ": " << card << endl;
        }
        else if(match == true && dupflag == true) {
            response = "Bad magician!";
			cout << "Case #" << iter << ": " << response << endl;
        }
        else {
            response = "Volunteer cheated!";
			cout << "Case #" << iter << ": " << response << endl;
        }
    }
    infile.close();
    return 0;
}

