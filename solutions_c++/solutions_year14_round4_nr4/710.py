/*
 * Author: fatboy_cw
 * Created Time:  2014/5/31 23:37:57
 * File Name: D.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

int t, n, m, ans, cnt, ca, server[20];
string str[20];

struct node {
    int ch[26];
    node() {
        memset(ch, -1, sizeof(ch));
    }
};

void insert(vector<node> &trie, string s) {
    int now = 0;
    for(int i = 0; i < s.size(); i++) {
        int l = s[i] - 'A';
        if(trie[now].ch[l] == -1) {
            trie[now].ch[l] = trie.size();
            trie.push_back(node());
        }
        now = trie[now].ch[l];
    }
}

int cntTrie(const vector<int> &v) {
    vector<node> trie = vector<node>(1);
    for(int i = 0; i < v.size(); i++) {
        string s = str[v[i]];
        insert(trie, s);
    }
    if(trie.size() == 1) return 0;
    return trie.size();
}

int calc() {
    int res = 0;
    for(int i = 0; i < m; i++) {
        vector<int> elements;
        for(int j = 0; j < n; j++) {
            if(server[j] == i) {
                elements.push_back(j);
            }
        }
        res += cntTrie(elements);
    }
    return res;
}

void dfs(int step) {
    if(step == n) {
        int res = calc();
        if(res > ans) {
            ans = res;
            cnt = 1;
        }
        else if(res == ans) {
            cnt += 1;
        }
        return;
    }
    for(int i = 0; i < m; i++) {
        server[step] = i;
        dfs(step + 1);
    }
}

int main() {
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);
    cin >> t;
    while(t--) {
        cin >> n >> m;
        for(int i = 0; i < n; i++) {
            cin >> str[i];
        }
        ans = -1;
        dfs(0);
        printf("Case #%d: %d %d\n", ++ca, ans, cnt);
    }
    return 0;
}

