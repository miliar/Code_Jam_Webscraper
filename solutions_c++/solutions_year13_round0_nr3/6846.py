#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

bool isPalindrom(long long n) {
    string s;
    stringstream strstream;
    strstream << n;
    strstream >> s;
    for(int i=0; i<s.size()/2; ++i) {
        if(s[i] != s[s.size()-i-1]) return false;
    }
    return true;
}

bool isSquare(long long n) {
    long long sq = sqrt(n);
    if(sq*sq == n) {
        return isPalindrom(sq);
    }
    return false;
}

int main() {
    ifstream in("C-small-attempt0.in");
    ofstream out("asd.txt");
    int n;
    in>>n;
    vector<vector<long long> > k;
    int a1, a2;
    for(int i=0; i< n ;++i) {
        in>>a1>>a2;
        vector<long long> r;
        r.push_back(a1);
        r.push_back(a2);
        k.push_back(r);
    }
    for(int i=0;i<k.size();++i) {
        int f=0;
        for(int j=k[i][0]; j<=k[i][1]; ++j) {
            if(isSquare(j) && isPalindrom(j)) {
                f++;
            }
        }
        out<<"Case #"<<(i+1)<<": "<<f<<endl;
    }
    return 0;
}
