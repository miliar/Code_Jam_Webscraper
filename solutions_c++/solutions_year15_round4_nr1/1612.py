#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <fstream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <stdio.h>
#include <set>
#define INF 1<<30
#define EPS 1e-8
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define M 10005
using namespace std;
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <fstream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <stdio.h>
#include <set>
#define INF 1<<30
#define EPS 1e-8
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define M 10005
using namespace std;
char mt[105][105];
bool dir[105][105][4];
bool vis[105][105];
char ch[] = {'<', '^', '>', 'v'};
int main() {
    freopen("A-large (2).in", "r", stdin);
    freopen("A-large (2).out", "w", stdout);
    int T, n, m, c = 0;
    scanf("%d", &T);
    int ans;
    while (T--) {
            scanf("%d%d", &n, &m);
            memset(dir, false, sizeof(dir));
            memset(vis, false, sizeof(vis));
             ans = 0;
    for (int i = 0; i < n; ++i) {
        scanf("%s", mt[i]);
    }
    printf("Case #%d: ", ++c);
    bool can = true;
            for (int i = 0; i < n; ++i) {
                int j = 0;
                while (j < m && mt[i][j] == '.')++j;
                if (j < m) {
                    dir[i][j][0] = true;
                    if (mt[i][j] == '<') {
                        if (!vis[i][j]) {
                            ++ans, vis[i][j] = true;
                        }
                        bool flag = false;
                        for (int k = 1; k < 4; ++k) {
                            if (!dir[i][j][k]) {
                                mt[i][j] = ch[k];
                                flag = true;
                                break;
                            }
                        }
                        if (!flag) {
                            puts("IMPOSSIBLE");
                            can = false;
                            break;
                        }
                    }
                }
                j = m - 1;
                while (j >=0 && mt[i][j] == '.')--j;
                if (j >= 0) {
                    dir[i][j][2] = true;
                    if (mt[i][j] == '>') {
                        if (!vis[i][j]) {
                            ++ans, vis[i][j] = true;
                        }
                        bool flag = false;
                        for (int k = 3, cnt = 0; cnt < 3; ++k, ++cnt) {
                            if (!dir[i][j][k%4]) {
                                mt[i][j] = ch[k%4];
                                flag = true;
                                break;
                            }
                        }
                        if (!flag) {
                            puts("IMPOSSIBLE");
                            can = false;
                            break;
                        }
                    }
                }
            }
            if (!can) {
                continue;
            }
            for (int j = 0; j < m; ++j) {
                int i = 0;
                while (i < n && mt[i][j] == '.')++i;
                if (i < n) {
                    dir[i][j][1] = true;
                    if (mt[i][j] == '^') {
                        if (!vis[i][j]) {
                            ++ans, vis[i][j] = true;
                        }
                        bool flag = false;
                        for (int k = 2, cnt = 0; cnt < 3; ++k, ++cnt) {
                            if (!dir[i][j][k%4]) {
                                mt[i][j] = ch[k%4];
                                flag = true;
                                break;
                            }
                        }
                        if (!flag) {
                            puts("IMPOSSIBLE");
                            can = false;
                            break;
                        }
                    }
                }
                i = n - 1;
                while (i >= 0 && mt[i][j] == '.')--i;
                if (i >= 0) {
                    dir[i][j][3] = true;
                    if (mt[i][j] == 'v') {
                        if (!vis[i][j]) {
                            ++ans, vis[i][j] = true;
                        }
                        bool flag = false;
                        for (int k = 0, cnt = 0; cnt < 3; ++k, ++cnt) {
                            if (!dir[i][j][k]) {
                                mt[i][j] = ch[k];
                                flag = true;
                                break;
                            }
                        }
                        if (!flag) {
                            puts("IMPOSSIBLE");
                            can = false;
                            break;
                        }
                    }
                }
            }
            if (!can) {
                continue;
            }
            /*
            if (mt[0][0] == '<' ||mt[0][0] == '^') ++ans mt[0][0] = '';

            if (mt[0][ m - 1] == '>' ||mt[0][m - 1] == '^') ++ans;
        if (mt[n - 1][ m - 1] == '>' ||mt[n - 1][m - 1] == 'v') ++ans;
        if (mt[n  - 1][ 0] == '<' ||mt[n - 1][0] == 'v') ++ans;

          for (int i = 1; i < n - 1; ++i) {
              if (mt[i][0] == '<') ++ans;
            if (mt[i][m-1] == '>')++ans;
          }
        for (int j = 1; j < m - 1; ++j) {

        if (mt[0][j] == '^') ++ans;
          if (mt[n - 1][j] == 'v')++ans;

        }
        */
        printf("%d\n", ans);
    }


    return 0;
}
/*
int main() {
    //freopen("a.txt", "r", stdin);
    memset(b, -1, sizeof(b));
    int n, m, k, c = 0;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &a[i]);
    }
    printf("Case #1:\n");
    while (m--) {
        scanf("%d", &k);
        if (b[k] != -1) {
            printf("%d\n", b[k]);
            continue;
        }
        st.clear();
        int i = 0, ans = 0, j = 0;
        num = 0;
        while (i < k) {
            st.insert(a[i]);
            //sum += a[i];
            if (st.count(a[i]) == 2) ++num;
            ++i;
        }
        --i;
        multiset<int>::iterator it;
        while (true){
            if (num == 0) {
                it = st.end();
                int l = *st.begin(), r = *(--it);
                if (r - l == k - 1) ++ans;
            }
            if(i == n - 1) break;
            st.erase(a[j]);
            if (st.count(a[j]) == 1) --num;
            st.insert(a[++i]);
            if (st.count(a[i]) == 2) ++num;
            ++j;
        }
        printf("%d\n", ans);
        b[k] = ans;
    }
    return 0;
}
*/


