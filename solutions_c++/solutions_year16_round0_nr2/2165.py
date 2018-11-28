#include<iostream>
#include<queue>
#include<set>
using namespace std;

bool check(string& s) {
    for(auto& c : s) if(c=='-') return false;
    return true;
}
string op(string s, int a) {
    int l = 0;
    int r = a-1;
    while(l<r) {
        swap(s[l],s[r]);
        l++;
        r--;
    }
    for(int i=0;i<a;i++) s[i] = s[i] == '+' ? '-' : '+';
    return s;
}

int c() {
    set<string> st;
    queue<pair<string,int> > q;
    string s;
    cin>>s;
    st.insert(s);
    q.push(make_pair(s,0));
    while(!q.empty()) {
        auto& p = q.front();
        string s = p.first;
        int move = p.second;
        q.pop();
        if(check(s)) return move;
        for(int i=1;i<=s.size();i++) {
            string new_s = op(s,i);
            if(st.count(new_s)) continue;
            st.insert(new_s);
            q.push(make_pair(new_s,move+1));
        }
    }
    
}

int main() {
    int t=0;
    cin>>t;
    for(int i=1;i<=t;i++) cout<<"Case #"<<i<<": "<<c()<<endl;
}
