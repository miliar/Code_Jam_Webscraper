/*
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int minFriends(string &s) {
    int standNum = s[0] - '0';
    int ret = 0;
    for (int i = 1; i < s.size(); ++i) {
        int d = s[i] - '0';
        if (standNum < i) {
            ret += i - standNum;
            standNum += i - standNum;
        }
        standNum += d;
    }
    return ret;
}

int main(int argc, char *argv[])
{
    int T, smax;
    string str;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cin >> smax >> str; 
        cout << "Case #" << i + 1 << ": " << minFriends(str) << endl;
    }
    return 0;
}
