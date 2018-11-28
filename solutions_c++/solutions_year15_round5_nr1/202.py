#include <bits/stdc++.h>
using namespace std;
const int N = 2000010;

/*
vector<int> E[N];
void add_edge(int a, int b)
{
        cout << a <<" " << b<< endl;
        E[a].push_back(b);
}

struct Tree
{
        int c[N];
        int n;
        void init(int n) {
                this->n = n + 1;
                memset(c, 0, sizeof(c));
        }
        void update(int x, int v) {
                for(x; x <= n; x += x&-x) {
                        c[x] += v;
                }
        }
        void update(int l, int r, int v) {
                update(l, v);
                update(r + 1, -v);
        }
        int sum(int x) {
                int s = 0;
                for(;x; x-=x&-x) {
                        s += c[x];
                }
                return s;
        }
}tree;

int tot, id[N];
int dep[N], L[N], R[N];
void dfs(int u, int f)
{
        L[u] = ++tot;
        for(int v: E[u]) {
                dep[v] = dep[u] + 1;
                dfs(v, u);
        }
        R[u] = tot;
}
bool vis[N], del[N];
#define wuyiqi
*/
const int inf = ~0u >> 2;
struct Node* null;
struct Data
{
        int lc, rc;
        int ls, rs;
        int sum[2];
        void init(int c, int cnt) {
                lc = rc = c;
                ls = rs = cnt;
                sum[0] = !c, sum[1] = c;
        }
};
inline Data operator + (const Data& l, const Data& r)
{
        Data ret;
        ret.sum[0] = l.sum[0] + r.sum[0];
        ret.sum[1] = l.sum[1] + r.sum[1];
        ret.lc = l.lc == -1 ? r.lc : l.lc;
        ret.rc = r.rc == -1 ? l.rc : r.rc;
        ret.ls = l.ls, ret.rs = r.rs;
        int lm = 0, rm = 0;
        if(!r.sum[!ret.rc] && l.rc == ret.rc) lm = r.rs + l.rs;
        if(!l.sum[!ret.lc] && r.lc == ret.lc) rm = l.ls + r.ls;
        ret.ls = std::max(ret.ls, rm);
        ret.rs = std::max(ret.rs, lm);
        return ret;
}
struct Node
{
        Node* ch[2];
        Node* fa;
        inline int sgn(){return fa->ch[0]==this?0:fa->ch[1]==this?1:-1;}
        inline void setc(int s, Node* who){who->fa=this;ch[s]=who;}
        inline void rotate() {
                int a=sgn(),b=fa->sgn(); 
                Node* y=fa; y->setc(a,ch[!a]),fa=y->fa;
                if(~b) fa->ch[b]=this;
                this->setc(!a,y),y->up();
        }
        inline void splay() {
                for(int a,b;~(a=sgn());rotate()) 
                        if(~(b=fa->sgn()))
                                (a^b)?rotate():fa->rotate();
                up();
        }
        Data data;
        int s[2], col;
        inline void up() {
                data.init(col, s[col] + 1);
                data = ch[0]->data + data;
                data = data + ch[1]->data;
        }
        void init(Node* f) {
                fa = f;
                ch[0] = ch[1] = null;
                col = 1;
                s[0] = s[1] = 0;
                data.init(1, 1);
        }
};
struct Link_Cut_Tree 
{
        Node node[N]; 
        Node* access(Node* u) {
                Node* v = null;
                for(; u != null; v = u, u = u->fa) {
                        u->splay();
                        if(u->ch[1] != null) {
                                u->s[u->ch[1]->data.lc] += u->ch[1]->data.ls;
                        }
                        if(v != null) {
                                u->s[v->data.lc] -= v->data.ls;
                        }
                        u->ch[1] = v;
                        u->up();
                }
                return v;
        }
        int query(int v) {
                Node* u = node + v;
                Node* root = access(u);
                if(v == 1) {
                        return root->data.ls;
                } else {
                        return root->data.rs;
                }
        }
        void update(int v) {
                Node* u = node + v;
                access(u);
                u->splay();
                u->col ^= 1;
                u->up();
        }
}lct;
int head[N], nxt[N * 2], pnt[N * 2];
int E;
void add_edge(int a, int b)
{
        a++; b++;
     //   printf("a=%d b=%d\n", a, b);
        pnt[E] = b;
        nxt[E] = head[a];
        head[a] = E++;
}
void dfs(int u, int f = -1) 
{
        if(f == -1) {
                lct.node[u].init(null);
        } else {
                lct.node[u].init(lct.node + f);
        }
        for(int i = head[u]; i != -1; i = nxt[i]) {
                int v = pnt[i];
                if(v == f) {
                        continue;
                }
                dfs(v, u);
                lct.node[u].s[1] += lct.node[v].data.ls;
        }
        lct.node[u].up();
}

int color[N], id[N];
int S[N], M[N];

void fileinput()
{
        freopen("A-large.in", "r", stdin);
        freopen("out.txt", "w", stdout);
}
int main()
{
        int __size__ = 256<<20;
	char *__p__ = (char *)malloc(__size__)+__size__;
	__asm__("movl %0,%%esp\n"::"r"(__p__));
        fileinput();
        null = new Node();
        null->ch[0] = null->ch[1] = null->fa = null;
        null->s[0] = null->s[1] = 0; 
        null->data.lc = null->data.rc = -1;
        null->data.ls = null->data.rs = 0;
        null->data.sum[0] = null->data.sum[1] = 0;
        int t, ca = 1, n, D;
        scanf("%d", &t);
        while(t--) {
                scanf("%d%d", &n, &D);
                E = 0;
                fill(head, head + n + 1, -1);
                fill(color, color + n + 1, 0);
                int As, Cs, Rs;
                int Am, Cm, Rm;
                cin >> S[0] >> As >> Cs >> Rs;
                cin >> M[0] >> Am >> Cm >> Rm;
                id[0] = 0;
                for(int i = 1; i < n; i++) {
                        id[i] = i;
                        S[i] = (1LL*S[i-1]*As + Cs) % Rs;
                        M[i] = (1LL*M[i-1]*Am + Cm) % Rm;
                        add_edge(M[i]%(i), i);
                }
                dfs(1);
                sort(id, id + n, [](int i, int j) {
                                return S[i] < S[j];
                                });
                int pt = 0;
                int ret = 0;
                for(int i = 0;  i < n; i++) {
                        int u = id[i];
                        color[u] ^= 1;
                        lct.update(u + 1);
                        while(pt < i && S[u] - S[id[pt]] > D) {
                                color[id[pt]] ^= 1;
                                lct.update(id[pt] + 1);
                                pt++;
                        }
                        if(color[0] == 1) {
                                int tmp = lct.query(1);
                                if(tmp > ret) ret = tmp;
                        }
                }
                printf("Case #%d: %d\n", ca++, ret);
        }
        return 0;
}
