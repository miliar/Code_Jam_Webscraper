#include <vector>
#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
void dfs(vector<string>& p, vector<int>& v, 
        const int n, int& ans, const vector<int>& left) {
    string test;
    for (int i=0;i<v.size();++i) {
        test+=p[v[i]];
    }
    char ch=0;
    vector<int> check(26,0);
    int m=test.length()-1;
    for (int i=0;i<m;++i) {
        check[test[i]-'a']++;
        if (test[i]!=test[i+1] 
            && left[test[i]-'a']!=check[test[i]-'a']) {
            return;
        }
    }
    
    if (v.size()==n) {
        ans++;
        return;
    }

    vector<bool> cand(n,true);

    for (int i=0;i<v.size();++i) {
        cand[v[i]]=false;
    }
    for (int i=0;i<n;++i) {
        if (!cand[i]) continue;
        v.push_back(i);
        dfs(p,v,n,ans,left);
        v.pop_back();
    }
    return;
}
int solve(vector<string>& p, const int n) {
    int ans=0;
    vector<int> v;
    vector<int> left(26,0);
    for (int i=0;i<n;++i) {
        string s=p[i];
        for (int j=0;j<s.length();++j) {
            left[s[j]-'a']++;
        }
    }
    dfs(p,v,n,ans, left);
    return ans;
}
int main(int argc, char* argv[]) {
    int T;
    cin>>T;
    for (int t=1;t<=T;++t) {
        cout<<"Case #"<<t<<": ";
        int n;
        cin>>n;
        vector<string> p;
        for (int i=0;i<n;++i) {
            string s;
            cin>>s;
            p.push_back(s);
        }
        int ans=solve(p,n);
        cout<<ans<<endl;
    }
    return 0;
}
