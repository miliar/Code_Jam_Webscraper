#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define EACH(it,a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); ++it)

#define DEBUG(x) { cerr << #x << " = "; cerr << (x) << endl; }
#define PR(a,n) { cerr << #a << " = "; FOR(_,1,n) cerr << a[_] << ' '; cerr << endl; }
#define PR0(a,n) { cerr << #a << " = "; REP(_,n) cerr << a[_] << ' '; cerr << endl; }

#define sqr(x) ((x) * (x))
#define TWO(X) (1<<(X))
#define CONTAIN(S,X) (S & TWO(X))
using namespace std;

bitset<2500> eng, fre, either[211];
int n;

char tmp[1000111];
map<string,int> id;
bitset<2500> read() {
    gets(tmp);
    istringstream ss(tmp);
    vector<int> res;
    string s;
    while (ss >> s) {
        if (id.count(s)) res.push_back(id[s]);
        else {
            int t = id.size() + 1;
            id[s] = t;
            res.push_back(t);
        }
    }
    bitset<2500> t;
    for(int x : res) t.set(x);
    return t;
}

int main(int argc, char** argv) {
    ios :: sync_with_stdio(false);
    int ntest; scanf("%d\n", &ntest);
    FOR(test,1,ntest) {
        scanf("%d\n", &n);
        id.clear();
        eng = read();
        fre = read();
        FOR(i,1,n-2) either[i] = read();

        int res = 1000111;
        REP(mask,TWO(n-2)) {
            bitset<2500> can_eng = eng;
            bitset<2500> can_fre = fre;

            REP(i,n-2) {
                if (CONTAIN(mask,i)) can_eng |= either[i+1];
                else can_fre |= either[i+1];
            }

            res = min(res, (int) (can_eng & can_fre).count());
        }
        cout << "Case #" << test << ": " << res << endl;
    }
    return 0;
}

