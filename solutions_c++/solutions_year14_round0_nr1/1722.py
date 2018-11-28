#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <set>
#include <map>
#include <iomanip>

#define fr(i,n) for(i=0;i<(int)(n);i++)
#define fit(a,b) for(typeof(b.begin()) a = b.begin(); a != b.end(); a++)
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define SZ(u) ((int)u.size())
#define WT(x) cout << #x << ": " << x << endl

using namespace std;

typedef long long ll;
typedef pair<int,int> p2;
typedef vector<int> vi;
typedef long double ld;

void check(set<int>& pos) {
	int n, i, j, x;
	cin >> n;
	fr (i, 4) fr(j, 4) {
		cin >> x;
		if (i + 1 != n) pos.erase(x);
	}
}

int main() {
  int tc, cn = 0;
  cin >> tc;
  while (cn++ < tc) {
    set<int> pos;
	int i;
	for (i = 1; i <= 16; ++i) pos.insert(i);
	check(pos);
	check(pos);
	cout << "Case #" << cn << ": ";
  	if (SZ(pos) > 1) cout << "Bad magician!" << endl;
	else if (SZ(pos) == 0) cout << "Volunteer cheated!" << endl;
	else cout << *pos.begin() << endl;
  }
  return 0;
}
