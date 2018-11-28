#include<algorithm>
#include<bitset>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define X first
#define Y second 
#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
typedef vector<int> VI;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.X << ", " << pair.Y << ")";}

typedef pair<char, int> PP;

const int N = 16;
int n;
PP t[N];

const int INF = 1e9;
int best = INF;

bool cmpX(PII a, PII b) {
    return a.X < b.X;
}

bool cmpY(PII a, PII b) {
    return a.Y < b.Y;
}

int mm[N];
void match(int i) {
    if (i == n) {
        REP(j, n) if (t[j].Y != 0 || (mm[j] != -1 && t[mm[j]].Y != 0)) {
            int x;
            if (t[j].Y != 0) x = t[j].Y;
            else x = t[mm[j]].Y;

            vector< PII > v;
            REP(l, n) {
                if (t[l].Y == x) {
                    if (mm[l] == -1) {
                        if (t[l].X == 'E') v.PB(MP(l,INF));
                        else v.PB(MP(-1, l));
                    } else {
                        if (t[l].X == 'E') {
                            v.PB(MP(l, mm[l]));
                        } else {
                            if (t[mm[l]].Y == 0) {
                                v.PB(MP(mm[l],l));
                            }
                        }
                    }
                }
            }

            sort(ALL(v), cmpX);
            REP(i, SZ(v)) {
                if (i < SZ(v) - 1) {
                    if (v[i].Y == INF) return;
                    if (v[i].Y > v[i+1].X) return;
                }
            }
        }

        int curr = 0;
        REP(j, n) {
            if (t[j].X == 'E' && mm[j] == -1) ++curr;
        }
/*
        if (curr < best) {
            debug(curr);
            REP(j, n) debug(MP(t[j], mm[j]));
        }
*/
        mini(best, curr);

        return;
    }
    match(i+1);
    if (t[i].X == 'L') return;

    FOR(j, i+1, n-1) {
        if (mm[j] >= 0) continue;
        if (t[j].X == 'E') continue;
        if (t[i].Y != 0 && t[j].Y != 0 && t[i].Y != t[j].Y) continue;

        mm[i] = j;
        mm[j] = i;
        match(i+1);
        mm[i] = -1;
        mm[j] = -1;
    }
}

void solve(int tc) {
    scanf("%d", &n);
    REP(i, n) scanf(" %c %d", &t[i].X, &t[i].Y);

    REP(i, n) mm[i] = -1;
    best = INF;
    match(0);
    
    printf("Case #%d: ", tc);
    if (best == INF) {
        printf("CRIME TIME\n");
    } else {
        printf("%d\n", best);
    }

}

int main(){
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);

    int t; scanf("%d", &t);
    REP(i, t) solve(i+1);
    
    return 0;
}

