#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include <utility>

using namespace std;

#define MAXM 10
#define MAXN 6

struct Trie {
    Trie *f[26];
    
    Trie() {
        for(int i = 0; i < 26; i++)
            f[i] = NULL;
    }
    
    ~Trie() {
        for(int i = 0; i < 26; i++)
            delete f[i];
    }
};

int T, M, N;
string S[MAXM];
int in[MAXM];
vector<string> L[MAXN];
int vmax, nrMax;

int buildTrie(vector<string> &A) {
    Trie *root = new Trie();
    int ret = 1;
    for(vector<string> :: iterator it = A.begin(); it != A.end(); it++) {
        Trie *t = root;
        string &s = *it;
        for(size_t i = 0; i < s.size(); i++) {
            int p = s[i] - 'A';
            if(t->f[p] == NULL) {
                t->f[p] = new Trie();
                ret++;
            }
            t = t->f[p];
        }
    }
    delete root;
    return ret;
}

void check() {
    for(int i = 0; i < N; i++)
        L[i].clear();
    for(int i = 0; i < M; i++)
        L[in[i]].push_back(S[i]);
    for(int i = 0; i < N; i++)
        if(L[i].size() == 0)
            return;
    
    int crt = 0;
    for(int i = 0; i < N; i++)
        crt += buildTrie(L[i]);
    
    if(crt == vmax)
        nrMax++;
    else if(crt > vmax) {
        vmax = crt;
        nrMax = 1;
    }
}

void back(int p) {
    if(p == M) {
        check();
        return;
    }
    
    for(int i = 0; i < N; i++) {
        in[p] = i;
        back(p + 1);
    }
}

int main() {
	freopen("date.in", "r", stdin);
	freopen("date.out","w", stdout);
	
	cin >> T;
	for(int t = 1; t <= T; t++) {
        cin >> M >> N;
        for(int i = 0; i < M; i++)
            cin >> S[i];
        
        vmax = 0;
        nrMax = 0;
        back(0);
        
        cout << "Case #" << t << ": " << vmax << " " << nrMax << '\n';
	}
	
	return 0;
}
