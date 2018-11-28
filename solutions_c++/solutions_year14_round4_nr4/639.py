#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <memory>
#include <vector>
#include <cstdio>
#include <bitset>
using namespace std;
int n , m;
int belong[10];
string a[10];
int ans, cnt;

struct node
{
    map<char , node *> children;
    char c;
    node(char _c = ' '):c(_c){};
    ~node()
    {
        for (map<char , node *>::iterator it = children.begin() ; it != children.end() ; ++it)
            delete it->second;
    }
};

int build_tree(const vector<string> &a)
{
    int cnt = 0;
    node * root = new node();
    ++cnt;
    for (vector<string>::const_iterator vit = a.begin(); vit != a.end() ; ++vit)
    {
        const string & s = *vit;
        node * p = root;

        for (string::const_iterator it = s.begin() ; it != s.end() ; ++it)
            if (p->children.count(*it))
            {
                p = p->children[*it];
            }
            else
            {
                ++cnt;
                node * new_node = new node(*it);
                p->children[*it] = new_node;
                p = new_node;
            }
    }
    delete root;
    return cnt;
}

int calc()
{
    vector< vector<string> > str_sets;
    str_sets.resize(n);
    for (int i = 0 ; i < m ; ++i)
        str_sets[belong[i]].push_back(a[i]);
    for (int i = 0 ; i < n ; ++i)
        if (str_sets[i].empty())
            return 0;
    int ans = 0;
    for (int i = 0 ; i < n ; ++i)
        ans += build_tree(str_sets[i]);
    return ans;
}

void gen_arr(int depth)
{
    if (depth == m)
    {
        int result = calc();
        if (ans < result)
            ans = result, cnt = 1;
        else if (ans == result)
            ++cnt;
        return ;
    }
    for (int i = 0; i < n ; ++i)
        belong[depth] = i, gen_arr(depth + 1);
}

static inline void process(int t)
{
    cin >> m >> n;
    for (int i = 0; i < m ; ++i)
        cin >> a[i];
    sort(a , a + m);
    ans = cnt = 0;
    gen_arr(0);
    printf("Case #%d: %d %d\n", t, ans , cnt);
}
int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t ; ++i)
        process(i + 1);
    return 0;
}
