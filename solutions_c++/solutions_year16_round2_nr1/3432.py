#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<cstdlib>

typedef long long ll;
typedef unsigned long long ull;

using namespace std;
vector< vector<int> > c = {
    {4, 14, 17, 25},
    {4, 13, 14},
    {14, 19, 22},
    {4, 4, 7, 17, 19},
    {5, 14, 17, 20},
    {4, 5, 8, 21},
    {8, 18, 23}, 
    {4, 4, 13, 18, 21},
    {4, 6, 7, 8, 19},
    {4, 8, 13, 13}
};
map<pair<int, vector<int>>, string> m;

pair<bool, vector<int>> try_x(int x, vector<int> zv) {
    for (unsigned i = 0; i<c[x].size(); ++i) {
        if (zv[c[x][i]] == 0) return make_pair(false, zv);
        zv[c[x][i]]--; 
    }
    return make_pair(true, zv);
}

string rek(int co, vector<int> &zv) {
    auto it = m.find(make_pair(co, zv));
    if (it != m.end()) {
        return it->second;
    }
    string ret;
    if (co == 10) {
        bool zero = true;
        for (unsigned i = 0; i<zv.size(); ++i) {
            if (zv[i] != 0) {
                zero = false;
                break;
            }
        }
        if (zero) ret = "";
        else ret = "-1";
    } else {
        pair<bool, vector<int>> dasa = try_x(co, zv);
        string x = rek(co+1, zv);
        if (dasa.first) {
            string y = rek(co, dasa.second);
            string cislo = to_string(co);
            if (y != "-1") x = cislo + y;
        }
        ret = x;
    }
    m[make_pair(co, zv)] = ret;
    return ret;
}

int main() {
    int T;
    cin>>T;
    for (int t = 0; t<T; ++t) {
        if (t>0) m.clear();
        string s;
        cin>>s;
        int n = s.length();
        vector<int> v(26,0);
        for (int i = 0; i<n; ++i) {
            v[s[i]-'A']++;
        }
        cout<<"Case #"<<t+1<<": "<<rek(0,v)<<"\n";
    }
    return 0;
}
