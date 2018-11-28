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

const int NORTH = 1;
const int WEST= 2;
const int SOUTH = 4;
const int EAST = 8;

int R, C;
int a[110][110];
int v[110][110];

void read(ifstream &fin) {
 string s;

 fin >> R >> C;
 frr(r, R) {
  fin >> s;
  frr(c, C) {
   if(s[c] == '^') a[r][c] = NORTH;
   if(s[c] == '>') a[r][c] = WEST;
   if(s[c] == 'v') a[r][c] = SOUTH;
   if(s[c] == '<') a[r][c] = EAST;
   if(s[c] == '.') a[r][c] = 0;
  }
 }
}

int calc() {
 _cl(v);

 frr(r, R) {
  frr(c, C) if(a[r][c]) {
   v[r][c] |= EAST;
   break;
  }
  for(int c = C - 1; c >= 0; --c) if(a[r][c]) {
   v[r][c] |= WEST;
   break;
  }
 }
 frr(c, C) {
  frr(r, R) if(a[r][c]) {
   v[r][c] |= NORTH;
   break;
  }
  for(int r = R - 1; r >= 0; --r) if(a[r][c]) {
   v[r][c] |= SOUTH;
   break;
  }
 }

 int change = 0;
 frr(r, R) frr(c, C) if(a[r][c]) {
  if(v[r][c] == 15) return -1;
  if(v[r][c] & a[r][c]) change++;
 }

 return change;
}

void proc(ofstream &fout) {
 int r = calc();
 if(r < 0)
  fout << "IMPOSSIBLE" << endl;
 else
  fout << r << endl;
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
