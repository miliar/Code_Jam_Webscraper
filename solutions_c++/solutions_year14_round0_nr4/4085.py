#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int deceit(vector<double> srcMe, vector<double> srcOther) {
    vector<double> me(srcMe);
    vector<double> other(srcOther);
    int points = 0;
    while (other.size()) {
        if (me.back() > other.back()) {
            points++;
            me.erase(--me.end());
            other.erase(--other.end());
        } else {
            me.erase(me.begin());
            other.erase(--other.end());
        }
    }
//    while (me.size()) {
//        if (me.front() > other.front()) {
//            me.erase(me.begin());
//            other.erase(other.begin());
//            points++;
//            continue;
//        }
//        if (me.back() > other.back()) {
//            points ++;
//            me.erase(--me.end());
//            other.erase(other.begin());
//            continue;
//        }
//        if (me.back() < other.back()) {
//            me.erase(me.begin());
//            other.erase(--other.end());
//            continue;
//        }
//        if (me.front() < other.front()) {
//            me.erase(me.begin());
//            other.erase(other.begin());
//            continue;
//        }
//    }
    return points;
}

int normalWar(vector<double> srcMe, vector<double> srcOther) {
    vector<double> me(srcMe);
    vector<double> other(srcOther);
    int points = 0;
    while (me.size()) {
        double myWeight = me[0];
        me.erase(me.begin());
        bool isErased = false;
        for (auto it = other.begin(); it != other.end(); ++ it) {
            if (*it > myWeight) {
                other.erase(it);
                isErased = true;
                break;
            }
        }
        if (!isErased) {
            points ++;
            other.erase(other.begin());
        }
    }
    return points;
}

int main() {
    int T;
    cin >> T;
    int testCase = 0;
    double tmp;
    while (testCase < T) {
        testCase++;
        cout << "Case #" << testCase << ": ";
        int N;
        cin >> N;
        vector<double> srcMe;
        vector<double> srcOther;
        for (int i = 0; i < N; ++ i) {
            cin >> tmp;
            srcMe.push_back(tmp);
        }
        for (int i = 0; i < N; ++ i) {
            cin >> tmp;
            srcOther.push_back(tmp);
        }
        sort(srcMe.begin(), srcMe.end());
        sort(srcOther.begin(), srcOther.end());
        cout << deceit(srcMe, srcOther) << ' ' << normalWar(srcMe, srcOther) << endl;
    /*for (auto it = srcMe.begin(); it != srcMe.end(); ++ it) {
        cout << *it << ' ';
    }
    cout << endl;
    for (auto it = srcOther.begin(); it != srcOther.end(); ++ it) {
        cout << *it << ' ';
    }
    cout << endl;*/
    }
}
