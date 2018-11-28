#include <fstream>
#include <sstream>
#include <string>
#include <iostream>

using namespace std;

int t;

string check (char m[4][4], bool e) {

    for (int i=0; i<4; i++) {
        
        int s = 0;
        if (m[i][0] != '.' && m[i][1] != '.') {
            if (m[i][0] == 'T') s = 1;
            bool f = true;
            for (int j=1; j<4; j++) {
                if (m[i][j] != m[i][s] && m[i][j] != 'T') {
                    f = false;
                    break;
                }
            }
            
            if (f) {
                stringstream ss;
                string st;
                ss << m[i][s];
                ss >> st;
                return st + " won";
            }
        }
    }
    
    for (int i=0; i<4; i++) {
        
        int s = 0;
        if (m[0][i] != '.') {
            if (m[0][i] == 'T' && m[1][0] != '.') s = 1;
        
            bool f = true;
            for (int j=1; j<4; j++) {
                if (m[j][i] != m[s][i] && m[j][i] != 'T') {
                    f = false;
                    break;
                }
            }
            
            if (f) {
                stringstream ss;
                string st;
                ss << m[s][i];
                ss >> st;
                return st + " won";
            }
        }
    }
    
    if (m[0][0] != '.') {
        int sh = 0;
        if (m[0][0] == 'T' && m[1][1] != '.') sh = 1;
        bool f = true;
        for (int i=1; i<4; i++) {
            if (m[i][i] != m[sh][sh] && m[i][i] != 'T') {
                f = false;
                break;
            }
        }
        
        if (f) {
            stringstream ss;
            string s;
            ss << m[sh][sh];
            ss >> s;
            return s + " won";
        }
    }
    
    if (m[0][3] != '.') {
        int sh = 0;
        if (m[0][3] == 'T' && m[1][2] != '.') sh = 1;
        bool f = true;
        for (int i=1; i<4; i++) {
            if (m[i][3-i] != m[sh][3-sh] && m[i][3-i] != 'T') {
                f = false;
                break;
            }
        }
        
        if (f) {
            stringstream ss;
            string s;
            ss << m[sh][3-sh] << " won";
            ss >> s;
            return s + " won";
        }
    }
    
    if (e) return "Game has not completed";
    else return "Draw";

}


int main () {

    ifstream in ("A-small-attempt1.in");
    ofstream out ("A-small-att1.out");

    in >> t;
    
    
    for (int i=0; i<t; i++) {
    
        char m[4][4];
        bool empty = false;
    
        for (int j=0; j<4; j++)
            for (int k=0;k<4;k++) {
                char a;
                in >> a;
                if (a == '.')
                    empty = true;
                m[j][k] = a;
            }
        
        out << "Case #" << i+1 << ": " << check (m, empty) << endl;
    }
}
