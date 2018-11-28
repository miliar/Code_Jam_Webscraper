#include <vector>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <fstream>
#include <iomanip>
#include <cstring>

using namespace std;

#define PRINT(x) cout << "DEBUG " << #x << " = " << x <<  endl;

#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i = 0; i < (n); i++)
#define frr(i, n) for(int i = 0; i < (n); i++)
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef istringstream ISS;
typedef ostringstream OSS;
typedef long long ll;

int N, M;
string a[100];
int ans, ansCount;
int assign[100];

void read(ifstream &fin) {
 fin >> M >> N;
 frr(i, M)
  fin >> a[i];
}

void check() {
 int nodes = 0;

 frr(i, N) {
  set<string> s;
  frr(j, M) {
   if(assign[j] != i) continue;
   frr(k, sz(a[j]))
    s.insert(a[j].substr(0, k + 1));
  }

  if(sz(s) == 0)
   return;
  nodes += sz(s) + 1;
 }

 if(nodes > ans) {
  ans = nodes;
  ansCount = 1;
 } else if(nodes == ans) {
  ansCount++;
 }
}

void rec(int m) {
 if(m == M) {
  check();
  return;
 }

 frr(i, N) {
  assign[m] = i;
  rec(m + 1);
 }
}

void proc(ofstream &fout) {
 ans = 0;
 rec(0);
 fout << ans << " " << ansCount << endl;
}

int main() {
 int i;
 int NT;

 ifstream fin("in");
 ofstream fout("out");
 string ln;

 getline(fin, ln);
 istringstream is(ln);
 is >> NT;

 fr(i, NT)
 {
  read(fin);
  fout << "Case #" << i + 1 << ": ";
  cout << "Case #" << i + 1 << endl;
  proc(fout);
 }

 return 0;
}
