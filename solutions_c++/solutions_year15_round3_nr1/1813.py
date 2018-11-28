#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <forward_list>
#include <array>
#include <iterator>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>
#include <stack>
#include <limits>

using namespace std;


int main(void) {
    ifstream ifs("/home/amor/Downloads/PI.txt");
    ofstream ofs("/home/amor/Downloads/PO.txt");
    int t;
    ifs >> t;
    for (int i = 1; i <= t; ++i) {
        int r, c, w;
        ifs >> r >> c >> w;
        int ret = 0;
        while (2 * w - 2 < c - 1) {
            c -= w;
            ++ret;
        }
        if (c == w) ret += w;
        else ret += w + 1;
        ofs << "Case #" << i << ": " << r * ret << endl;
    }
    ifs.close();
    ofs.close();
    return EXIT_SUCCESS;
}



