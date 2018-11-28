#include <bits/stdc++.h>

using namespace std;
int t, n, r, p, s;

vector<char> prevs, nexts;

string getStr(int begin, int end) {
    string tmp = "";
    for (int i = begin; i < end; i++) {
        // assert(i < prevs.size() && i >= 0);
        tmp += prevs[i];
    }
    return tmp;
}

void alphebetize(int start, int end) {
    int mid = (start + end) / 2;
    if (end - start != 2) {
        alphebetize(start, mid);
        alphebetize(mid, end);
    }
    // cout << start << " " << end << " " << mid << endl;
    // string s1 = getStr(start, mid), s2 = getStr(mid, end);
    string s1(prevs.data() + start, mid - start), s2(prevs.data() + mid, end - mid);
    assert(s1.size() == s2.size() && s1.size() + s2.size() == end - start);
    if (s2 < s1) {
        for (int i = start; i < mid; i++) {
            char tmp = prevs[i];
            prevs[i] = prevs[i + mid - start];
            // cout << (i + mid - start) << " " << i << " " << mid << " " << start << endl;
            // assert(i + mid - start < prevs.size() && i + mid - start >= 0);
            prevs[i + mid - start] = tmp;
        }
    }
}

bool works() {
    for (int i = 0; i < n; i++) {
        nexts.clear();
        nexts.reserve(prevs.size() * 2);
        for (int j = 0; j < prevs.size(); j++) {
            switch (prevs[j]) {
                case 'R':
                    nexts.push_back('R'); nexts.push_back('S'); break;
                case 'P':
                    nexts.push_back('P'); nexts.push_back('R'); break;
                case 'S':
                    nexts.push_back('P'); nexts.push_back('S'); break;
                default:
                    assert(false);
            }
        }
        prevs = nexts;
    }
    assert(prevs.size() == (r + p + s));
    int rCount = 0, pCount = 0, sCount = 0;
    for (int i = 0; i < prevs.size(); i++) {
            switch (prevs[i]) {
                case 'R':
                    rCount++; break;
                case 'P':
                    pCount++; break;
                case 'S':
                    sCount++; break;
                default:
                    assert(false);
            }
    }
        // cout << string(prevs.begin(), prevs.end()) << " " << rCount << " " << pCount << " " << sCount << " " << r << " " << p << " " << s <<endl;

    alphebetize(0, prevs.size());
    return rCount == r && pCount == p && sCount == s;
}

int main() {
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> n >> r >> p >> s;
        string best = "";
        prevs = {'P'};
        if (works()) {
            best = getStr(0, prevs.size());
        }
        prevs = {'R'};
        if (works()) {
            string tmp = getStr(0, prevs.size());
            if (best == "" || tmp < best) {
                best = tmp;
            }
        }
        prevs = {'S'};
        if (works()) {
            string tmp = getStr(0, prevs.size());
            if (best == "" || tmp < best) {
                best = tmp;
            }
        }
        if (best == "") {
            cout << "Case #" << test << ": IMPOSSIBLE" << endl; 
        } else {
            cout << "Case #" << test << ": " << best << endl;
        }
    }
}