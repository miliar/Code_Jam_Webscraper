#include <bits/stdc++.h>//{{{
#define all(x) begin(x),end(x)
#define rall(x) (x).rbegin(),(x).rend()
#define REP(i,b,n) for(int i=(int)(b);i<(int)(n);++i)
#define rep(i,n) REP(i,0,n)
#define repsz(i,v) rep(i,(v).size())
#define aur auto&
#define bit(n) (1LL<<(n))
#define eb emplace_back
#define mt make_tuple
#define fst first
#define snd second
using namespace std;
typedef long long ll;
//#define int long long
template<class C>int size(const C &c){ return c.size(); }
template<class T>bool chmin(T&a,const T&b){if(a<=b)return false;a=b;return true;}
template<class T>bool chmax(T&a,const T&b){if(a>=b)return false;a=b;return true;}//}}}
template<typename T> T s_to(string s){ //{{{
    stringstream ss;
    T res;
    ss << s;
    ss >> res;
    return res;
} //}}}

// Allocator//{{{
template<typename T>
struct Allocator{//{{{
    private:
        struct Handler{//{{{
            Handler(){ Allocator::constructor(); }
            ~Handler(){ Allocator::destructor(); }
        };//}}}

        using Ptr = T *;
        static vector<Ptr> pool;
        static vector<size_t> sizes;
        static vector<Ptr> frees;

        static inline void constructor(){ allocate(1024); }
        static inline void destructor(){ for(auto &p : pool) ::operator delete(p); }

        static inline Ptr get(const bool &clear = false){//{{{
            static Handler h;
            static size_t i = 0, p = 0;
            if(clear){ i = p = 0; return nullptr; }
            if(!frees.empty()){
                Ptr res = frees.back(); frees.pop_back();
                return res;
            }
            if(p == sizes[i]) if(++i == sizes.size()){
                p = 0;
                allocate(sizes.back() * 2);
            }
            return &pool[i][p++];
        }//}}}
        static inline void reserve(const size_t &n){ allocate(n); }
        static inline void allocate(const size_t &n){//{{{
            pool.emplace_back(static_cast<Ptr>(::operator new(n * sizeof(T))));
            sizes.emplace_back(n);
        }//}}}
    public:
        static void *operator new(size_t size){
            return static_cast<void *>(get());
        }
        template<typename Arg, typename ...Args>
            static void *operator new(size_t size, Arg arg, Args ...args){
                return ::operator new(size, arg, args...);
            }
        static void operator delete(void *ptr){
            frees.emplace_back(static_cast<Ptr>(ptr));
        }
        static void clear_allocated(){ get(true); }
};//}}}
template<typename T> vector<T*> Allocator<T>::pool;
template<typename T> vector<size_t> Allocator<T>::sizes;
template<typename T> vector<T*> Allocator<T>::frees;
//}}}

template<typename Node>
struct RBST{//{{{
    static inline unsigned int xor128(){//{{{
        static unsigned int x=129042, y=38923212, z=3829312, w=3893189;
        unsigned int t=x^(x<<11);
        x=y;y=z;z=w;
        return w=(w^(w>>19))^(t^(t>>8));
    }//}}}
    static inline int rnd(int m){ return xor128() % m; }

    using Ref = Node *;
    static inline int size(Ref u){ return u == nullptr ? 0 : u->size; }

    static inline Ref update(Ref u){ return u->update(); }
    static inline Ref remove_ch(Ref u, int dir, bool need_update = true){//{{{
        Ref c = u->ch(dir);
        if(c != nullptr){
            u->ch(dir) = c->p = nullptr;
            if(need_update) update(u);
        }
        return c;
    }//}}}
    static inline Ref add_ch(Ref u, int dir, Ref c, bool need_update = true){//{{{
        remove_ch(u, dir, false);
        if((u->ch(dir) = c) != nullptr) c->p = u;
        return need_update ? update(u) : u;
    }//}}}
    static Ref join(Ref l, Ref r){//{{{
        if(l == nullptr or r == nullptr) return l == nullptr ? r : l;
        if(rnd(size(l) + size(r)) < size(l)){
            l->r = join(l->r, r);
            if(l->r != nullptr) l->r->p = l;
            return update(l);
        }else{
            r->l = join(l, r->l);
            if(r->l != nullptr) r->l->p = r;
            return update(r);
        }
    }//}}}
    static Ref join(initializer_list<Ref> us){//{{{
        Ref res = nullptr;
        for(Ref u : us) res = join(res, u);
        return res;
    }//}}}

