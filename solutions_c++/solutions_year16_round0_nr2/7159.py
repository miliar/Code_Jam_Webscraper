#include <array>
#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

int solve(const string l) {
    vector<bool> pq;
    for(auto& q: l){
        pq.push_back(q == '+' ? true : false);
    }

    bool curr = pq[0];
    int count = 0;
    for(auto q: pq) {
        if (q != curr) {
            count++;
            curr = q;
        }
    }

    if (!curr) {
        count++;
    }

    return count;
}

int main(){
    ifstream inf("B-large.in");
    ofstream ouf("2.out");
    int T;
    inf >> T;
    for(int i = 0; i < T; ++i) {
        string l;
        inf >> l;
        ouf << "Case #" << i + 1 << ": " << solve(l) << endl;
    }
    ouf.close();
    inf.close();
}
