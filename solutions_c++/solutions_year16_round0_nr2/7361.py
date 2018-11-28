#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <set>
#include <cstring>
#include <memory>
#include <vector>
#include <cassert>

using namespace std;

int used[10];
int currently;

void update(int x, int mark)
{
    while (x > 0) {
        int c = x % 10;
        if (used[c] != mark) {
            currently++;
        }
        used[c] = mark;
        x /= 10;
    }
}

int main(int argc, char* argv[])
{
    ifstream in;
    in.open("input.txt");
    ofstream out;
    out.open("output.txt");
    
    ios_base::sync_with_stdio(false);
    
    int tests;
    in >> tests;
    for (int t = 1; t <= tests; t++) {
        out << "Case #" << t << ": ";
    
        string s;
        in >> s;
        int i = static_cast<int>(s.length()) - 1;
        while (i >= 0 && s[i] == '+') {
            i--;
        }
        if (i < 0) {
            out << 0 << "\n";
            continue;
        }
        int cnt = 1;
        for (; i > 0; i--) {
            cnt += s[i - 1] != s[i];
        }
        out << cnt << "\n";
    }
    
    in.close();
    out.close();
}

