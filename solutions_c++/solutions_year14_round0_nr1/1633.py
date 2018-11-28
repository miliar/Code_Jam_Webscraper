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

int a[20];

void read(ifstream &fin) {
 int n, x;

 frr(i, 20)
  a[i] = 0;

 frr(k, 2) {
  fin >> n;
  frr(i, 4) {
   frr(j, 4) {
    fin >> x;
    if(n == i + 1)
     a[x - 1]++;
   }
  }
 }
}

void proc(ofstream &fout) {
 int c = 0;
 int ans = -1;

 frr(i, 20) {
  if(a[i] == 2) {
   ans = i + 1;
   c++;
  }
 }

 if(c == 0)
  fout << "Volunteer cheated!" << endl;
 else if(c > 1)
  fout << "Bad magician!" << endl;
 else
  fout << ans << endl;
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
