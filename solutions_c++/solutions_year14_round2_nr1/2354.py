
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
#include <climits>
#include <fcntl.h>
#include <unistd.h>
#include <fstream>

using namespace std;

typedef long long INT;
typedef vector<INT> INTVec;
typedef vector<INTVec> Mat;


vector<pair<char, int> > count(string A) {
    vector<pair<char, int> > nd;
    int j = 1;
    for (size_t i = 1; i <= A.size(); ++i) {
        if (i == A.size() || A[i] != A[i-1]) {
            nd.push_back(make_pair(A[i-1], j));
            j = 1;
        } else {
            ++j;
        }
    }
    return nd;
}

int minAction(string A, string B) {
    auto nd1 = count(A);
    auto nd2 = count(B);
    if (nd1.size() != nd2.size()) return 2000;
    int cnt = 0;
    for (size_t i = 0; i < nd1.size(); ++i) {
        if (nd1[i].first != nd2[i].first) return 2000;
        cnt += abs(nd1[i].second - nd2[i].second);
    }
    return cnt;
    // for (auto v : nd) {
    //     cout << v.first << " : " << v.second << endl;
    // }
}



int main(int argc, char *argv[]) {
    ifstream inFile("A-small-attempt2.in");
    // ifstream inFile("A.tiny");
    // ofstream outFile();
    // ofstream outFile("A-small-attempt0-1.out");
    istream &in = inFile;
    // ostream &out = outFile;
    // istream &in = cin;
    ostream &out = cout;
    int T;
    in >> T;
    for (int i = 0; i < T; ++i) {
        int N;
        in >> N;
        vector<string> S;
        string s;
        for (size_t j = 0; j < N; ++j) {
            in >> s;
            S.push_back(s);
        }
        // int res = minAction(S);
        // cout << "S[0]" << S[0];
        // map<Key, int> dp;
        // int res = minAction(S[0], 0, S[1], 0, '\0', dp);
        int res = minAction(S[0], S[1]);
        if (res < 1000) {
            out << "Case #" << i+1 << ": " <<  res << endl;
        } else {
            out << "Case #" << i+1 << ": " <<  "Fegla Won"<< endl;
        }
    }
    return 0;
}

