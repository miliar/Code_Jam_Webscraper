#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <cstring>
#include <map>

using namespace std;

const int MAXN = 200;

struct node
{
    node *link[300];
};

int SIZE = 0;
node MEM[MAXN];
node *root;

inline void init_tree()
{
    root = &(MEM[0]);
    memset(MEM, 0, sizeof(MEM));
    SIZE = 1;
}

inline node *new_node()
{
    return &(MEM[SIZE++]);
}

inline void push_tree(string &s)
{
    node *cur = root;
    for (int i = 0; i < s.size(); i++) {
        if (!cur->link[s[i]]) {
            cur->link[s[i]] = new_node();
        }
        cur = cur->link[s[i]];
    }
}

vector< string > s;
vector< vector< int > > division;
int n, m;

int cases = 0;
int bad_num = 0;

int check()
{
    int res = 0;
    for (int i = 0; i < n; i++)
    {
        init_tree();
        if (division[i].empty()) {
            return 0;
        }
        for (int j = 0; j < division[i].size(); j++) {
            push_tree(s[division[i][j]]);
        }
        
        res += SIZE;
    }
    return res;
}

void rec(int i)
{
    if (i == m) {
        int res = check();
        if (res == bad_num) {
            cases++;
        } else if (res > bad_num) {
            bad_num = res;
            cases = 1;
        }
        return;
    }
    
    for (int j = 0; j < n; j++) {
        division[j].push_back(i);
        rec(i + 1);
        division[j].pop_back();
    }
}

void solve(int test_num)
{
    bad_num = 0;
    cases = 0;
    cin >> m >> n;
    s.resize(m);
    division.resize(n);
    for (int i = 0; i < m; i++)
        cin >> s[i];
    
    
    rec(0);
    
    cout << "Case #" << test_num + 1 << ": " << bad_num << " " << cases << "\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
        solve(i);
}