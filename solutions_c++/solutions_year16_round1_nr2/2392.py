#include <stdio.h>
#include <bits/stdc++.h>
#include <string.h>

using namespace std;

const int max_n = 52;
const int big = 10000;

typedef vector<vector<int>> mat;
typedef vector<bool> vb;

mat             a, ar;
vector<bool>    u, ur;
vector<int>     b[max_n*2];
int             n;


void init()
{
    for (auto &x : b)
        x.clear();
    cin >> n;
    a.resize(n);
    ar.resize(n);
    u.assign(n, false);
    ur = u;
    for (int i=0; i<n; ++i) {
        a[i].assign(n, big);
        ar[i].assign(n, big);
    }
    for (int i=0; i+1<2*n; ++i)
        for (int j=0; j<n; ++j) {
            int x;
            cin >> x;
            b[i].push_back(x);
        }
}

void s1()
{
    a[0] = b[0];
    for (int j=0; j<n; ++j)
        ar[j][0] = b[0][j];
}

bool valid(const mat& m, const vector<int>& v, const int idx)
{
    //if (m[idx] == v) return false;
    for (int i=0; i<n; ++i)
        if (m[idx][i] != big && m[idx][i] != v[i]) return false;
    return true;
}

void print_vec(const vector<int> &v) {
    for (int i=0; i<v.size(); ++i)
        printf("%d%c", v[i], i==v.size()-1?'\n':' ');
}
void print_mat(const mat& m)
{
    for (int i=0; i<n; ++i)
        print_vec(m[i]);
}

void put(mat &m, mat &rm, mat& ba, mat& bar, vb &used, const vector<int>& v, int idx) {
    ba = m;
    bar = rm;
    m[idx] = v;
    used[idx] = true;
    for (int i=0; i<n; ++i)
        rm[i][idx] = v[i];
    
}

void unput(mat &m, mat &rm, mat& ba, mat& bar, vb& used, const vector<int>& v, int idx) {
    used[idx] = false;
    m = ba;
    rm = bar;
    /*
    m[idx].assign(n, big);
    for (int i=0; i<n; ++i)
        rm[i][idx] = big;
    */
}

bool test(int cur)
{   
    if (cur == 2*n-1) return true;
    mat*    tab[2] = {&a, &ar};
    vb*     ftab[2] = {&u, &ur};
    const vector<int> & v = b[cur];
    for (int b=0; b<2; ++b) {
        auto p = lower_bound(tab[b]->begin(), tab[b]->end(), v);
        if (p == tab[b]->end()) continue;
        int idx = p-tab[b]->begin();
        if ((*ftab[b])[idx] || !valid(*tab[b], v, idx)) continue;
        mat ba, bar;
        put(*tab[b], *tab[!b], ba, bar, *ftab[b], v, idx);
        if (test(cur+1)) return true;
        else unput(*tab[b], *tab[!b], ba, bar, *ftab[b], v, idx);
    }
    return false;
}

void print_res()
{
    multiset<vector<int>> m(a.begin(), a.end());
    m.insert(ar.begin(), ar.end());
    for (int i=0; i+1<2*n; ++i) {
        m.erase(m.find(b[i]));
    }
    print_vec(*m.begin());
}


int main()
{
    int ncase;
    cin >> ncase;
    for (int ic=0; ic<ncase; ++ic) {
        init();
        sort(b, b+2*n-1);
        s1();
        test(1);
        printf("Case #%d: ", ic+1);
        print_res();
    }
    return 0;
}