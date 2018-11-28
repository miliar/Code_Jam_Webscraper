#include <iostream>
#include <map>
#include <string>
#include <algorithm>
#include <queue>
#include <set>

using namespace std;

map<string,int> ans;

string flip(string ss,int x)
{
    string stmp = ss;
    reverse(stmp.begin(),stmp.begin()+x);
    for(int i=0;i<x;++i)
        stmp[i] = (stmp[i]=='-' ? '+' : '-');
    // cout << "stmp " << stmp << endl;
    return stmp;
}

void solve(int len)
{
    ans.clear();
    vector<string> vec;
    vec.push_back(string("-"));
    vec.push_back(string("+"));
    for(int i=1;i<len;++i) {
        vector<string> v2 = vec;
        vec.clear();
        int ed = v2.size();
        for(int j=0;j<ed;++j) {
            vec.push_back(v2[j]+"-");
            vec.push_back(v2[j]+"+");
        }
    }
    for(int i=0;i<(int)vec.size();++i)
        ans[vec[i]] = 999;
    ans[vec.back()] = 0;
    queue<string> q;
    q.push(vec.back());
    set<string> sets;
    while(!q.empty()) {
        string now = q.front(); q.pop();
        // cout << now << "NOW" << endl;
        sets.erase(now);
        for(int i=1;i<=len;++i) {
            string s2 = flip(now,i);
            if(ans[now]+1<ans[s2]) {
                ans[s2] = ans[now]+1;
                if(sets.count(s2)==0) {
                    sets.insert(s2);
                    q.push(s2);
                }
            }
        }
    }
}

int getans(string ss)
{
    int len = ss.size();
    int ans = 0;
    for(int i=0;i<len-1;++i)
        if(ss[i]=='+' && ss[i+1]=='-')
            ans += 2;
    if(ss[0]=='-') ++ans;
    return ans;
}

// int main(void)
// {
//     for(int len=20;len<21;++len) {
//         solve(len);
//         vector<string> vec;
//         vec.push_back(string("-"));
//         vec.push_back(string("+"));
//         for(int i=1;i<len;++i) {
//             vector<string> v2 = vec;
//             vec.clear();
//             int ed = v2.size();
//             for(int j=0;j<ed;++j) {
//                 vec.push_back(v2[j]+"-");
//                 vec.push_back(v2[j]+"+");
//             }
//         }
//         for(int i=0;i<(int)vec.size();++i) {
//             if(getans(vec[i])!=ans[vec[i]]) {
//                 cout << vec[i] << endl;
//                 cout << getans(vec[i]) << ' ' << ans[vec[i]] << endl;
//             }
//         }
//     }
//     return 0;
// }

int main(void)
{
    int T; cin >> T;
    for(int t=1;t<=T;++t) {
        cout << "Case #" << t << ": ";
        string ss; cin >> ss;
        // solve(ss.size());
        cout << getans(ss) << endl;
        // cout << ans[ss] << endl;
    }
    return 0;
}
