#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int tests;
    cin >> tests;
    int test = 1;
    while(tests--) {
        int n;
        cin >> n;
        vector<string> v;
        vector<int> helper;
        for(int i = 0; i < n; ++i) {
            string s;
            cin >> s;
            v.push_back(s);
            helper.push_back(i);
        }
/*
        bool imp = false;
        for(char c = 'a'; c <= 'z'; ++c) {
            bool inner = false;
            bool outer = false;
            bool onlyinner = false;
            for(string s : v) {
                bool thisinner = false;
                bool thisouter = false;
                int last = -1;
                int len = s.length();
                for(int i = 0; i < len; ++i) {
                    if(s[i] == c) {
                        if(last != -1) {
                            if((i - last) > 1) {
                                imp = true;
                                break;
                            }
                        }
                        if( (i != 0) && (i != (len - 1) )) {
                            thisinner = true;
                        }
                        if( (i == 0) || (i == (len - 1)) ) {
                            thisouter  = true;
                        }
                        last = i;
                    }
                }
                if( (thisinner && !thisouter && outer) || (thisouter && onlyinner) || imp) {
                    imp = true;
                    break;
                }
                if(thisouter) outer = true;
                if(!thisouter && thisinner) onlyinner = true;
            }
        }
        if(imp) {
            cout << "Case #" << test << ": 0" << endl;
            test++;
            continue;
        }*/

        int alp[26];
        int numOfPerms = 0;
        do {
            for(int i = 0; i < 26; ++i)
                alp[i] = -1;

            bool ok = true;
            int index = 0;
            for(int i = 0; i < n; ++i) {
                string s1 = v[helper[i]];
                int len = s1.length();
                for(int j = 0; j < len; ++j){
                    char c = s1[j];
                    int last = alp[c - 97];
                    if(last != -1 && ( (index - last) > 1 ) ){
                        ok = false;
                        break;
                    }
                    alp[c - 97] = index;
                    index++;
                }
                if(!ok) break;
            }

            if(ok) numOfPerms = (numOfPerms + 1) % 1000000007;

        } while(next_permutation(helper.begin(), helper.end()));
        cout << "Case #" << test << ": " << numOfPerms << endl;
        test++;
    }
    return 0;
}

