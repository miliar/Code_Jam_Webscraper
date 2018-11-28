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
int a[10000];
int temp[10000];
int dp[2000][2000];

void read(ifstream &fin) {
 fin >> N;
 frr(i, N)
  fin >> a[i];
}

int cal(int s, int e) {
 if(s == e) return 0;
 int &ans = dp[s][e];
 if(ans != -1) return ans;

 int n = N - (e - s + 1);
 int p = 0;
 frr(i, N) {
  if(a[i] > n) p++;
  if(a[i] == n) break;
 }
 ans = cal(s + 1, e) + p;

 p = 0;
 for(int i = N - 1; i >= 0; --i) {
  if(a[i] > n) p++;
  if(a[i] == n) break;
 }
 ans = min(ans, cal(s, e - 1) + p);

 return ans;
}

void proc(ofstream &fout) {
 frr(i, N)
  temp[i] = a[i];
 sort(temp, temp + N);
 frr(i, N) frr(j, N)
  if(a[j] == temp[i])
   a[j] = i;

 _rs(dp);

 fout << cal(0, N - 1) << endl;
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
