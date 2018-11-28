// {{{
#include <bits/stdc++.h>
#define MP make_pair
#define PB push_back
#define ALL(x) begin(x),end(x)
#define SZ(x) ((int)x.size())
#define REP(i,n) for(int i=0;i<n;i++)
#define REP2(i,a,b) for(int i=a;i<=b;i++)
using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;

#ifdef FEI
template<typename T>
void _dump(const char* s, T&& head) { cerr<<s<<"="<<head<<endl; }
template<typename T, typename... Args>
void _dump(const char* s, T&& head, Args&&... tail) {
    int c=0;
    while (*s!=',' || c!=0) {
        if (*s=='(' || *s=='[' || *s=='{') c++;
        if (*s==')' || *s==']' || *s=='}') c--;
        cerr<<*s++;
    }
    cerr<<"="<<head<<", ";
    _dump(s+1, tail...);
}

#define dump(...) do { \
    fprintf(stderr, "%s:%d - ", __PRETTY_FUNCTION__, __LINE__); \
    _dump(#__VA_ARGS__, ##__VA_ARGS__); \
} while(0);

template<typename Iter>
ostream& _out(ostream &s, Iter b, Iter e) {
    s<<'[';
    for (auto it=b; it!=e; it++) s<<(it==b?"":",")<<*it;
    s<<']';
    return s;
}

template<typename A, typename B>
ostream& operator <<(ostream &s, const pair<A,B> &p) { return s<<"("<<p.first<<","<<p.second<<")";}
template<typename T>
ostream& operator <<(ostream &s, const vector<T> &x) { return _out(s,ALL(x)); }
template<typename T, size_t N>
ostream& operator <<(ostream &s, const array<T,N> &x) { return _out(s,ALL(x)); }
template<typename T>
ostream& operator <<(ostream &s, const set<T> &x) { return _out(s,ALL(x)); }
template<typename A, typename B>
ostream& operator <<(ostream &s, const map<A,B> &x) { return _out(s,ALL(x)); }
#else
#define dump(...)
#endif

template<typename T>
void _R(T &x) { cin>>x; }
void _R(int &x) { scanf("%d",&x); }
void _R(LL &x) { scanf("%" PRId64,&x); }
void _R(double &x) { scanf("%lf",&x); }
void _R(char &x) { scanf(" %c",&x); }
void _R(char *x) { scanf("%s",x); }

void R(){}
template<typename T, typename... X>
void R(T& head, X&... tail) { _R(head); R(tail...); }
// }}}

const int SQN = 50, N = SQN*SQN;
bool np[N];
int p[N] = {2}, pc = 1;

int main() {
    for (int i=3; i<N; i+=2)
        if (!np[i]) {
            p[pc++] = i;
            if (i < SQN) for (int j=i*i; j<N; j+=i) np[j] = 1;
        }

    int T;
    R(T);

    for (int t=1; t<=T; t++) {
        int n, m;
        R(n, m);

        printf("Case #%d:\n", t);

        int x = (1<<(n-1))+1, mask = (1<<n)-1;

        for ( ; x!=mask && m; x+=2) {
            int ans[11]={};
            for (int base=2; base<=10; base++) {
                LL val = 0;
                for (int i=n-1; i>=0; i--)
                    val = val*base+((x>>i)&1);

                for (int i=0; i<pc; i++)
                    if (val%p[i] == 0) {
                        ans[base] = p[i];
                        break;
                    }
                if (!ans[base]) break;
            }
            if (!ans[10]) continue;

            for (int i=n-1; i>=0; i--)
                printf("%d", (x>>i)&1);
            for (int i=2; i<=10; i++)
                printf(" %d", ans[i]);
            puts("");
            m--;
        }
    }
    return 0;
}