    // [*, u), [u, *)
    static pair<Ref, Ref> split_l(Ref u){//{{{
        Ref l = remove_ch(u, 0), r = u;
        for(Ref p = u->p; p; u = p, p = p->p){
            if(p->l == u) r = add_ch(p, 0, r);
            else          l = add_ch(p, 1, l);
        }
        return make_pair(l, r);
    }//}}}
    // [*, u], (u, *)
    static pair<Ref, Ref> split_r(Ref u){//{{{
        Ref l = u, r = remove_ch(u, 1);
        for(Ref p = u->p; p; u = p, p = p->p){
            if(p->l == u) r = add_ch(p, 0, r);
            else          l = add_ch(p, 1, l);
        }
        return make_pair(l, r);
    }//}}}
    // [*, u), u, (u, *]
    static pair<Ref, Ref> split_lr(Ref u){//{{{
        Ref l = remove_ch(u, 0), r = remove_ch(u, 1);
        for(Ref p = u->p; p; u = p, p = p->p){
            if(p->l == u) r = add_ch(p, 0, r);
            else          l = add_ch(p, 1, l);
        }
        return make_pair(l, r);
    }//}}}
    static Ref root(Ref u){//{{{
        while(u->p) u = u->p;
        return u;
    }//}}}

    static int index(Ref u){//{{{
        int res = size(u->l);
        for(; u->p; u = u->p) if(u->p->r == u) res += size(u->p->l) + 1;
        return res;
    }//}}}
};//}}}
struct ETT{//{{{
    struct Node : Allocator<Node>{//{{{
        using Ref = Node *;
        Ref l, r, p;
        int size;
        Ref &ch(int dir){ return dir > 0 ? r : l; }

        Ref rev;
        Node() : l(nullptr), r(nullptr), p(nullptr), size(1), rev(nullptr) {
            update();
        }
        Ref update(){
            size = (l ? l->size : 0) + 1 + (r ? r->size : 0);
            return this;
        }
    };//}}}

    using Tree = RBST<Node>;
    using Ref  = Tree::Ref;

    vector<Ref> vs;
    unordered_map<ll, Ref> es;

        ETT(const int &n){
            vs.resize(n);
            rep(u, n) vs[u] = new Node();
        }
    ~ETT(){ for(auto &p : vs) delete p; }

    void add_edge(int u, int v){//{{{
        if(u > v) swap(u, v);
        const ll key = ((ll)(u)<<32) | v;

        Ref ul, ur; tie(ul, ur) = Tree::split_l(vs[u]);
        Ref vl, vr; tie(vl, vr) = Tree::split_l(vs[v]);
        Ref uv = new Node(), vu = new Node();
        uv->rev = vu; vu->rev = uv;
        Tree::join({ul, uv, vr, vl, vu, ur});
        es[key] = uv;
    }//}}}
    void remove_edge(int u, int v){//{{{
        if(u > v) swap(u, v);
        const ll key = ((ll)(u)<<32) | v;
        assert(es[key] != nullptr);

        Ref uv = es[key], vu = uv->rev;
        es.erase(key);
        if(Tree::index(vu) < Tree::index(uv)) swap(uv, vu);
        // A-uv-B-vu-C   =>   C-A, B
        Ref A, B, C;
        tie(A, B) = Tree::split_lr(uv);
        tie(B, C) = Tree::split_lr(vu);
        Tree::join(C, A);
    }//}}}
    bool has_edge(int u, int v){//{{{
        if(u > v) swap(u, v);
        const ll key = ((ll)(u)<<32) | v;
        return es.count(key);
    }//}}}

    int get_size(int u){
        int res = Tree::size(Tree::root(vs[u]));
        return (res + 2) / 3;
    }
};//}}}

bool solve(){
    int n, D; cin >> n >> D;
    vector<ll> ss;
    vector<int> par(n);
    ETT ett(n);
    {//{{{
        vector<ll> ms;
        ll s0, as, cs, rs; cin >> s0 >> as >> cs >> rs;
        ss.eb(s0);
        rep(i, n-1) ss.eb((ss.back() * as + cs) % rs);
        ll m0, am, cm, rm; cin >> m0 >> am >> cm >> rm;
        ms.eb(m0);
        rep(i, n-1) ms.eb((ms.back() * am + cm) % rm);
        rep(i, n) if(i) par[i] = ms[i] % i;
    }//}}}
    vector<int> idx(n); rep(i, n) idx[i] = i;
    sort(all(idx), [&](const int &i, const int &j){ return ss[i] < ss[j]; });
    int r = 0;
    int res = 0;
    rep(l, n){
        //cout << "l = " << l << "(" << idx[l] << ")" << endl;
        while(r < n and ss[idx[r]] <= ss[idx[l]] + D){
            if(idx[r] != 0){
                ett.add_edge(idx[r], par[idx[r]]);
        //      cout << "link " << idx[r] << " to " << par[idx[r]] << endl;
            }
            ++r;
        }
        if(ss[idx[l]] <= ss[0] and ss[0] <= ss[idx[l]] + D){
        //  cout << "chmax " << ett.get_size(0) << endl;
            chmax(res, ett.get_size(0));
        }
        if(idx[l] != 0)ett.remove_edge(idx[l], par[idx[l]]);
    }
    cout << res << endl;
    return true;
}
signed main(){
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cout << std::fixed << std::setprecision(10);
    string s;
    getline(cin, s);
    int T = s_to<int>(s);
    rep(i, T){
        cout << "Case #" << (i+1) << ": ";
        solve();
    }
    return 0;
}
// vim:set foldmethod=marker commentstring=//%s:
