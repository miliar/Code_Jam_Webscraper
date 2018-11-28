#include <cstdio>
#include <iostream>
#include <string>
#include <map>

#define FOR(i,a,b) for(int i(a); i <= b; ++i)
#define FORD(i,a,b) for(int i(a); i >= b; --i)
#define REP0(i,n) FOR(i,0,n-1)
#define REP1(i,n) FOR(i,1,n)
#define PU push_back
#define PO pop_back
#define MP make_pair
#define A first
#define B second
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define SZ(s) (int)((s).size())
#define CL(a) memset((a),0,sizeof(a))
#define MAX(X,Y) X = max((X),(Y))
#define MIN(X,Y) X = min((X),(Y))
#define FORIT(X,Y) for(typeof((Y).begin()) X=(Y).begin(); X!=(Y).end(); ++X)
#define VI vector <int>
#define ll long long
#define PII pair<int,int>
#define PDD pair<double,double>
#define INF 1000000000

using namespace std;

map<char, map<char, char> > table;
map<char, map<char, int> > sign;

void setup() {
    table['1']['1'] = '1';
    table['1']['i'] = 'i';
    table['1']['j'] = 'j';
    table['1']['k'] = 'k';
    table['i']['1'] = 'i';
    table['i']['i'] = '1';
    table['i']['j'] = 'k';
    table['i']['k'] = 'j';
    table['j']['1'] = 'j';
    table['j']['i'] = 'k';
    table['j']['j'] = '1';
    table['j']['k'] = 'i';
    table['k']['1'] = 'k';
    table['k']['i'] = 'j';
    table['k']['j'] = 'i';
    table['k']['k'] = '1';

    sign['1']['1'] = 1;
    sign['1']['i'] = 1;
    sign['1']['j'] = 1;
    sign['1']['k'] = 1;
    sign['i']['1'] = 1;
    sign['i']['i'] = -1;
    sign['i']['j'] = 1;
    sign['i']['k'] = -1;
    sign['j']['1'] = 1;
    sign['j']['i'] = -1;
    sign['j']['j'] = -1;
    sign['j']['k'] = 1;
    sign['k']['1'] = 1;
    sign['k']['i'] = 1;
    sign['k']['j'] = -1;
    sign['k']['k'] = -1;
}
int L, X, N;
string S;
int lookup(char c, char f, int s) {
    int pos = 1;
    do {
        if (s >= N)
            return -1;
        s++;
        char fp = table[f][S[s%L]];
        pos *= sign[f][S[s%L]];
        f = fp;
    } while (f != c || pos == -1);
//    printf("%c %d\n", f, s);
    return s;
}
int T;
void solve() {
  T++;
  cin >> L >> X >> S;
  N = L*X;
  printf("Case #%d: ", T);
  int si = -1, sj, sk;
  char ci = '1';
  char cj = '1';
  char ck = '1';

    si = lookup('i',ci,si);
    if (si==-1 || si > N-3) {
        cout << "NO" << endl;
        return;
    }
    ci = 'i';
    sj = lookup('j',cj,si);
    if (sj==-1 || sj > N-2) {
        cout << "NO" << endl;
        return;
    }
    cj = 'j';
    sk = sj;
    do {
        sk = lookup('k',ck,sk);
        ck = 'k';
    } while (sk!=-1 && sk!=N-1);
    if (sk==-1) {
        cout << "NO" << endl;
        return;
    }
    if (sk==N-1) {
        cout << "YES" << endl;
        return;
    }

}

int main() {
//  freopen("C.in", "r", stdin);
  setup();
  int T;
  cin >> T;
  while (T-->0) solve();
  return 0;
}
