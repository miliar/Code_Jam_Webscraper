#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <climits>

using namespace std;

struct Trie {
    struct TrieNode {
        struct TrieNode *next[26];
        TrieNode() {
            for(int i=0;i<26;++i)
            {
                next[i] = NULL;
            }
        }
        ~TrieNode() {
            for(int i=0;i<26;++i)
            {
                if(next[i] != NULL){delete next[i];}
            }
        }
    };
    struct TrieNode root;
    int curr_size;
    Trie() {
        curr_size = 1;
    }
    void add(const char *s) {
        TrieNode *curr = &root;
        while(*s) {
            char ch = *s++;
            int idx = ch-'A';
            if(curr->next[idx] == NULL){
                curr->next[idx] = new TrieNode();
                ++curr_size;
            }
            curr = curr->next[idx];
        }
    }
};
int bestcount;
int bestsc;

int foo[16];
struct Trie *trees[16];
vector<string> strings;
void do_dfs(int at, int M, int N)
{
    if(at == M)
    {
        for(int i=0;i<N;++i)
        {
            trees[i] = new Trie();
        }
        for(int i=0;i<M;++i)
        {
            trees[foo[i]]->add(strings[i].c_str());
        }
        int sc = 0;
        for(int i=0;i<N;++i)
        {
            sc += trees[i]->curr_size;
            if(trees[i]->curr_size == 1){--sc;}
        }
        if(sc > bestsc){bestsc = sc;bestcount = 0;}
        if(sc == bestsc){++bestcount;}
        for(int i=0;i<N;++i)
        {
            delete trees[i];
            trees[i] = NULL;
        }
        return;
    }
    for(int i=0;i<N;++i)
    {
        foo[at] = i;
        do_dfs(at+1, M, N);
    }
}

void solve_case(const int cn)
{
    int M,N;
    cin >> M >> N;
    vector<string> vs(M, string());
    for(int i=0;i<M;++i)
    {
        cin >> vs[i];
    }
    ::strings = vs;
    ::bestsc= 0;
    ::bestcount = 0;
    do_dfs(0, M, N);
    printf("Case #%d: %d %d\n", cn, bestsc, bestcount);
}

int main(int argc, char **argv)
{
    int CASES;
    cin >> CASES;
    for(int cn=1;cn<=CASES;++cn)
    {
        solve_case(cn);
    }
    return 0;
}
