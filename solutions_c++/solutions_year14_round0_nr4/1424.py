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

int N;
vector<double> a, b;

void read(ifstream &fin) {
 double v;
 fin >> N;
 a.clear();
 b.clear();

 frr(i, N) {
  fin >> v;
  a.pb(v);
 }

 frr(i, N) {
  fin >> v;
  b.pb(v);
 }
}

int calc(vector<double> x, vector<double> y) {
 sort(all(x));
 sort(all(y));

 int i = N - 1, j = N - 1;
 int r = 0;

 while(i >= 0 && j >= 0) {
  if(x[i] < y[j])
   r++, i--, j--;
  else
   i--;
 }

 return r;
}

void proc(ofstream &fout) {
 fout << calc(b, a) << " " << N - calc(a, b) << endl;
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
