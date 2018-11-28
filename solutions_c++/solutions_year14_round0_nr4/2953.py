#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cassert>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <set>
#include <iomanip>

using namespace std;

vector<double> convertToVec(string line) {;
    vector<double> res;
    char *list =  strdup(line.c_str());
    char* next = strtok(list, " ");
    while (next) {
        res.push_back(atof(next));
        next = strtok(NULL, " ");
    }
    free(list);
    return res;
}


pair<int, int> war(vector<double> &B1, vector<double> &B2) {
    // for (auto v : B1) cout << v << " "; 
    // cout << endl; 
    sort(B2.begin(), B2.end());
    sort(B1.begin(), B1.end());
    vector<double>::iterator up = B2.begin()-1;
    int i = 0;
    for (; i < B1.size(); ++i) {
        up = upper_bound(up+1, B2.end(), B1[i]);
        if (up == B2.end()) break;
    }
    int warRes = B1.size() - i;

    i = 0;
    auto up2 = B2.rbegin() - 1;
    for (; i < B1.size(); ++i) {
        // up2 = upper_bound(up2 + 1, B2.rend(), B1[i]);
        // if (up2 == B2.rend()) break;
        bool flag = true;
        for (int j = i; j < B1.size(); ++j) {
            if (B1[j] < B2[j-i]) {
                flag = false;
                break;
            }
        }
        if (flag) break;
    }
    int deceitWarRes = B2.size() - i;
    return make_pair(deceitWarRes, warRes);
}

int main(int argc, char *argv[]) {
    // istream &in = cin;
    // ostream &out = cout;
    // in = &cin;
    // out = &cout;
    // ifstream inFile("tiny.in");
    // ifstream inFile("D-small-attempt0.in");
    // ofstream outFile("D-small-attempt0.out");
    // ifstream inFile("B-small-attempt0.in");
    // ofstream outFile("B-small-attempt0.out");
    // ifstream inFile("C-small-attempt0.in");
    // ifstream inFile("C-large-1.in");
    // ofstream outFile("result_large.txt");
    // ofstream outFile("C-large-1.out");
    ifstream inFile("D-large.in");
    ofstream outFile("D-large.out");
    istream &in = inFile;
    ostream &out = outFile;
    // ostream &out = cout;

    string line;
    getline(in, line);
    int T = atoi(line.c_str());
    // cout << "T: " <<  T << endl;
    for (int i = 0; i < T; ++i) {
        getline(in, line);
        auto tmp = convertToVec(line);
        getline(in, line);
        auto B1 = convertToVec(line);
        getline(in, line);
        auto B2 = convertToVec(line);
        auto res = war(B1, B2);
        out << "Case #" << i+1 << ": " << res.first << " " << res.second << endl;

        // out.setf(ios::fixed,ios::floatfield);
        // out.precision(7);
    }
    return 0;
}
