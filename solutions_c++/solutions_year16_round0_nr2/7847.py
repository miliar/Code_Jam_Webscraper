#include <iostream>
#include <string>
#include <unordered_set>
#include <queue>
using namespace std;

using UOSS = unordered_set<string>;
UOSS uset;
int ans = -1;

string change(string s) {
    for(int i = 0; i < s.length(); i++) 
        s[i] = s[i] == '+' ? '-' : '+';
    string ret;
    for(int i = s.length()-1; i >=0; i--)
        ret += s[i];
    return ret;
}



int bfs(string& s, string& t) {
    queue<pair<string,int>> q;
    q.push({s,0});
    uset.insert(s);
    while(!q.empty()) {
        pair<string,int> now = q.front();
        q.pop();
        if(now.first == t) {
            return now.second;
        }
        int l = now.first.length();
        for(int i = 1; i <= l; i++) {
            string tmp = change(now.first.substr(0,i)) + now.first.substr(i, l);
            if(uset.find(tmp) == uset.end()) {
                uset.insert(tmp);
                q.push({tmp, now.second+1});
            }
        }
    }
    return -1;
}


int main() {
    int T, cas = 1;
    cin >> T;
    string S;

    while(T--) {
        cin >> S;
        uset.clear();
        string target = string(S.length(), '+');
        cout << "Case #" << cas++ << ": " << bfs(S,target)<< endl;
    }
    return 0;
}
