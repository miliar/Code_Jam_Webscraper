#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

vector<string> s;
vector<int> sentence[25];
const int INF = 1e9;

int N;
string temp;

void reset() {
    s.clear();
    for(int i = 0; i < 25; i++) {
        sentence[i].clear();
    }
}

bool french[100005];
bool english[100005];

int test(int b) {
    for(int i = 0; i < s.size(); i++) {
        french[i] = false;
        english[i] = false;
    }
    for(int i = 0; i < sentence[0].size(); i++) {
        english[sentence[0][i]] = true;
    }
    for(int i = 0; i < sentence[1].size(); i++) {
        french[sentence[1][i]] = true;
    }
    for(int i = 2; i < N; i++) {
        if(b & (1<<i)) {
            for(int j = 0; j < sentence[i].size(); j++) {
                english[sentence[i][j]] = true;
            }
        } else {
            for(int j = 0; j < sentence[i].size(); j++) {
                french[sentence[i][j]] = true;
            }
        }
    }
    int ans =0;
    for(int i = 0; i < s.size(); i++) {
        if(french[i] && english[i]) {
            ans++;
        }
    }
    return ans;
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> N;
        getline(cin, temp);
        for(int i = 0; i < N; i++) {
            //cerr << i << "\n";
            getline(cin, temp);
            //cerr << temp << "\n";
            stringstream ss;
            ss << temp;
            while(ss >> temp) {
                bool found = false;
                for(int j = 0; j < s.size(); j++) {
                    if(temp == s[j]) {
                        sentence[i].push_back(j);
                        //cerr << "old word " << temp << " id " << j << "\n";
                        found = true;
                        break;
                    }
                }
                if(!found) {
                    s.push_back(temp);
                    sentence[i].push_back(s.size()-1);
                    //cerr << "New word " << temp << " " << s.size()-1 << "\n";
                }
            }
        }

        int best = INF;
        for(int b = 0; b < (1<<N); b++) {
            best = min(best, test(b));
        }
        cout << "Case #" << t << ": " << best << "\n";
        reset();
    }
}
