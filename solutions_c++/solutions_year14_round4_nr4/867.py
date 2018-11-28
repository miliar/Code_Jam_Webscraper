#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

struct Trie
{
    char key;
    vector<Trie *> vec;
} *head;

int ans, ccc;
char s[10][12];
int server[10][10];
int cnt_s[10];

void add_trie(Trie *ptr, char *s, int pos)
{
    if( s[pos] == '\0' ) return;
    for( int i = 0, ii = ptr->vec.size(); i < ii; i++ )
        if( ptr->vec[i]->key == s[pos] )
        {
            add_trie(ptr->vec[i], s, pos + 1);
            return;
        }
    Trie *tmp = new Trie;
    tmp->key = s[pos];
    ptr->vec.push_back(tmp);
    add_trie(ptr->vec[ptr->vec.size() - 1], s, pos + 1);
    return;
}

void count_node(Trie *head, int &aaacnt)
{
    aaacnt++;
    for( int i = 0, ii = head->vec.size(); i < ii; i++ ) count_node(head->vec[i], aaacnt);
    head->vec.clear();
    delete head;
}

void cnt_ans(int m)
{
    int aaacnt = 0;
    for( int i = 0; i < m; i++ )
    {
        head = new Trie;
        head->key = '\0';
        for( int j = 0; j < cnt_s[i]; j++ )
        {
            add_trie(head, s[server[i][j]], 0);
        }
        count_node(head, aaacnt);
    }
    if( aaacnt > ans )
    {
        ans = aaacnt;
        ccc = 1;
    }
    else if( aaacnt == ans ) ccc++;
}

void DFS(int n, int m, int p)
{
    if( p == n )
    {
        for( int i = 0; i < m; i++ )
            if( cnt_s[i] == 0 ) return;
        cnt_ans(m);
        return;
    }
    for( int i = 0; i < m; i++ )
    {
        server[i][cnt_s[i]] = p;
        cnt_s[i]++;
        DFS(n, m, p + 1);
        cnt_s[i]--;
    }
    return;
}

int main()
{
    int cases;
    scanf("%d", &cases);
    for( int tt = 1; tt <= cases; tt++ )
    {
        int n, m;
        scanf("%d %d", &n, &m);
        for( int i = 0; i < n; i++ ) scanf("%s", s[i]);
        ans = 0; ccc = 0;
        for( int i = 0; i < m; i++ ) cnt_s[i] = 0;
        DFS(n, m, 0);
        printf("Case #%d: %d %d\n", tt, ans, ccc);
    }
    return 0;
}
