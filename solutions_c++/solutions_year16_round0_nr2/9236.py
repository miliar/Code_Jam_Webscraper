#include <ctime>
#include <cstdlib>
#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
//Containers
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

using namespace std;


int RevengeOfThePancakes (string s) {
    int len = (int)s.size();
    int cnt = 0;
    bool flag = (s[0] == '+') ? true : false;

    for(int j = 0; j < len; ++j) {
        if(flag == true && s[j] == '-') {
            flag = false;
        }
        else if(flag == false && s[j] == '+') {
            flag = true;
            cnt += 2;
        }
    }
    if(s[0] == '-') cnt--;
    if(s[len - 1] == '-') cnt += 2;
    return cnt;
}

int main (int argc, const char * argv[])
{
    //    Solution sol;
    ifstream in("/Users/Xiangyu/Desktop/B-large.in");
    ofstream out("/Users/Xiangyu/Desktop/output.txt");
    if (!in.is_open() || !out.is_open()) {
        cout << "Error opening file" << endl;
        exit (1);
    }
    int i = 0;
    string line;
    while(in >> line) {
        if(0 != i)
        {
            out << "Case #" << i << ": " << RevengeOfThePancakes(line) <<endl;
        }
        ++i;
    }
    in.close();
    out.close();
    return 0;
}