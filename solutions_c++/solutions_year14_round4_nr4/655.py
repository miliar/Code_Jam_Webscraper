#define OSW2
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <utility>
using namespace std;


typedef long long ll;

int n,m;
int maxx = 0;
int a,b;
vector<set<string>> allc;
vector<string> v;
void dfs(int cnt) {
    if (cnt==m) {
        //cout << "ads" << endl;
        for (auto& s:allc) {
            for (auto& str:s) {
                a=rand(); b=rand();
            }
        }
        return;
    }
    int sz = 0;
    for (int i=0; i!=n; ++i) {
        if (!allc[i].empty()) ++sz;
        else break;
    }
    sz = min(sz, n);
    for (int i=0; i!=sz; ++i) {
        allc[i].insert(v[cnt]);
        dfs(cnt+1);
        allc[i].erase(v[cnt]);
    }
}

int main() {
    #ifdef OSW
    freopen("C:\\Users\\Administrator\\Desktop\\in.txt", "r", stdin);
    #endif // OSW
    #ifdef OSW2
    string file_name = "D-small-attempt0";
    string file_in = file_name+".in";
    string file_out = file_name+".out";
    freopen(file_in.c_str(), "r", stdin);
    freopen(file_out.c_str(), "w", stdout);
    #endif // OSW
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    int t=0;
    while (T-(t++)) {
        cout << "Case #" << t << ": ";
        cin >> m >> n;
        v.clear();
        for (int i=0; i!=m; ++i) {
            v.push_back("");
            cin >> v[i];
        }
        allc = vector<set<string>> (4);
        a=0; b=0;
        dfs(0);
        cout << a << ' ' << b << endl;

    }
}


