#include <cstdio>
#include <memory>
#include <string>
#include <utility>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

class Node{
    unique_ptr<Node> children[26];
public:
    Node(){}
    void insert(const string& str, unsigned i = 0){
        if(i < str.size()){
            unsigned pos = str[i] - 'A';
            if(!children[pos].get())
                children[pos].reset(new Node());
            children[pos]->insert(str, i + 1);
        }
    }
    int count(){
        int cc = 0;
        for(char c = 'A'; c <= 'Z'; c++)
            if(Node* n = children[c - 'A'].get())
                cc += n->count();
        return cc + 1;
    }
};

inline pair<int, int> merge(pair<int, int> a, pair<int, int> b) {
    if(a.first > b.first)
        return a;
    else if(a.first < b.first)
        return b;
    else
        return {a.first, a.second + b.second};
}

int eval(const vector<string>& vec){
    Node n;
    for(auto& s: vec) n.insert(s);
    return n.count();
}

pair<int, int> bf(int i, int n, vector<string>& vc, vector<vector<string>>& vec){
    if(i == n) {
        if(any_of(vec.begin(), vec.end(), mem_fn(&vector<string>::empty))) return {0,0};
        int cnt = 0;
        for(auto& v: vec) cnt += eval(v);
        return {cnt, 1};
    } else {
        pair<int, int> ll = {0, 0};
        for(auto& v: vec) {
            v.push_back(vc[i]);
            ll = merge(ll, bf(i + 1, n, vc, vec));
            v.pop_back();
        }
        return ll;
    }
}

pair<int, int> solve(){
    int m, n;
    scanf("%d %d", &m, &n);
    vector<string> vec;
    for(int i = 0; i < m; i++){
        char buf[101];
        scanf("%s", buf);
        vec.push_back(buf);
    }
    vector<vector<string>> dd(n);
    return bf(0, m, vec, dd);
}

int main(){
    int n;
    scanf("%d", &n);
    ofstream out ("D.out");
    for(int i = 1; i <= n; i++){
        auto a = solve();
        out << "Case #" << i << ": " << a.first << " " << a.second << "\n";
    }
}
