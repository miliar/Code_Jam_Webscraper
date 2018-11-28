#include <iostream>
#include <string>
#include <math.h>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <map>
#include <limits>
#include <queue>
#include <stack>

using namespace std;


int main() {
    
    ifstream fin ("A-large.in");
    ofstream fout ("output.out");
    
    int tests;
    fin >> tests;
    for (int test = 0; test < tests; test++) {
        string s;
        fin >> s;
        long long alpha[26] = {0};
        for (int i = 0; i < s.length(); i++) {
            alpha[s[i]-'A']++;
        }
        long long res[10] = {0};
        res[0] = alpha['Z'-'A'];
        res[2] = alpha['W'-'A'];
        res[6] = alpha['X'-'A'];
        res[8] = alpha['G'-'A'];
        res[3] = alpha['H'-'A']-res[8];
        res[4] = alpha['U'-'A'];
        res[5] = alpha['F'-'A']-res[4];
        res[7] = alpha['V'-'A']-res[5];
        res[6] = alpha['S'-'A']-res[7];
        res[9] = alpha['I'-'A']-res[5]-res[6]-res[8];
        res[1] = alpha['O'-'A']-res[0]-res[2]-res[4];
        fout << "Case #" << test+1 << ": ";
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < res[i]; j++) {
                fout << i;
            }
        }
        fout << endl;
    }
    
    
    
}