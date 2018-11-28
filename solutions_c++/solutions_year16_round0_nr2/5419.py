#include <bits/stdc++.h>

using namespace std;

string flip(int i, int j, string s) {
    string out(s);
    for(int k = i, l = j; k <= j; k ++, l --){
        out[k] = (s[l] == '+') ? '-' : '+';
    }
    return out;
}

int main() {
    ifstream fileIn;
    ofstream fileOut;
    fileIn.open("B-large.in");
    fileOut.open("out.txt");
    int T;
    fileIn >> T;
    for(int p = 1; p <= T; p ++) {
        string s;
        fileIn >> s;
        int i, j, len = s.length(), count = 0;
        i = len - 1;
        while(i >= 0){
            if(s[i] == '-') {
                j = 0;
                while(s[j] != '-')
                    j ++;
                if(j > 0){
                    s = flip(0, j - 1, s);
                    count ++;
                }
                s = flip(0, i, s);
                count ++;
            }
            i --;
        }
        fileOut << "Case #" << p << ": " << count << "\n";
    }
    return 0;
}
