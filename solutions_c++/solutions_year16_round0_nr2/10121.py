//
//  main.cpp
//  Pancakes
//
//  Created by Leo Lee on 4/9/16.
//  Copyright © 2016 Leo Lee. All rights reserved.
//

#include <iostream>
#include <queue>
#include <string>
#include <set>

using namespace std;

struct Step {
    Step(string as, int aswaps) :
    s(as),
    swaps(aswaps) { }
    
    string s;
    int swaps;
};

set<string> seen;

bool checkAllHappy(const string &s) {
    for (int i = 0; i < s.length(); ++i) {
        if (s[i] != '+') {
            return false;
        }
    }
    return true;
}

int numTrailingHappy(const string &s) {
    int len = (int)s.length();
    int cnt = 0;
    while (cnt < len && s[len - cnt - 1] == '+') {
        ++cnt;
    }
    return cnt;
}

string trimTrailingHappy(const string &s) {
    int th = numTrailingHappy(s);
    return s.substr(0, s.length() - th);
}

bool helper(Step &step, queue<Step> &q) {
    int curSwaps = step.swaps;
    
    int slen = (int)step.s.length();
    for (int i = 0; i < slen; ++i) {
        string s1 = step.s.substr(0, i + 1);
        string s2 = "";
        if (i < slen - 1) {
            s2 = step.s.substr(i + 1, slen - i);
        }
        reverse(s1.begin(), s1.end());
        for (int j = 0; j < s1.length(); ++j) {
            char c = s1[j];
            s1[j] = (c == '+') ? '-' : '+';
        }
        string flippedCombined = s1 + s2;
        if (seen.find(flippedCombined) == seen.end()) {
            if (i == slen - 1) {
                flippedCombined = trimTrailingHappy(flippedCombined);
                if (flippedCombined.length() == 0) {
                    return true;
                }
            }
            q.push(Step(flippedCombined, curSwaps + 1));
            seen.insert(flippedCombined);
        }
    }
    
    return false;
}

int countSteps(queue<Step> &q) {
    while (!q.empty()) {
        Step step = q.front();
        q.pop();
        
        if (helper(step, q)) {
            return step.swaps + 1;
        }
    }
    return 0;
}

int main(int argc, const char * argv[]) {
    uint numCases = 1;
    cin >> numCases;
    for (uint caseIndex = 0; caseIndex < numCases; ++caseIndex) {
        seen.clear();
        string s = "-----++---";
        cin >> s;
        Step step(trimTrailingHappy(s), 0);
        int steps;
        if (step.s.empty()) {
            steps = 0;
        } else {
            queue<Step> q;
            q.push(step);
            seen.insert(step.s);
            steps = countSteps(q);
        }
        cout << "Case #" << (caseIndex + 1) << ": " << steps << endl;
    }
    return 0;
}

