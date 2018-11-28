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

int main() {
    int T;
    R(T);

    for (int t=1; t<=T; t++) {
        int n, mask = (1<<10)-1;
        R(n);

        printf("Case #%d: ", t);
        if (!n) {
            puts("INSOMNIA");
            continue;
        }
        int now=0;
        do {
            now += n;
            for (int x=now; x; x/=10)
                mask &= ~(1<<(x%10));
        } while (mask);

        printf("%d\n", now);

    }
    return 0;
}
