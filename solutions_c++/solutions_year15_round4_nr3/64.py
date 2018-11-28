#include <bits/stdc++.h>

#define FO(i,a,b) for (long long i = (a); i < (b); i++)
#define sz(v) int(v.size())

using namespace std;

namespace MF {
    const long long N = 10000, M = 5000*500;
    long long f[N], e[2*M], c[2*M], fl[2*M], nxt[2*M], ce;
    long long n, s, t;
    long long Q[N], lvl[N];
    long long le[N];

    void init(long long _n) {
        n = _n+2; s = _n; t = _n+1; ce = 0;
        FO(i,0,n) f[i]=-1;
    }

    void add(long long a, long long b, long long cap) {
        nxt[ce]=f[a]; f[a]=ce; e[ce]=b; fl[ce]=0; c[ce]=cap; ce++;
        nxt[ce]=f[b]; f[b]=ce; e[ce]=a; fl[ce]=0; c[ce]=0; ce++;
    }

    bool bfs() {
        FO(i,0,n) lvl[i]=-1;
        long long qi = 1;
        Q[0] = s; lvl[s] = 0;
        FO(i,0,qi) {
            long long x=Q[i];
            le[x]=f[x];
            for (long long j=f[x];j>=0;j=nxt[j]) if (c[j]-fl[j]>0) {
                long long y=e[j];
                if (lvl[y]==-1) {
                    lvl[y]=lvl[x]+1;
                    Q[qi++]=y;
                }
            }
        }
        return lvl[t]!=-1;
    }

    long long aug(long long cu, long long f) {
        if (cu == t) return f;
        for (long long &i=le[cu];i>=0;i=nxt[i]) if (c[i]-fl[i]>0) {
            long long x=e[i];
            if (lvl[x]!=lvl[cu]+1) continue;
            long long rf = aug(x,min(f,c[i]-fl[i]));
            if (rf>0) {
                fl[i]+=rf;
                fl[i^1]-=rf;
                return rf;
            }
        }
        lvl[cu]=-1;
        return 0;
    }

    long long mf() {
        long long tot = 0;
        while (bfs())
            for (long long x=aug(s,1e14);x;x=aug(s,1e14)) tot+=x;
        return tot;
    }
};

char buf[100000];
vector<string> rdsent() {
    gets(buf);
    istringstream is(buf);
    string w;
    vector<string> v;
    while(is >> w) {
        v.push_back(w);
    }
    return v;
}

int main() {
    long long T; scanf("%lld", &T);
    FO(Z,1,T+1) {
        long long n;
        scanf(" %lld ", &n);
        vector<vector<string> > v(n);
        FO(i,0,n) v[i] = rdsent();
        map<string,long long> w;
        for (auto x : v) for (auto y : x) if (!w.count(y)) {
            long long nv = sz(w);
            w[y] = nv;
        }
        MF::init(n + 2*sz(w));
        FO(i,0,sz(w)) {
            MF::add(MF::s, 2*i, 1);
            MF::add(2*i+1, MF::t, 1);
            MF::add(2*i,2*i+1, 1);
        }
        MF::add(MF::s, 2*sz(w)+0, 10000000000000ll);
        MF::add(2*sz(w)+1, MF::t, 10000000000000ll);
        FO(i,2,n) {
            MF::add(MF::s, 2*sz(w)+i, 100000000ll);
            MF::add(2*sz(w)+i, MF::t, 100000000ll);
        }
        FO(i,0,n) {
            for (auto x : v[i]) {
                MF::add(2*sz(w)+i, 2*w[x]+1, 10000000000000ll);
                MF::add(2*w[x], 2*sz(w)+i, 10000000000000ll);
            }
        }
        printf("Case #%lld: %lld\n", Z, MF::mf() - 100000000ll*(n-2) - sz(w));
    }
}

