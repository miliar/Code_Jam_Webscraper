#include <iostream>
#include <fstream>

using namespace std;

char swp(char c) {
    if(c == '+') {
        return '-';
    }
    return '+';
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("outputlarge.out");

    int T;
    fin >> T;
    for(int c = 0; c < T; c++) {
        string s;
        int K;
        fin >> s >> K;
        int ops = 0;
        for(int i = 0; i < s.length(); i++) {
            if(s[i] == '-') {
                if(i+K > s.length()) {
                    fout << "Case #" << c+1 << ": " << "IMPOSSIBLE" << '\n';
                    break;
                } else {
                    for(int j = 0; j < K; j++) {
                        s[i+j] = swp(s[i+j]);
                    }
                    ops++;
                }
            } else if (i == s.length()-1) {
                fout << "Case #" << c+1 << ": " << ops << '\n';
            }
        }


    }

}
