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
    int nb_cases = 0;
    ifs >> nb_cases;
    for (int i = 1; i <= nb_cases; ++i) {
        int max_shyness = 0;
        ifs >> max_shyness;
        vector<int> count(max_shyness + 1);
        string s;
        ifs >> s;
        for (int j = 0; j <= max_shyness; ++j)
            count[j] = s[j] - '0';
        int ret = 0;
        int nb_standing = 0;
        int cur = 0;
        while (cur <= max_shyness) {
            while (cur <= max_shyness && cur <= nb_standing)
                nb_standing += count[cur++];
            while (cur <= max_shyness && !count[cur])
                ++cur;
            if (cur > max_shyness) break;
            ret += cur - nb_standing;
            nb_standing = cur;
        }
        ofs << "Case #" << i << ": " << ret << endl;
    }
    ifs.close();
    ofs.close();
    return EXIT_SUCCESS;
}



