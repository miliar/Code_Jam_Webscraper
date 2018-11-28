#include <iostream>
#include <cmath>
#include <cstring>
#include <queue>
#include <vector>
#include <cstdio>
#include <map>
#include <stack>
#include <set>
#include <algorithm>
#define ll long long
using namespace std;
const int Maxn = 100010 , Maxm = 11, Mo = 1e9 + 7;
const int oo = 1ll << 30;
#define PB push_back

int T, cs = 1;
int n, d, m, nq;
struct Inv{
    int l, r;
}a[Maxn];
int mk[Maxn * 3], t[Maxn * 3];
void check(int k, int l, int r){
    if (l < r){
        mk[k * 2] |= mk[k];
        mk[k * 2 + 1] |= mk[k];
    }
    if (mk[k]) t[k] = r - l + 1;
    mk[k] = 0;
}
int ask(int k, int l, int r, int x, int y){
    check(k, l, r);
    if (r < x || y < l) return 0;
    if (x <= l && r <= y) return t[k];
    int mid = (l + r) >> 1;
    return ask(k * 2, l, mid, x,  y) + ask(k * 2 + 1, mid + 1, r, x, y);    
}
void ins(int k, int l, int r, int x, int y){
    check(k, l, r);
    if (r < x || y < l) return;
    if (x <= l && r <= y){
        mk[k] = 1;
        check(k, l, r);
        return;
    }
    int mid = (l + r) >> 1;
    ins(k * 2, l, mid, x, y);
    ins(k * 2 + 1, mid + 1, r, x, y);
    t[k] = t[k * 2] + t[k * 2 + 1];
}
int main(){
    cin >> n >> d >> nq;
    for (int i = 1, l, r; i <= n; i++){
        cin >> a[i].l >> a[i].r;
    }
    for (int i = 1, td; i <= nq; i++){
        cin >> td; 
        memset(t,0,sizeof(t));
        memset(mk,0,sizeof(mk));
        for (int i = 1; i <= n; i++){
            if (a[i].r - a[i].l + 1 >= td)
                if (ask(1, 1, d, a[i].l, a[i].r) == 0){
                    //cout << i << endl;
                    ins(1, 1, d, a[i].l, a[i].r);
                }
        }
        cout << ask(1, 1, d, 1, d) << endl;
    }
}