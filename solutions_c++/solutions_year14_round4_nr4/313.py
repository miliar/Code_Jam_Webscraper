//
// trie.cpp
//
// Siwakorn Srisakaokul - ping128
// Written on Saturday, 31 May 2014.
//

#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <algorithm>
#include <map>
#include <ctype.h>
#include <string.h>

#include <assert.h>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<PII, int> PII2;

#define MAXM 1005
#define MAXN 105

string in[MAXM];
int M, N;

int group_id[MAXM];
int used[MAXN];

map<int, int> counter;
int num_node;

typedef struct node {
    node *next[26];
    node () {
        for (int i = 0; i < 26; i++) {
            next[i] = NULL;
        }
    }
}TrieNode, *TrieNodePtr;

bool insert(TrieNodePtr &cur, char c) {
    bool ret = false;
    if (cur->next[c - 'A'] == NULL) {
        ret = true;
        cur->next[c - 'A'] = new TrieNode();
        num_node++;
    }
    cur = cur->next[c - 'A'];
    return ret;
}


void search(int x) {
    if (x == M) {
        for (int i = 0; i < N; i++) used[i] = 0;
        for (int i = 0; i < M; i++) used[group_id[i]] = 1;
        for (int i = 0; i < N; i++) {
            if (used[i] == 0) return ;
        }

        //        for (int i = 0; i < M; i++) cout << group_id[i] << " ";
        //        cout << endl;

        num_node = 0;
        for (int i = 0; i < N; i++) {
            TrieNodePtr root = new TrieNode();
            num_node++;
            for (int j = 0; j < M; j++) {
                if (group_id[j] == i) {
                    TrieNodePtr cur = root;
                    for (int k = 0; k < in[j].size(); k++)
                        insert(cur, in[j][k]);
                }
            }
        }

        counter[num_node]++;
        return ;
    }
    for (int i = 0; i < N; i++) {
        group_id[x] = i;
        search(x + 1);
    }
}

void solve() {
    counter.clear();
    cin >> M >> N;
    for (int i = 0; i < M; i++) {
        cin >> in[i];
    }
    search(0);
    auto it = counter.end();
    it--;
    cout << it->first << " " << it->second << endl;
}

int main() {
    int test;
    scanf("%d", &test);
    for (int tt = 0; tt < test; tt++) {
        printf("Case #%d: ", tt + 1);
        solve();
    }
    return 0;
}
