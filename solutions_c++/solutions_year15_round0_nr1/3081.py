#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <cassert>
#include <cstring>
#include <cmath>
#include <fstream>
#include <algorithm>
using namespace std;

int main()
{
    int t;
    char s[1005];
    ifstream fp ("/Users/aviral.gupta/Downloads/in.txt");
    ofstream ofp ("/Users/aviral.gupta/Downloads/out.txt");
    fp >> t;
    for(int k = 1;k <= t; k++) {
        int sum = 0, res = 0, len;
        fp >> len >> s;
        len++;
        for (int i = 0; i < len; i++) {
            if (sum < i)
                res += i - sum, sum = i;
            sum += s[i] - '0';
        }
        ofp << "Case #" << k << ": " << res << endl;
    }
    fp.close();
    ofp.close();
    return 0;
}
