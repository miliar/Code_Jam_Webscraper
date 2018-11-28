//
//  main.cpp
//  CodeJam-qr-01
//
//  Created by 张云尧 on 2017/4/8.
//  Copyright © 2017年 张云尧. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

int main(int argc, const char * argv[]) {
    ifstream in("A-large.in");
    ofstream out("A-large.out");
    int t;
    in >> t;
    for (int i = 0; i < t; ++i) {
        string str;
        int n;
        in >> str >> n;
        int res = 0;
        queue<int> que;
        for (int i = 0; i < str.size(); ++i) {
            while (!que.empty() && que.front() < i)
                que.pop();
            if ((que.size() % 2 == 1 && str[i] == '+') ||
                (que.size() % 2 == 0 && str[i] == '-')) {
                if (i + n - 1 >= str.size()) {
                    res = -1;
                    break;
                }
                ++res;
                que.push(i + n - 1);
            }
        }
        out << "Case #" << i + 1 << ": ";
        res == -1 ? out << "IMPOSSIBLE" << endl : out << res << endl;
    }
    return 0;
}
