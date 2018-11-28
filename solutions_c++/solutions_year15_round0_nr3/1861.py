//#pragma comment(linker,"/STACK:102400000,102400000")
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<string>
#define ll long long
#define db double
#define PB push_back
#define lson k<<1
#define rson k<<1|1
using namespace std;

const int N = 10005;

struct node
{
    int x, y;
    node(int _x = 0, int _y = 0): x(_x), y(_y) {}
    void setval(char t)
    {
        x = 1;
        if(t == 'i') y = 1;
        else if(t == 'j') y = 2;
        else y = 3;
    }
    node operator * (const node & t) const
    {
        if(y == t.y)
        {
            if(y == 0) return node(x * t.x, 0);
            else return node(-x * t.x, 0);
        }
        else
        {
            int m = y * t.y;
            if(m == 0) return node(x * t.x, max(y, t.y));
            node res;
            if(m == 2)
            {
                if(y < t.y) res.x = 1;
                else res.x = -1;
                res.y = 3;
            }
            else if(m == 3)
            {
                if(y < t.y) res.x = -1;
                else res.x = 1;
                res.y = 2;
            }
            else
            {
                if(y < t.y) res.x = 1;
                else res.x = -1;
                res.y = 1;
            }
            res.x *= x, res.x *= t.x;
            return res;
        }
    }
    node operator / (const node &t) const
    {
        node res(1, 0);
        if(t * res == *this) return res;
        for(int i = 1; i < 4; i++)
        {
            res.y = i;
            if(t * res == *this) return res;
        }
        res.x = -1;
        for(int i = 1; i < 4; i++)
        {
            res.y = i;
            if(t * res == *this) return res;
        }
        return node(-1, -1);
    }
    bool operator == (const node &t) const
    {
        return x == t.x && y == t.y;
    }
    void output()
    {
        printf("I am output: %d %d\n", x, y);
    }
} p[N], pre[N], tol[5], tail[N], indi[N], indk[N];

char str[N];

int main()
{
#ifdef PKWV
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("c-small.out","w",stdout);
#endif // PKWV
    int T, cas(1);
    scanf("%d", &T);
    while(T--)
    {
        int l, x;
        scanf("%d%d", &l, &x);
        scanf("%s", str);
        for(int i = 0; i < l; i++)
        {
            p[i].setval(str[i]);
            if(i > 0) pre[i] = pre[i - 1] * p[i];
            else pre[i] = p[i];
        }
        tol[0] = pre[l - 1];
        for(int i = 1; i < 4; i++)
            tol[i] = tol[i - 1] * pre[l - 1];
        tail[l - 1] = p[l - 1];
        for(int i = l - 2; i >= 0; i--)
            tail[i] = p[i] * tail[i + 1];
        node base(1, 0);
        int li(0);
        for(int i = 0; i < min(4, x); i++)
        {
            for(int j = 0; j < l; j++)
            {
                base = base * p[j];
                if(base.x == 1 && base.y == 1)
                {
                    indi[li].x = i, indi[li].y = j;
                    li++;
                }
            }
        }
//        for(int i=0;i<4;i++) tol[i].output();
//        for(int i=l-1;i>=0;i--) tail[i].output();
        base = node(1, 0);
        int lk(0);
        for(int i = 0; i < min(4, x); i++)
        {
            for(int j = l - 1; j >= 0; j--)
            {
//                printf("%d %d == ",i,j);
                base = p[j] * base;
//                base.output();
                if(base.x == 1 && base.y == 3)
                {
//                    printf(":::: %d %d\n",x-i-1,j);
                    indk[lk].x = x - i - 1, indk[lk].y = j;
                    lk++;
                }
            }
        }
        node ans = node(1, 2) * node(1, 1) * node(1, 2);
//        printf("^^^^^ %d %d\n",ans.x,ans.y);
        bool ok = false;
        for(int i = 0; i < li; i++)
        {
//            printf("*** %d %d\n",indi[i].x,indi[i].y);
            for(int k = 0; k < lk; k++)
            {
//                printf("&&&& %d %d\n",indk[k].x,indk[k].y);
                if(indi[i].x < indk[k].x || indi[i].x == indk[k].x && indi[i].y < indk[k].y - 1)
                {
                    node res;
                    if(indi[i].x < indk[k].x)
                    {
                        node a, b, c;
                        if(indi[i].y + 1 < l) a = tail[indi[i].y + 1];
                        else a = node(1, 0);
                        if(indk[k].y - 1 >= 0) b = pre[indk[k].y - 1];
                        else b = node(1, 0);
                        int deta = indk[k].x - indi[i].x;
                        deta += 2;
                        deta %= 4;
//                        printf("%d===\n",deta);
                        c = tol[deta];
//                        a.output(),b.output(),c.output();
                        res = a * c * b;
                    }
                    else
                    {
                        res = pre[indk[k].y - 1] / pre[indi[i].y];
                    }
                    if(res.x == 1 && res.y == 2)
                    {
                        ok = true;
                        break;
                    }
                }
                else break;
            }
            if(ok) break;
        }
        printf("Case #%d: %s\n", cas++, ok ? "YES" : "NO");
    }
    return 0;
}