/*
struct Point{
    int x,y;
}p[M], sta[M];
int cmp(Point a,Point b)
{
    if(a.y == b.y)return a.x < b.x;
    return a.y < b.y;
}
int det(int x1,int y1,int x2,int y2)
{
    return x1*y2 - x2*y1;
}
int cross(Point c,Point a,Point b)
{
    return det(a.x-c.x,a.y-c.y,b.x-c.x,b.y-c.y);
}
double dis(Point a,Point b)
{
    return sqrt((a.x - b.x)*1.0*(a.x - b.x) + (a.y - b.y)*1.0*(a.y - b.y));
}
int now;
int n,l, x,y;
double cal_distance(Point a,const int u,const int v,const int w)
{
    return (a.x*u + a.y*v + w)*1.0/sqrt(u*u + v*v);
}
double solve(Point a,Point b)
{
    int del_max = 0, Max = -INF, Min = INF;
    if (a.y == b.y){
        for(int i = 0; i < now; i++){
            del_max = max(del_max, abs(sta[i].y - a.y));
            Max = max(Max, sta[i].x);
            Min = min(Min, sta[i].x);
        }
        return (double)del_max * (double)(Max - Min);
    }
    else if (a.x == b.x){
        for(int i = 0; i < now; i++){
            del_max = max(del_max, abs(sta[i].x - a.x));
            Max = max(Max, sta[i].y);
            Min = min(Min, sta[i].y);
        }
        return (double)del_max *(double)(Max - Min);
    }
    int u, v, w, u1, v1, w1;
    u = b.y - a.y;
    v = a.x - b.x;
    w = b.x*a.y - a.x*b.y;
    u1 = a.x - b.x;
    v1 = a.y - b.y;
    w1 = a.y*b.y - a.y*a.y + a.x*b.x - a.x*a.x;
    double dist1 = 0.0, dist2 = -INF, dist3 =INF;
    for(int i = 0;i < now; i++){
        dist1 = max(dist1, fabs(cal_distance(sta[i],u,v,w)));
        dist2 = max(dist2, cal_distance(sta[i],u1,v1,w1));
        dist3 = min(dist3, cal_distance(sta[i],u1,v1,w1));
    }
    return (dist2 - dist3) * dist1;
}
int main()
{
    //freopen("a.txt", "r", stdin);
    int T, c = 0;
    scanf("%d",&T);
    while (T--) {
        scanf("%d",&n);
        n<<=2;
        for(int i = 0;i < n; i++) {
            scanf("%d%d", &p[i].x, &p[i].y);
        }
        sort(p, p+n, cmp);
        sta[0] = p[0], sta[1] = p[1];
        now = 2;
        for(int i = 2;i < n; i++){
            while(now >= 2 && cross(sta[now-2],sta[now-1],p[i])<0) now--;
            sta[now++] = p[i];
        }
        int tmp = now;
        for(int i = n - 2;i >= 0;i--){
            while(now >= tmp && cross(sta[now-2], sta[now-1], p[i])<0)now--;
            sta[now++] = p[i];
        }
        double ans = INF, t;
        for(int i = 0; i < now-1; i++){
            if(sta[i].x == sta[i+1].x && sta[i].y == sta[i+1].y)continue;
            t = solve(sta[i],sta[i+1]);
            if (t < ans) ans = t;
        }
        printf("Case #%d:\n%.0f\n",++c,ans);
    }
    return 0;
}*/
/*
struct node{
    char s[100];
    int w;
}p[M];
int a[M];
queue<int> q;
int sum[M << 2];
int val[M << 2];
int mp[M];
void build(int l, int r, int rt) {
    sum[rt] = 0;
    if (l == r) {
        mp[l] = rt;
        return ;
    }
    int m = (l + r) >> 1;
    build(lson);
    build(rson);
}
void update(int pos, int v) {
    int rt  = mp[pos];
    while (true) {
        sum[rt] += v;
        if (rt == 1) break;
        rt >>= 1;
    }
}
int num;
int now;
int query(int l, int r, int rt) {
    while (true) {
        if (l == r) return a[l - 1];
        int m = (l + r) >> 1;
        if (sum[rt<<1] >= now){
            rt <<= 1;
            r = m;
        }
        else {
            now -= sum[rt<<1];
            l = m + 1;
            rt = rt<<1|1;
        }
    }
    return -1;
}
int main () {
    //freopen("a.txt", "r", stdin);

    int T, c = 0, n;
    int k = 0;

    while(scanf("%d", &n)!=EOF) {
    k = 0;
    while(!q.empty()) q.pop();
    for (int i = 0; i < n; ++i){
        scanf("%s", p[i].s);
        if (p[i].s[0] == 'i'){
            scanf("%d", &p[i].w);
            a[k++] = p[i].w;

        }
    }
    sort(a, a + k);
    build(1, n, 1);
    num = 0;
    printf("Case #%d:\n", ++c);
    for (int i = 0; i < n; ++i) {
        if (p[i].s[0] == 'i') {
           int pos = lower_bound(a, a + k, p[i].w) - a + 1;
           update(pos, 1);
           q.push(pos);
           ++num;
        }
        else if (p[i].s[0] == 'o') {
            int pos = q.front();
            q.pop();
            update(pos, -1);
            --num;
        }
        else {
            now = num/2 + 1;
            printf("%d\n", query(1, n, 1));
        }
    }
    }
    return 0;
}*/
/*
long long a[10005];
int main() {
    //freopen("a.txt", "r", stdin);
    int T, c = 0, n;
    long long m, k;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%I64d%I64d", &n, &m, &k);
        for (int i = 0; i < n; ++i) scanf("%I64d", &a[i]);
        sort(a, a + n);
        printf("Case #%d:\n", ++c);
        if (m >= a[n - 1]) {
            printf("why am I so diao?\n");
            continue;
        }
        if (m < a[0]) {
            puts("madan!");
            continue;
        }
        int l = 0, r = n - 1, mid;
        int ans = -1;
        while (l <= r) {
            mid = (l + r) >> 1;
            if (a[mid] > m) r = mid - 1;
            else if (a[mid] <= m) {
                l = mid + 1;
                if (mid > ans) ans = mid;
            }
        }
        int i = ans;
        m = a[ans];
        bool can = true;
        do {
            long long t = m + k;
            if (t >= a[n - 1]) break;
            int now = i;
            while (i + 1 < n && a[i + 1] <= t)++i;
            if (i == now) {
                can = false;
                break;
            }
            if (k > 0) --k;
            else {
                if (m < a[n - 1]) {
                    can = false;
                    break;
                }
                else break;
            }
            m = a[i];
        } while (i < n - 1);
        if (can) puts("why am I so diao?");
        else puts("madan!");
    }
    return 0;
}
*/
/*
char ch;
int N, Q, lb[M<<2], rb[M<<2], mp[M], L, R, K;
inline void update(const int &rt) {
    if (lb[rt<<1] >= rb[rt<<1|1]) rb[rt] = rb[rt<<1], lb[rt] = lb[rt<<1|1] + (lb[rt<<1] - rb[rt<<1|1]);
    else lb[rt] = lb[rt<<1|1], rb[rt] = rb[rt<<1] + (rb[rt<<1|1] - lb[rt<<1]);
}
void build(const int &l, const int &r, const int &rt) {
    if (l == r) {
        ch = getchar();
        if (ch == '(')lb[rt] = 1, rb[rt] = 0;
        else lb[rt] = 0, rb[rt] = 1;
        mp[l] = rt;
        return ;
    }
    int m = (l + r) >> 1;
    build(lson);
    build(rson);
    update(rt);
}
void change(const int &p) {
    int rt = mp[p];
    swap(rb[rt], lb[rt]);
    while ((rt = rt>>1)) {
        update(rt);
    }
}
struct Point {
    int l, r;
    Point(const int & _r, const int & _l):l(_l), r(_r){}
};
Point query(const int &l, const int &r, const int &rt) {
    if (L <= l && r <= R) return Point(rb[rt], lb[rt]);
    int m = (l + r) >> 1;
    Point p = query(lson);

    return Point(1,2);

}
int main() {
    int T, op;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &N, &Q);
        getchar();
        build(1, N, 1);
        while (Q--) {
            scanf("%d", &op);
            if (op == '1') {
                scanf("%d", &K);
                change(K);
            }
            else {
                scanf("%d%d%d", &L, &R, &K);
                query(1, N, 1);
            }
        }
    }
    return 0;
}
*/
/*
int n, m, k;
int xk,yk,xn,yn1;
int mt[1005][1005];
int dx[] = {-2, -1, 1, 2, 2, 1, -1, -2};
int dy[] = {1, 2, 2, 1, -1, -2, -2, -1};
int getDis(const int x, const int y) {
    int dis1 = max(abs(x - xk), abs(y - yk));
    int dis2 = mt[x][y];
    if (dis2 == dis1) return dis1;
    if (dis2 > dis1) {
        //return dis2;
        if (dis1 == 0 && dis2 == 1) return 3;
        return dis2;
    }
    return dis1 + (dis1&1);
}
int bfs() {
    queue<pair<int, int> >q;
    q.push(make_pair(xn, yn1));
    int M = getDis(xn, yn1);
    while (!q.empty()) {
        pair<int,int> p = q.front(); q.pop();
        for (int i = 0; i < 8; ++i) {
            int x = p.first + dx[i];
            int y = p.second + dy[i];
            if (x < 1 || y < 1 || x > n || y > m) continue;
            if (mt[x][y] == -1) {
                mt[x][y] = mt[p.first][p.second] + 1;
                M = min(M, getDis(x, y));
                q.push(make_pair(x, y));
            }
        }
    }
    return M;
}
int main(){
    int T, c = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d%d", &n, &m, &k);
        scanf("%d%d%d%d", &xk, &yk, &xn,&yn1);
        memset(mt,-1, sizeof(mt));
        mt[xn][yn1] = 0;
        int t = bfs();
        printf("Case #%d:\n", ++c);
        if (t <= k)printf("%d\n", t);
        else puts("OH,NO!");
    }
    return 0;
}*/
/*
int extended_euclid(int a, int b, int &x, int &y)
{
     int d;
     if(b == 0) {x = 1;     y = 0;     return a;}
     d = extended_euclid(b, a % b, y, x);
     y -= a / b * x;
     return d;
}

int Inv(int a, int n)
{
     int d, x, y;
     d = extended_euclid(a, n, x, y);
     if(d == 1)	return (x%n + n) % n;
     else	return -1; // no solution
}
int mod = 1000000007;
int a[1000005];
int main() {
    int T, n ,cnt = 0;
    for (int i = 1; i <= 1000000; ++i)
        a[i] = Inv(i, mod);
    scanf("%d", &T);
    while(T--) {
        scanf("%d",&n);
        printf("Case #%d:\n",++cnt);
        if (n == 1) {
            puts("1");
            continue;
        }
        long long s = 1;
        long long l = n, r = (n&1)?n - 1 : n;
        long long t1 = l, t2 = r;
        while (t2) {
            s = (s*t1%mod)*a[t2]%mod;
            --t2, --t1;
        }
        long long sum = s;
        ++t1;
        t2 = r;
        while (t2) {
            s = (((s * t2 %mod) * (t2 - 1) %mod) * a[t1] % mod) * a[t1 + 1] % mod;
            sum = ((sum + 1) * s)% mod;
            t2 -= 2, t1 += 2;

        }
        printf("%I64d\n", sum);
    }
    return 0;
}*/
/*
double pi = acos(-1.0);
int main () {
    //freopen("a.txt","r", stdin);
    int T, n ,cnt = 0;
    scanf("%d", &T);
    while(T--) {
        scanf("%d",&n);
        printf("Case #%d:\n",++cnt);
        --n;
        long long a = 1;
        while (n--)
        {
            a<<=1;
            if (a>=1000000007)a%=1000000007;
        }
        printf("%I64d\n", a);
    }
    return 0;
}*/
/*
int main() {
    ifstream fin("D:\\Program Files (x86)\\CodeBlocks\\projects\\temp\\trialkey.txt");
    ofstream fout("D:\\Program Files (x86)\\CodeBlocks\\projects\\temp\\test.txt");
    int a, b, c, cnt= 0;
    string s;
    while (fin>>a>>s>>b>>c) {
        if (c == 1) {
            ++cnt;
            fout<<s<<":"<<b<<endl;
        }

    }
    fin.close();
    fout.close();
    //printf("%d\n", cnt);
    return 0;
}
*/
/*
struct node {
    int model, speaker, channel;
    string train;
    node(int _m, string _t, int _c, int _s) {model = _m, train = _t, channel = _c, speaker = _s;}
};
vector<node> v;
int Find(const int &m) {
    int l = 0, r = v.size() - 1, mid;
    while (l < r) {
        mid = (l + r) >> 1;
        if (v[mid].model == m) return mid;
        else if (v[mid].model > m) r = mid - 1;
        else l = mid + 1;
    }
    return l;
}
set<int> st;
int main() {
    ifstream fin("D:\\Program Files (x86)\\CodeBlocks\\projects\\temp\\modelkey.txt");
    string t;
    int m, s, c;
    while (fin>>m>>t>>c>>s) {
        v.push_back(node(m, t, c, s));
    }
    fin.close();
    ifstream fin2("D:\\Program Files (x86)\\CodeBlocks\\projects\\temp\\trialkey.txt");
    ofstream fout("D:\\Program Files (x86)\\CodeBlocks\\projects\\temp\\testplan1.txt");
    ofstream fout2("D:\\Program Files (x86)\\CodeBlocks\\projects\\temp\\model.txt");
    int re, idx, cnt = 0;
    int sz = v.size() - 1, j;
    while (fin2>>m>>t>>c>>re) {
        if (re == 1) {
            idx = Find(m);
            if (idx == -1) {puts("error!"); break;}
            else {
                ++cnt;
                fout<<t<<":"<<c<<" "<<v[idx].train<<":"<<v[idx].channel;
                fout2<<m<<" "<<v[idx].model;
                st.clear();
                for (int i = 0; i < 10; ++i) {
                    while (true) {
                        j = (int)((float)rand()/RAND_MAX * sz);
                        if (v[j].speaker == v[idx].speaker || st.count(v[j].model)) continue;
                        fout<<" "<<v[j].train<<":"<<v[j].channel;
                        fout2<<" "<<v[j].model;
                        st.insert(v[j].model);
                        break;
                    }
                }
                fout<<endl;
                fout2<<endl;
            }
        }
    }
    printf("%d\n", cnt);
    fin2.close();
    fout.close();
    fout2.close();
    return 0;
}
*/
/*
int main() {
    freopen("C:\\Users\\Thyme\\Desktop\\folder\\trial-keys\\NIST_SRE08_short2-short3.trial.key","r",stdin);
    freopen("trialkey.txt", "w", stdout);
    string s;
    getline(cin, s);
    int a;
    char b[1000], c[1000], ch;
    while (scanf("%d,%[^,],%c,%[^,]%*s", &a, b, &ch, c)!=EOF) {
        printf("%d %s %d %d\n", a, b, ch == 'a'?1:2, c[0] == 'n'?0:1);
    }
    return 0;
}
*/
/*
int main() {
    string s;
    freopen("C:\\Users\\Thyme\\Desktop\\folder\\model-keys\\NIST_SRE08_short2.model.key","r",stdin);
    freopen("modelkey.txt", "w", stdout);
    getline(cin, s);
    int a, b;
    char c[1000], ch;
    while (scanf("%d,%*c,%[^:]:%c,%d%*s", &a, c, &ch, &b)!=EOF) {
        printf("%d %s %d %d\n", a, c, ch == 'a'?1:2, b);
    }
    return 0;
}
*/
/*
int main() {
    freopen("C:\\Users\\Thyme\\Desktop\\folder\\segment-keys\\test\\NIST_SRE08_short3.test.segment.key","r",stdin);
    freopen("segmentkey.txt", "w", stdout);
    string s;
    getline(cin, s);
    int a;
    char b[1000], c[1000], d[1000], ch;
    while (scanf("%[^,],%*[^,],%*[^,],%*[^,],%*[^,],",b)!=EOF) {
        printf("%s", b);
        scanf("%[^:]:%[^:]:%*s", c, d);
        if (c[0] == 'N') {
           scanf(" %[^:]%*s\n", c);
            printf(" -1 %s\n", c);
        }
        else {
            if (d[0] == 'm') {
                getchar();
                printf(" %s -1\n", c);
            }
            else {
                printf(" %s", c);
                scanf(" %[^:]%*s\n", c);
                if (c[0] != 'N')printf(" %s\n", c);
                else printf(" -1\n");
            }

        }
    }
    return 0;
}
*/
/*
vector<string> v;
int main ()
{
    string s;
    getline(cin, s);
    char ch;
    int i = 0, j = s.size();
    while (i <j) {
        if (isalpha(s[i])) {
            int k = i, l = i;
            while (k + 1 < j && isalpha(s[k + 1])) ++k;
            i = k + 1;
            v.push_back(s.substr(l,k - l + 1));
        }
        ++i;
    }
    j = v.size(), i = j - 1;
    while (i>=0) {
        if (i == j-1) cout<<v[i];
        else cout<<" "<<v[i];
        --i;
    }
    cout<<endl;
    return 0;
}*/
