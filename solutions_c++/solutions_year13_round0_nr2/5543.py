#include <iostream>
#include <string>
#include <string.h>
#include <sstream>
#include <vector>
#include <stdlib.h>
#include <fstream>

using namespace std;

/* Function Prototypes */
bool readLawnPattern();

bool compareLawns();
void trimLawn();
void trimCheckRow(int row);
void trimCheckCol(int col);
void trimRow(int row, int val);
void trimColumn(int col, int val);

string processTestCase();



/* Global Variables */
int T,N,M;

int maxHeight;

vector< vector<int> > lawnPattern;
vector< vector<int> > lawnTrim;

int main() {
    string str;

    cin >> T;
    getline(cin,str);
    str.erase();
    if(T<1 && T>100) return 1;
    
    for (int t=0;t<T;t++ ) {
        cout << "Case #" << t+1 << ": " << processTestCase() << endl;
        lawnPattern.clear();
        lawnTrim.clear();
    }
   
    return 0;
}

string processTestCase() {
    
    if(!readLawnPattern()){
        return "NO";
    }

    trimLawn();                 // Trims the Lawn
    
    
    if(compareLawns()){
        return "YES";
    }
    
    return "NO";
}

void trimLawn() {
    int i,j;

    trimCheckRow(0);
    trimCheckRow(N-1);
    
    trimCheckCol(0);
    trimCheckCol(M-1);

    return;
}


void trimCheckRow(int row) {
    int i,j;

    i=row;
    for (j=0;j<M;j++) {
        trimColumn(j,lawnPattern[i][j]);
    }
}

void trimCheckCol(int col) {
    int i,j;

    j=col;
    for (i=0;i<N;i++ ) {
        trimRow(i,lawnPattern[i][j]);
    }
}

void trimRow(int row, int val) {
    for (int k=0;k<M;k++ ) {
        if(lawnPattern[row][k] > val || lawnTrim[row][k] < val){
            return;
        }
    }

    for (int k=0;k<M;k++ ) {
        lawnTrim[row][k] = val;
    }

}

void trimColumn(int col, int val) {
    for (int k=0;k<N;k++ ) {
        if(lawnPattern[k][col] > val || lawnTrim[k][col] < val){
            return;
        }
    }

    for (int k=0;k<N;k++ ) {
        lawnTrim[k][col] = val;
    }
}

bool readLawnPattern(){
    int temp;
    
    cin >> N;
    cin >> M;
    if(N<1 && N>100) return false;
    if(M<1 && M>100) return false;

    maxHeight = 0;
    for (int i=0;i<N;i++ ) {
        vector<int> row;
        for (int j=0;j<M;j++ ) {
            cin >> temp;
            if(temp < 1 && temp >100) return false;
            if(maxHeight < temp ) maxHeight = temp;
            row.push_back(temp);
        }
        lawnPattern.push_back(row);
    }
        
    for (int i=0;i<N;i++ ) {
        vector<int> row;
        for (int j=0;j<M;j++ ) {
            row.push_back(maxHeight);
        }
        lawnTrim.push_back(row);
    }
    
    return true;
}

bool compareLawns(){
    for (int i=0;i<N;i++ ) {
        for (int j=0;j<M;j++ ) {
            if(lawnPattern[i][j] != lawnTrim[i][j] ){
                return false;
            }
        }
    }    
    return true;
}

