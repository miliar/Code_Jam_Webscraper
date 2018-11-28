#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
using namespace std;
#define ll long long
const int mo = 1000002013;
struct node {ll x, p, type;}b[10000], sta[10000];
struct inp {ll l, r, p; } a[10000];
int t;
ll n, m;

ll cal(ll x, ll y, ll z)
{
   ll v = ((n + n - (y - x - 1)) * (y - x) / 2) % mo;
    return ((z * v) % mo) % mo;
}

bool cmp(node a, node b)
{
     if (a.x < b.x) return true;
     if (a.x == b.x && a.type < b.type) return true;
     return false;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    ll ans1, ans2;
    int ts, ks, i, j;
    ll v;
    cin >> ts;
    for (ks = 0; ks < ts; ks++){
        cin >> n >> m;
        t = 0;
        ans1 = 0; ans2 = 0;
        for (i = 0; i < m; i++){
            cin >> a[i].l >> a[i].r >> a[i].p;
            ans1 = (ans1 + cal(a[i].l, a[i].r, a[i].p)) % mo;
            if (ans1 < 0) 
               cout << "haha" << endl;
            b[t].p = a[i].p; b[t].type = 0; b[t++].x = a[i].l; 
            b[t].p = a[i].p; b[t].type = 1; b[t++].x = a[i].r;
        }
        //sort(b, b + t);
       // j = 0;
       // for (i = 1; i < t; i++)
       //     if (b[i] != b[j]){
       //        b[j++] = b[i];
       //     }
       // t = j;
        
      //  for (i = 0; i < m; i++){
      //      a[i].l = find(a[i].l);
      //      a[i].r = find(a[i].r);
      //  }
      //  sort(a, a + m, cmp);
         sort(b, b + t, cmp);
         int top = 0;
         for (i = 0; i < t; i++){
             if (b[i].type == 0){
                sta[top++] = b[i];
             }
             else {
                  while (b[i].p > 0){
                        ll v = min(sta[top-1].p, b[i].p);
                        ans2 = (ans2 + cal(sta[top - 1].x, b[i].x, v)) % mo;
                        if (ans2 < 0) cout << "haha" << endl;
                        sta[top - 1].p -= v;
                        b[i].p -= v;
                        if (sta[top-1].p == 0) top--;
                  }
             }
         }
         cout << "Case #" << ks + 1<< ": " << (ans1 + mo - ans2) % mo << endl;
    }
    return 0;
}
