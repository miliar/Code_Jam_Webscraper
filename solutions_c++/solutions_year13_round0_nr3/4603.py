#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;

inline bool ispal(int n)
{
    stringstream ss;
    string s;
    ss << n;
    ss >> s;
    int len = s.size();
    for (int i = 0; i < len / 2; ++i)
        if (s[i] != s[len-1-i]) return false;
    return true;
}

int main()
{
    ifstream fin("C-small-attempt0.in");
    ofstream fou("out");

    int t;
    fin >> t;
    for (int i = 0; i < t; ++i) {
        int a, b;
        fin >> a >> b;

        int l = ceil(sqrt((float)a));
        int h = floor(sqrt((float)b));

        int cnt = 0;
        for (int k = l; k <= h; ++k)
            if (ispal(k) && ispal(k * k)) ++cnt;

        fou << "Case #" << i + 1 << ": " << cnt << endl;

    }

    fin.close();
    fou.close();
    return 0;
}
