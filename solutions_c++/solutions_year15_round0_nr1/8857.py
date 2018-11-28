#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <fstream>

#define LPI(start,stop) for(int i=(start);i<(stop);i++)
#define LPI0(stop) for(int i=0;i<(stop);i++)
#define LP(i,start,stop) for((i)=(start);(i)<(stop);(i)++)
#define LP0(i,stop) for((i)=0;(i)<(stop);(i)++)

using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");


void test() {
    int sm;
    char c;
    vector<int> s;

    fin >> sm;
    LPI0(sm+1) {
        fin >> c;
        s.push_back(c-'0');
    }

    int y = 0;
    int p = 0;

    LPI0(sm+1) {
        p += s[i];
        if (p < i+1) {
            y += i+1-p;
            p += i+1-p;
        }
    }

    fout << y;
}

int main() {
    int t;
    fin >> t;
    LPI0(t) {
        cout << "On #" << i+1 << " of " << t << endl;
        fout << "Case #" << i+1 << ": ";
        test();
        fout << endl;
    }

    cout << "Done\n";

    return 0;
}