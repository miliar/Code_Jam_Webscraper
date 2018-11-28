#include <bits/stdc++.h>

using namespace std;

const int N = (int)1e2 + 10;

struct treap{
    int x, y, sz;
    bool rev;
    treap *left, *right;
    treap(){};
    treap(int x) : x(x){
        y = rand() | (rand() << 16);
        rev = false;
        sz = 1;
        left = right = NULL;
    }
};

int get_sz(treap *t) {return t == NULL ? 0 : t->sz;}
void update(treap *t) {
    if (t == NULL) return ;
    t->sz = get_sz(t->left) + get_sz(t->right) + 1;
}
void push(treap *t) {
    if (t == NULL) return ;
    if (t->rev){
        if (t->left != NULL) t->rev ^= 1;
        if (t->right != NULL) t->rev ^= 1;
        swap(t->left, t->right);
        t->rev = false;
    }
}
void Merge(treap *&t, treap *left, treap *right){
    push(left);
    push(right);
    if (left == NULL || right == NULL){
        t = (right == NULL ? left : right);
        return ;
    }
    if (left->y > right->y){
        Merge(left->right, left->right, right);
        t = left;
    } else {
        Merge(right->left, left, right->left);
        t = right;
    }
    update(t);
}


void Split(treap *t, int key, treap *&left, treap *&right){
    push(t);
    if (t == NULL){
        left = right = NULL;
        return ;
    }
    int curidx = get_sz(t->left) + 1;
    if (curidx <= key){
        Split(t->right, key - curidx, t->right, right);
        left = t;
    } else {
        Split(t->left, key, left, t->left);
        right = t;
    }
    update(left);
    update(right);
}

void Insert(treap *&t, int pos, int x){
    if (t == NULL){
        t = new treap(x);
        return ;
    }
    treap *l, *r, *m;
    l = r = m = NULL;
    Split(t, pos, l, r);
    m = new treap(x);
    Merge(t, l, m);
    Merge(t, t, r);
}

void Reverse(treap *&t, int A, int B){
    treap *l, *r, *m;
    l = r = m = NULL;
    Split(t, A, l, r);
    Split(r, B - A, m, r);
    m->rev ^= 1;
    Merge(t, l, m);
    Merge(t, t, r);
}

int kth(treap *cur, int k){
    while (cur != NULL){
        int leftsz = get_sz(cur->left);
        if (k == leftsz) return cur->x;
        cur = (k < leftsz ? cur->left : cur->right);
        if (k > leftsz) k -= leftsz + 1;
    }
    return -1;
}

void del(treap *t){
    if (t == NULL) return ;
    del(t->left);
    del(t->right);
    delete t;
}

treap *t;

int solve1(string s){
    int n = s.length();
    bool flip = false;
    int res = 0;
    for (int i = 0; i < n; ++i) Insert(t, i, (s[i] == '+' ? 1 : 0));
    for (int i = n - 1; i >= 0; --i){
        int cur = kth(t, i);
        if (flip) cur = !cur;
        if (cur != 0){
            flip ^= 1;
            ++i;
            Reverse(t, 0, i);
            res++;
            if (res > 100) return -1;
        }
    }
    return res + 1;
}

int solve2(string s){
    int n = s.length();
    bool flip = false;
    int res = 0;
    for (int i = 0; i < n; ++i) Insert(t, i, (s[i] == '+' ? 1 : 0));
    for (int i = n - 1; i >= 0; --i){
        int cur = kth(t, i);
        if (flip) cur = !cur;
        if (cur == 0){
            flip ^= 1;
            ++i;
            Reverse(t, 0, i);
            res++;
            if (res > 100) return -1;
        }
    }
    return res;
}

int solve(string s){
    string t;
    for (int i = 0; i < s.length(); ++i){
        if (t.size() == 0 || t[t.size() - 1] != s[i]) t += s[i];
    }
    if (t[0] == '-'){
        int cnt = 0;
        for (int i = 0; i < t.size(); ++i) cnt += (t[i] == '-' ? 1 : 0);
        return 2 * (cnt - 1) + 1;
    } else {
        if (t.size() == 1) return 0;
        return (t.size() / 2) * 2;
    }
}
int n;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n;
    for (int i = 0; i < n; ++i){
        string s; cin >> s;
        cout << "Case #" << i + 1 << ": " << solve(s) << endl;
    }
    return 0;
}
