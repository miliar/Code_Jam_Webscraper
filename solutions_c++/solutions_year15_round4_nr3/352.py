#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define rep(i,s,e) for (int i=(s);i<(e);++i)
#define pb push_back
#define mk make_pair
#define fst first
#define snd second
#define all(x) (x).begin(),(x).end()
#define clr(x,y) memset(x,y,sizeof x)
#define contains(x,y) (x).find(y)!=(x).end()
#define endl "\n"
#define test(j) ((i >> j) % 2)

int dx[]={0,0,1,-1,1,-1,1,-1}, dy[]={-1,1,0,0,1,-1,-1,1};
const int mod = 1e9+7;

int isect(set<int> &s1, set<int> &s2) {
  return count_if(all(s1), [&](int i) { return s2.find(i) != s2.end(); });
}

int main() {
	ios::sync_with_stdio(0);
	cout << fixed << setprecision(16);

	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ti++) {
		cout << "Case #" << ti << ": ";
    cerr << ti << endl;
    int n;
    cin >> n; cin.ignore();
    unordered_map<string, int> idx;
    vector<set<int>> sentences(n);
    rep(i,0,n) {
      while (cin.peek() != '\n') {
        string w;
        cin >> w;
        if (!idx.count(w))
          idx[w] = idx.size() - 1;
        sentences[i].insert(idx[w]);
      }
      cin.ignore();
    }
    int res = INT_MAX;
    rep(i, 0, (1 << n)) {
      if (test(0) && !test(1)) {
        int val = 0;
        vector<bool> eng(idx.size()), fr(idx.size());
        rep (j,0,n) {
          if (test(j)) for (int k : sentences[j]) eng[k] = true;
          else for (int k : sentences[j]) fr[k] = true;
        }
        //for (auto &p : idx)
        //  cerr << p.first << p.second << " ";
        rep (j,0,idx.size()) {
          //cerr << eng[j] << fr[j] << " ";
          if (eng[j] && fr[j]) {
            val++;
          }
        }
        //cerr << val << " " << i << endl;
        res = min(res, val);
      }
    }
    cout << res << endl;
  }
}
