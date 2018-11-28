#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cmath>

using namespace std;
typedef long long INT;
typedef vector<INT> INTVec;
typedef long double FLOAT;

#define PI 3.141592653

inline INT paint_len(INT r, INT n) {
    return 2 * (n * r + n * (n - 1)) + n;
    // FLOAT log_n = log(n);
    // return log_n + log(2 * r + 2 * n - 1);
}

INT cal_circle_num(INT r, INT t) {
    INT i = 1;
    // FLOAT logt =  log(t);
    while (paint_len(r, i) < t) {
    // while (paint_len(r, i) < logt) {
        ++i;
    }
    if (paint_len(r, i) == t) {
    // if (paint_len(r, i) < logt + 1e-5) {
        return i;
    } 
    return i - 1;
}

void convertToINTVec(string line, INTVec &res) {
    char *list =  strdup(line.c_str());
    char* next = strtok(list, " ");
    while (next) {
        res.push_back(atol(next));
        next = strtok(NULL, " ");
    }
    free(list);
}

int main(int argc, char *argv[]) {
    // ifstream inFile("tiny.in");
    ifstream inFile("A-small-attempt0.in");
    // ifstream inFile("B-small-attempt1.in");
    // ofstream outFile("B-small-attempt0.out");
    // ofstream outFile("B-small-attempt1_comp.out");
    // ifstream inFile("A-small-attempt0.in");
    ofstream outFile("A-small-attempt0.out");
    // ifstream inFile("A-large.in");
    // ofstream outFile("A-large.out");
    istream &in = inFile;
    ostream &out = outFile;
    // ostream &out = cout;

    string line;
    getline(in, line);
    INT T = atoi(line.c_str());

    for (INT i = 0; i < T; ++i) {
        INTVec para;
        getline(in, line);
        convertToINTVec(line, para);
        INT r = para[0];
        INT t = para[1];
        // cout<< "r =: " <<  r  << endl;
        // cout<< "t =: " <<  t  << endl;
        // cout << "N: " << lawnSize[0] << " M: " << lawnSize[1] << endl;
        
        INT N = cal_circle_num(r, t);
        out << "Case #" << i+1 << ": " << N << endl;
        // out << "Case #" << i+1 << ": " << checkStatus(bd) << endl;
        //
    }
    return 0;
}
