#include <iostream>
#include <vector>
#include <map>
#include <fstream>
#define LL long long
#define ABS(a) (((a) > 0) ? (a) : (-(a)))
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FOR1(i, n) for(int i=1; i<=(n);++i)
#define FORIT(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define all(o) (o).begin(), (o).end()
#define pb push_back
#define mp make_pair
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
#define MOD 1000000007
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> pii;
template<typename T> ostream& operator<<(ostream& s, vector<T>& v)
{ s << '{'; for (int i = 0 ; i < v.size(); ++i) s << (i ? "," : "") << v[i]; return s << '}'; }
template<typename S, typename T> ostream& operator<<(ostream &s, pair<S,T>& p)
{ return s << "(" << p.first << "," << p.second << ")"; }

string word[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int num[10] = {0, 2, 4, 6, 8, 1, 3, 5, 7, 9};
int main() {
	int TC; cin >> TC;
	FOR1(tc, TC) {
		map<char, int> m;
		string s;
		cin >> s;
		FOR(i, s.size()){
			m[s[i]]++;
		}
	
		int j = 0;
		int k = 0;
		vi ret;
			while (k < 10) {
			j = num[k];
			string w = word[j];
			bool tf = true;
			map<char, int> mm = m;
			FOR(i, w.size()) {
				if (mm[w[i]] <= 0) {
					tf = false;
					break;
				} else {
					mm[w[i]]--;
				}
			}
			if (tf) {
				ret.pb(j);
				m = mm;
			} else {
				k++;
			}
		}
		sort(ret.begin(), ret.end());
		cout << "Case #" << tc << ": ";
		FOR(i, ret.size()) cout << ret[i];
		cout << endl;

	}
}
