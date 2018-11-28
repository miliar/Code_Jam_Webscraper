#include <fstream>
#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int main(){
    ifstream fin("in1");
    ofstream fout("out1");
    int T;
    string S;

    fin >> T;
    for (int i = 1; i <= T; i++){
        fin >> S;
        string s;
        for (int j = 0; j < S.length(); j++){
            bool inc = false;
            if (s.empty())
                s.push_back(S[j]);
            else if (S[j] > s[0])
                s.insert(0, 1, S[j]);
            else if (S[j] == s[0])
                s.insert(0, 1, S[j]);
            else
                s.push_back(S[j]);
        }
        fout << "Case #" << i << ": " << s << endl;
    }

    fin.close();
    fout.close();
}
