#include <iostream>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

#define mo 1000002013
#define maxn 1007

long long ans;
long long my;
long long z;
int n, m;
struct atype
{
  int o, e, p;
} a[maxn];
struct btype
{
    long long x, y;
} b[maxn+maxn], t[maxn+maxn];


bool cmp(atype p, atype q)
{
    return p.o<q.o;
}
bool cmpb(btype p, btype q)
{
    if (p.x < q.x) return true;
    if (p.x > q.x) return false;
    if (p.y > 0 && q.y < 0) return true;
    return false;
}
int main()
{
    freopen("A.in","r",stdin);
    freopen("A1.out","w",stdout);

    int cases, k, i, j, h, p, q;

    scanf("%d",&cases);
    for (k = 1; k <= cases; ++k) {
        printf("Case #%d: ",k);
        scanf("%d%d",&n,&m);
        h = 0;
        for (i = 0; i < m; ++i) {
            scanf("%d%d%d",&a[i].o,&a[i].e,&a[i].p);
            if (a[i].o == a[i].e) continue;
            b[h].x = a[i].o;
            b[h].y = a[i].p;
            ++h;
            b[h].x = a[i].e;
            b[h].y = -a[i].p;
            ++h;
        }
        ans = 0;
        for (i = 0; i < m; ++i) {
            z = a[i].e-a[i].o;
            z = (n+(n-z+1))*z/2;
            ans = (ans+z*a[i].p)%mo;
        }
        sort(b,b+h,cmpb);
        my = 0; p = 1; q = 0;
        for (i = 0; i < h; ++i) {
            if (i > 0 && b[i].x > b[i-1].x) {
                for (j = p; j <= q; ++j){
                    z = b[i].x-b[i-1].x;
                    if (t[j].x > n) {
                        z = (n+n-(z-1)+1)*(z-1)/2;
                    }
                    else {
                        z = (t[j].x+t[j].x-z+1)*z/2;
                    }
                    my = (my+z*t[j].y)%mo;
                    t[j].x -= b[i].x-b[i-1].x;
                }
            }
            if (b[i].y > 0) {
                ++q;
                t[q].x = n+1;
                t[q].y = b[i].y;
            }
            else {
                while (b[i].y+t[q].y <= 0) {
                    b[i].y += t[q].y;
                    if (t[q].x <= n) my = (my+t[q].x*t[q].y)%mo;
                    --q;
                    if (b[i].y == 0) break;
                }
                if (b[i].y < 0) {
                    if (t[q].x <= n) my = (my-b[i].y*t[q].x)%mo;
                    t[q].y += b[i].y;
                }
            }
        }
        ans -= my;
        if (ans < 0) ans += mo;
        cout << ans << endl;
    }
    return 0;
}
