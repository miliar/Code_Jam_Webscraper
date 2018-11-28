#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <string>

#define LARGE

using namespace std;


int process(string s) {
    int numOfBuckets = 0;
    int last = s[0];
    for (int i = 0; i < s.size(); i++) {
        if (s[i] != last) {
            last = s[i];
            numOfBuckets ++;
        }
    }
    if (s[s.size() - 1] == '+') {
        numOfBuckets --;
    }
    return numOfBuckets + 1;
}




int main() {
#ifdef SMALL
    freopen("B-small-practice.in", "rt", stdin);
    freopen("B-small-practice.out", "wt", stdout);
#endif
#ifdef LARGE
    freopen("B-large-practice.in", "rt", stdin);
    freopen("B-large-practice.out", "wt", stdout);
#endif
    
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string S;
        cin >> S;
        int n = process(S);
        cout << "Case #" << i + 1 << ": " << n << endl;
    }
}