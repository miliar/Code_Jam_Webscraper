#include <iostream>
#include <cstdio>

using namespace std;

const int L = 105, N = 10;
char word[N][L];
int n, m;
long long best, cnt;

struct node
{
    node *next[26];
    node() { for(int i = 0; i < 26; i++) next[i] = NULL; }
} ;
void kill(node *x)
{
    if(x == NULL) return;
    for(int i = 0; i < 26; i++) kill(x->next[i]);
    delete x;
}

long long count(node *x)
{
    if(x == NULL) return 0;
    long long res = 1;
    for(int i = 0; i < 26; i++) res += count(x->next[i]);
    return res;
}

struct trie
{
    node *root;
    bool asdf;
    void init() { asdf = false; kill(root); root = new node; }
    void insert(char s[])
    {
        asdf = true;
        node *n = root;
        for(int i = 0; s[i]; i++)
        {
            if(!n->next[s[i] - 'A']) n->next[s[i] - 'A'] = new node;
            n = n->next[s[i] - 'A'];
        }
    }
} ;

trie tries[5];

void solve(int a[])
{
    long long num = 0;
    for(int i = 0; i < n; i++) tries[i].init();
    for(int i = 0; i < m; i++)
        tries[a[i]].insert(word[i]);
    for(int i = 0; i < n; i++) num += tries[i].asdf ? count(tries[i].root) : 0;

    if(num > best) { best = num; cnt = 1; }
    else if(num == best) cnt++;
}

int ngen;
void gen(int curr, int a[])
{
    if(curr == m) { ngen++; solve(a); }
    else for(int i = 0; i < n; i++) { a[curr] = i; gen(curr + 1, a); }
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int test;
    scanf("%i", &test);

    for(int t = 0; t < test; t++)
    {
        scanf("%i %i", &m, &n);
        for(int i = 0; i < m; i++) scanf(" %s", &word[i]);

        ngen = 0;

        int a[N];
        best = -1; cnt = 0;
        gen(0, a);

        printf("Case #%i: %lld %lld\n", t + 1, best, cnt % 1000000007);
        //printf("%i\n", ngen);
    }

    return 0;
}

