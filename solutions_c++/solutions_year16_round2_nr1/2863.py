//from c
#include <ctime>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
//stream
#include <fstream>
#include <iostream>
#include <sstream>

//containers
#include <string>
#include <bitset>
#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

#include <algorithm>
#include <limits>
#include <climits>
#include <numeric>
using namespace std;

string find(string s) {
    string res;
    vector<int> m(128, 0);
    vector<int> num(10, 0);
    for (auto c : s)
        m[c] ++;
    
    num[0] = m['Z'];
    m['E'] -= m['Z'];
    m['R'] -= m['Z'];
    m['O'] -= m['Z'];
    m['Z'] = 0;
    
    num[6] = m['X'];
    m['S'] -= m['X'];
    m['I'] -= m['X'];
    m['X'] = 0;
    
    num[7] = m['S'];
    m['E'] -= 2 * m['S'];
    m['V'] -= m['S'];
    m['N'] -= m['S'];
    m['S'] = 0;
    
    num[5] = m['V'];
    m['F'] -= m['V'];
    m['I'] -= m['V'];
    m['E'] -= m['V'];
    m['V'] = 0;
    
    num[4] = m['F'];
    m['O'] -= m['F'];
    m['U'] -= m['F'];
    m['R'] -= m['F'];
    m['F'] = 0;
    
    num[3] = m['R'];
    m['T'] -= m['R'];
    m['H'] -= m['R'];
    m['E'] -= 2 * m['R'];
    m['R'] = 0;
    
    num[2] = m['W'];
    m['T'] -= m['W'];
    m['O'] -= m['W'];
    m['W'] = 0;
    
    num[1] = m['O'];
    m['N'] -= m['O'];
    m['E'] -= m['O'];
    m['O'] = 0;
    
    num[8] = m['T'];
    m['E'] -= m['T'];
    m['I'] -= m['T'];
    m['G'] -= m['T'];
    m['H'] -= m['T'];
    m['T'] = 0;
    
    num[9] = m['I'];
    for(int i = 0; i < num.size(); ++i) {
        while(num[i]) {
            res += to_string(i);
            num[i] --;
        }
    }
    return res;
}

int main (int argc, const char * argv[])
{
    //    Solution sol;
    ifstream in("/Users/Xiangyu/Desktop/A-small-attempt2.in");
    ofstream out("/Users/Xiangyu/Desktop/output.txt");
    if (!in.is_open() || !out.is_open()) {
        cout << "Error opening file" << endl;
        exit (1);
    }
    int i = 0;
    in >> i;
    
    string a;
    int index = 1;
    while (in >> a) {
        out << "Case #" << index << ": " << find(a) << endl;
        index++;
    }
    in.close();
    out.close();
    return 0;
}