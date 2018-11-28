#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream inf("ovation.in");
    ofstream ouf("ovation.out");
    int T; inf >> T;
    for(int t = 0; t < T; ++t) {
        int n; inf >> n;
        int standing = 0;
        int answer = 0;
        for(int shy = 0; shy <= n; ++shy) {
            char c; inf >> c;
            int ppl = c - '0';
            if(standing < shy) {
                answer += shy - standing;
                standing = shy;
            }
            standing += ppl;
        }
        ouf << "Case #" << t + 1 << ": " << answer << endl;
    }
    return 0;
}