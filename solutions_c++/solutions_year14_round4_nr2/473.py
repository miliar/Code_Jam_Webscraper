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
    int N;
    cin >> N;
    vector<int> v(N);
    tr(v,it) cin>>(*it);

    vector<int> s=v;
    sort(all(s));

    map<int,int> pos;
    num(i,N) pos[v[i]]=i;

    int left = 0, right = N-1;

    int steps = 0;
    num(i,N-1) {
        int p = pos[s[i]];
        if (p-left < right-p) {
            steps += p-left;
            for (int j=p-1; j>=left; j--) {
                swap(pos[v[j]],pos[v[j+1]]);
                swap(v[j],v[j+1]);
            }
            left++;
        } else {
            steps += right-p;
            for (int j=p+1; j<=right; j++) {
                swap(pos[v[j]],pos[v[j-1]]);
                swap(v[j],v[j-1]);
            }
            right--;
        }
    }
    printf("%d\n", steps);

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
