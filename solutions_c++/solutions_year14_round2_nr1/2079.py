#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

int main()
{
    int tests, n;
    cin >> tests;
    int test = 1;
    while(tests--) {
        bool poss = true;
        cin >> n;
        if(n == 1) {
            cout << "Case #" << test << ": 0" << endl;
            test++;
            continue;
        }
        vector<char> chars;
        vector<vector<int>> sizes;
        for(int i = 0; i < n; ++i) {
            string s;
            cin >> s;
            if(i == 0) {
                for(int j = 0; j < s.length(); ++j) {
                    if(j > 0 && s[j] != s[j - 1]) {
                        chars.push_back(s[j]);
                    } else if(j == 0) {
                        chars.push_back(s[j]);
                    }
                }
                int cnt = 0;
                vector<int> ss;
                for(int j = 0; j < s.length(); ++j) {
                    cnt++;
                    if(j > 0 && s[j] != s[j - 1]) {
                        ss.push_back(cnt);
                        cnt = 0;
                    }
                }
                ss.push_back(cnt);
                sizes.push_back(ss);
            } else {
                vector<char> nchars;
                for(int j = 0; j < s.length(); ++j) {
                    if(j > 0 && s[j] != s[j - 1]) {
                        nchars.push_back(s[j]);
                    } else if(j == 0) {
                        nchars.push_back(s[j]);
                    }
                }
                int cnt = 0;
                vector<int> ss;
                for(int j = 0; j < s.length(); ++j) {
                    cnt++;
                    if(j > 0 && s[j] != s[j - 1]) {
                        ss.push_back(cnt);
                        cnt = 0;
                    }
                }
                ss.push_back(cnt);
                sizes.push_back(ss);
                if(chars.size() != nchars.size()) {
                    poss = false;
                    break;
                } else {
                    for(int j = 0; j < chars.size(); ++j) {
                        if(chars[j] != nchars[j]) {
                            poss = false;
                            break;
                        }
                    }
                    if(!poss) break;
                }
            }
        }
        if(!poss) {
            cout << "Case #" << test << ": Fegla Won" << endl;
            test++;
            continue;
        }
        int moves = 0;
        for(int i = 0; i < chars.size(); ++i) {
            int avg = 0;
            for(int j = 0; j < sizes.size(); ++j) {
                avg += sizes[j][i];
            }
            avg = int((avg / sizes.size()) + 0.5);
            for(int j = 0; j < sizes.size(); ++j) {
                moves += abs(avg - sizes[j][i]);
            }
        }
        cout << "Case #" << test << ": " << moves << endl;
        test++;
    }
    return 0;
}

