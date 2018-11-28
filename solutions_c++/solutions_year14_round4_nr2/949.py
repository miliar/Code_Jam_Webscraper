#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string.h>
#include <strings.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <math.h>
#include <cmath>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <climits>
//#include <unordered_set>
//#include <unordered_map>
#include <assert.h>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> int2;
typedef pair<float, float> float2;
typedef pair<ull, ull> ull2;

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(s,i) for ( __typeof((s).begin()) i = ((s).begin())   ; i != (s).end(); ++i)  
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mp(a,b) make_pair(a,b)
#define del(s,x) if(s.find(x)!=s.end()) s.erase(s.find(x))

#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)

bool comp(pair<int,int> a,pair<int,int> b) {return a.first < b.first; }

int IMP = 100000;

int main() {
  //ios_base::sync_with_stdio(0);
  int T;
  cin >> T;
  cout.precision(12);
  FOR (test, 1, T+1) {
    int n;
    cin >> n;
    vector<ll> tab(n);
    FOR(i,0,n) cin >> tab[i];

    vector<pair<ll,int> > tabs(n);;
    FOR(i,0,n) tabs[i] = mp(tab[i],i);
    sort(all(tabs));
    int cpt = 0;
    FOR(i,0,n) {
      int cpt1 = 0, cpt2 = 0;
      FOR(j,0,n) {
	if (j < tabs[i].second && tab[j] > tabs[i].first) {
	  cpt1++;
	} else if (j > tabs[i].second && tab[j] > tabs[i].first) {
	  cpt2++;
	}
      }
      //cout << tabs[i].first << " " << cpt1 << " " << cpt2 << endl;
      cpt += min (cpt1, cpt2);
    }
    
    cout << "Case #" << test << ": " << cpt << endl;
  }
  return 0;
}
