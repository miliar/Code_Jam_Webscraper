#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

using namespace std;

vector<int> prime = {2, 3, 5, 7, 11, 13};

int solve(priority_queue<int> p, int depth) {
    if (depth > 1000) {
        cout << "ERROR:" << endl;
        exit(0);
    }
    int top = p.top();
    if (top <= 3) {
        return top;
    }
    p.pop();


    int min = top;
    for (int i: prime) {
        if (i > top) {
            continue;
        }

        priority_queue<int> pp(p);
        int tt = top;
        int part = (top + (top % i ? i : 0)) / i;
        for (int j = 0; j < i-1; ++j) {
            pp.push(part);
            tt -= part;
        }
        pp.push(tt);

        int ret = solve(pp, depth + 1) + i - 1;
        //cout << "ret: " << ret << "i: " << i << "top: " << top << "part: " << part << endl;

        //cout << "pp: " ;
        //for (int j = 0; j < pp.size(); ++j) {
        //    cout << pp.top() << ", ";
        //    pp.pop();
        //}
        //cout << endl;

        if (ret < min) {
            min = ret;
        }
    }

    return min;
}

int main() {
    ifstream ifs("small");
    int t;
    ifs >> t;

    for (int tt = 0; tt < t; ++tt) {
        int d;
        priority_queue<int> p;
        ifs >> d;
        for (int i = 0; i < d; ++i) {
            int tmp;
            ifs >> tmp;
            p.push(tmp);
            //cout << tmp << " ";
        }
        //cout << endl;
        cout << "Case #" << tt + 1 << ": " << solve(p, 1) << endl;
    }
}
