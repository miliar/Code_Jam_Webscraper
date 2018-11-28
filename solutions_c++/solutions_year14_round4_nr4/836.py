#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define all(o) (o).begin(), (o).end()
#define allr(o) (o).rbegin(), (o).rend()
const int INF = 2147483647;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> int size(T &x) { return x.size(); }

// assert or gtfo

vector<string> S;

int m, n;

template <class T>
class trie {
public:
    struct node {
        map<T, node*> children;
        int prefixes, words;
        node() { prefixes = words = 0; } };
    node* root;
    trie() : root(new node()) {  }
    template <class I>
    void insert(I begin, I end) {
        node* cur = root;
        while (true) {
            cur->prefixes++;
            if (begin == end) { cur->words++; break; }
            else {
                T head = *begin;
                typename map<T, node*>::const_iterator it;
                it = cur->children.find(head);
                if (it == cur->children.end()) {
                    pair<T, node*> nw(head, new node());
                    it = cur->children.insert(nw).first;
                } begin++, cur = it->second; } } }
    template<class I>
    int countMatches(I begin, I end) {
        node* cur = root;
        while (true) {
            if (begin == end) return cur->words;
            else {
                T head = *begin;
                typename map<T, node*>::const_iterator it;
                it = cur->children.find(head);
                if (it == cur->children.end()) return 0;
                begin++, cur = it->second; } } }
    template<class I>
    int countPrefixes(I begin, I end) {
        node* cur = root;
        while (true) {
            if (begin == end) return cur->prefixes;
            else {
                T head = *begin;
                typename map<T, node*>::const_iterator it;
                it = cur->children.find(head);
                if (it == cur->children.end()) return 0;
                begin++, cur = it->second; } } }

    int cnt()
    {
        return cnt(root);
    }

    int cnt(node *nd)
    {
        if (nd == 0)
            return 0;

        int sm = 1;
        typename map<T, node*>::const_iterator it;
        for (it = nd->children.begin(); it != nd->children.end(); ++it)
        {
            sm += cnt(it->second);
        }

        return sm;
    }
};

pair<int, ll> mem[5][1 << 9];
bool comp[5][1 << 9];

pair<int, ll> dp(int at, int done)
{
    if (at == n)
    {
        if (done == ((1 << m) - 1))
        {
            return pair<int, ll>(0, 1);
        }
        else
        {
            return pair<int, ll>(0, 0);
        }
    }
    else if (done == ((1 << m) - 1))
    {
        return pair<int, ll>(0, 0);
    }
    else
    {
        if (comp[at][done])
            return mem[at][done];

        int mx = 0;
        ll cnt = 0;

        for (int i = 1; i < (1 << m); i++)
        {
            if ((done & i) == 0)
            {

                trie<char> T;
                for (int j = 0; j < m; j++)
                {
                    if (i & (1 << j))
                    {
                        T.insert(all(S[j]));
                    }
                }

                int cur = T.cnt();
                // assert(cur >= 1);
                pair<int, ll> rest = dp(at + 1, done | i);

                if (rest.second == 0)
                    continue;

                cur += rest.first;

                if (cur < mx)
                {
                    continue;
                }
                else if (cur > mx)
                {
                    mx = cur;
                    cnt = 0;
                }

                cnt += rest.second;
            }
        }

        comp[at][done] = true;

        return mem[at][done] = make_pair(mx, cnt);
    }
}

int main()
{
    int ts;
    scanf("%d\n", &ts);

    for (int t = 0; t < ts; t++)
    {
        printf("Case #%d: ", t+1);

        scanf("%d %d\n", &m, &n);

        S = vector<string>(m);
        for (int i = 0; i < m; i++)
        {
            cin >> S[i];
        }

        memset(comp, 0, sizeof(comp));
        pair<int, ll> res = dp(0, 0);
        cout << res.first << " " << res.second << endl;
    }

    return 0;
}

