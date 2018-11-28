#include <iostream>
#include <cstring>
#include <vector>
// #include <algorithm>
#include <cassert>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <set>

using namespace std;

// typedef unsigned long long INT;
typedef long long INT;
typedef vector<INT> IntVec;
typedef vector<IntVec> Mat;

IntVec convertToIntVec(string line) {;
    IntVec res;
    char *list =  strdup(line.c_str());
    char* next = strtok(list, " ");
    while (next) {
        res.push_back(atol(next));
        next = strtok(NULL, " ");
    }
    free(list);
    return res;
}

string magicTric(const Mat &m1, int r1, const Mat &m2, int r2) {
    set<INT> s1(m1[r1-1].begin(), m1[r1-1].end());
    // set<INT> s2(m2[r2-1].begin(), m2[r2-1].end());
    vector<INT> us;
    for (auto v : m2[r2-1]) {
        if (s1.find(v) != s1.end()) {
            us.push_back(v);
        }
    }
    if (us.size() == 1) {
        return to_string(us[0]);
    } else if (us.size() == 0) {
        return "Volunteer cheated!";
    } else {
        return "Bad magician!";
    }
}


int main(int argc, char *argv[]) {
    // istream &in = cin;
    // ostream &out = cout;
    // in = &cin;
    // out = &cout;
    // ifstream inFile("tiny.in");
    ifstream inFile("./qualify/A-small-attempt0.in");
    // ifstream inFile("C-small-attempt0.in");
    // ifstream inFile("C-large-1.in");
    // ofstream outFile("result_large.txt");
    ofstream outFile("C-small-attempt0.out");
    // ofstream outFile("C-large-1.out");
    istream &in = inFile;
    ostream &out = outFile;
    // ostream &out = cout;

    string line;
    getline(in, line);
    int T = atoi(line.c_str());
    // cout << "T: " <<  T << endl;
    for (int i = 0; i < T; ++i) {
        getline(in, line);
        IntVec tmp = convertToIntVec(line);
        int r1 = tmp[0];
        Mat m1;
        for (int j = 0; j < 4; ++j) {
            getline(in, line);
            m1.push_back(convertToIntVec(line));
        }

        getline(in, line);
        tmp = convertToIntVec(line);
        int r2 = tmp[0];
        Mat m2;
        for (int j = 0; j < 4; ++j) {
            getline(in, line);
            m2.push_back(convertToIntVec(line));
        }

        string res = magicTric(m1, r1, m2, r2);
        out << "Case #" << i+1 << ": " << res << endl;
    }
    return 0;
}
