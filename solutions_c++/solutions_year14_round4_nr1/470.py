#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;

#define num(i,N) for(int i=0; i < (N); ++i)
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#if __cplusplus > 199711L
#define tr(c,i) for(auto i=(c).begin(); i != (c).end(); ++i)
#else
#define tr(c,i) for(typeof((c).begin()) i=(c).begin(); i != (c).end(); ++i)
#endif
#define has(c,x) ((c).find(x) != (c).end())

// Cut begin
#define DEBUG(x) cout<<"#"<<__LINE__<<": "<<#x<<" = "<<x<<endl;
template <class T> ostream& operator<<(ostream &out, const vector<T> &v) {
    out<<"["; num(i,sz(v)) out<<(i?", ":"")<<v[i]; return out << "]"; }
template <class T, class K> ostream& operator<<(ostream &out, const map<K,T> &m) {
    out<<"{"; tr(m,it) out<<(it==m.begin()?"":", ")<<it->first<<":"<<it->second;
    return out << "}"; }
template <class T> ostream& operator<<(ostream &out, const set<T> &s) {
    out<<"{"; tr(s,it) out<<(it==s.begin()?"":", ")<<*it; return out<<"}"; }
template <class T, class K> ostream& operator<<(ostream &out, const pair<K,T> &p) {
    return out<<"("<<p.first<<", "<<p.second<<")"; }
template <class T> void vprint(vector<T> v, int W=1) { cout<<"[\n";
    num(i,sz(v)) { if (i%W==0) cout<<"\n  "; cout<<v[i]<<", "; } cout<<"\n]\n"; }
// Cut end

bool solve() {
    int N, X;
    cin >> N >> X;
    vector<int> s(N);
    tr(s,it) cin>>(*it);
    sort(all(s));

    int i=0, j=s.size()-1, count=0;
    while (j>=i) {
        if (s[i]+s[j] <= X || i==j) {
            //DEBUG(mp(s[i], s[j]));
            j--; i++;
        } else {
            //DEBUG(s[j]);
            j--;
        }
        count ++;
    }
    printf("%d\n", count);
    return true;
}

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        if (!solve()) break;
    }
}

// vim: set ff=unix ai tw=80 ts=4 sts=4 sw=4 et:
