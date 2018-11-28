#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

int main() {
    
    cin.tie(0);
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    
    int TC, lines;
    string line, aux;
    cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {
        
        int extra = 0;
        
        set<string> english;
        set<string> french;
        vector< set<string> > unknown;
        cin >> lines;
        getline(cin, line);
        for (int i = 0; i < lines; i++) {
            getline(cin, line);
            stringstream ss(line);
            set<string> sentence;
            while (ss >> aux) {
                sentence.insert(aux);
            }
            if (i == 0) english.insert(sentence.begin(), sentence.end());
            else if (i == 1) french.insert(sentence.begin(), sentence.end());
            else unknown.push_back(sentence);
        }
        
        for (set<string>::iterator it = english.begin(); it != english.end();) {
            if (french.count(*it)) {
                extra++;
                french.erase(french.find(*it));
                english.erase(it++);
            } else {
                ++it;
            }
        }
        
        
        int minimum = 1000000000;
        for (int mask = 0; mask < (1<<unknown.size()); mask++) {
            set<string> en = english;
            set<string> fr = french;
            
            int i = 0;
            for (vector< set<string> >::iterator sentenceIt = unknown.begin(); sentenceIt != unknown.end(); sentenceIt++) {
                if (mask & 1<<i) en.insert(sentenceIt->begin(), sentenceIt->end());
                else fr.insert(sentenceIt->begin(), sentenceIt->end());
                i++;
            }
            
            int ans = 0;
            for (set<string>::iterator it = en.begin(); it != en.end(); it++) {
                if (fr.count(*it)) {
                    ans++;
                }
            }
            minimum = min(minimum, ans);
            
        }
        
        cout << "Case #" << tc << ": " << minimum+extra << endl;
        
        
        /*int prevSize = unknown.size();
        for (int i = 0; i < unknown.size() + 10; i++) {
            for (set< set<string> >::iterator sentenceIt = unknown.begin(); sentenceIt != unknown.end(); sentenceIt++) {
                bool isEnglish = false;
                bool isFrench = false;
                for (set<string>::iterator it = sentenceIt->begin(); it != sentenceIt->end(); it++) {
                    if (english.count(*it)) isEnglish = true;
                    if (french.count(*it)) isFrench = true;
                }
                if (isEnglish) english.insert(sentenceIt->begin(), sentenceIt->end());
                if (isFrench) french.insert(sentenceIt->begin(), sentenceIt->end());
            }
        }
        
        
        int ans = 0;
        //
        for (set<string>::iterator it = english.begin(); it != english.end(); it++) {
            if (french.count(*it)) {
                ans++;
                cout << *it << " ";
            }
        }
        cout << endl;
        cout << "Case #" << tc << ": " << ans << endl;*/
    }

    return 0;
}
