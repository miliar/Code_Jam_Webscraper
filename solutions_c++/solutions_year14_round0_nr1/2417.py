#include <iostream>
#include <fstream>
#include <cassert>
using namespace std;

//#define DEBUG

const char *infile="A-small-attempt0.in";
const char *outfile="pa-small.out";

int getAns(int row1[], int row2[]) {
    int ans=0;
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            if (row1[i] == row2[j]) {
                if (ans==0) {
                    ans=row1[i];
                    break;
                }
                else {
                    return -1;
                }
            }
        }
    }
    return ans;
}

int main() {
    ifstream fin(infile);
    assert(fin);
    ofstream fout(outfile);
    assert(fout);
    
    int test;
    fin >> test;
    for (int count=1; count<=test; count++) {
            
    #ifdef DEBUG
        cout << "current_test:" << count << endl;
    #endif
    
        int row1[4], row2[4];
        int rid1, rid2;
        
        fin >> rid1;
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                int x;
                fin >> x;
                if (i+1 == rid1) row1[j]=x;
            }
        }
        
        fin >> rid2;
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                int x;
                fin >> x;
                if (i+1 == rid2) row2[j]=x;
            }
        }
        
    #ifdef DEBUG
        cout << "row1: ";
        for (int i=0; i<4; i++) cout << row1[i] << ' ';
        cout << endl;
        
        cout << "row2: ";
        for (int i=0; i<4; i++) cout << row2[i] << ' ';
        cout << endl;
    #endif
        
        int ans = getAns(row1, row2);
        fout << "Case #" << count << ": ";
        if (ans==-1) fout << "Bad magician!";
        else if (ans==0) fout << "Volunteer cheated!";
        else fout << ans;
        fout << endl; 
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
