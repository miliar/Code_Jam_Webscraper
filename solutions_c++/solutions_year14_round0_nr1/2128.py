#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <utility>
#include <set>
#include <map>
#include <cctype>

#define FOR(i,n) for(long long int i=0; i<n; i++)
#define MP(a,b) make_pair(a,b)
#define PB(x) push_back(x)
#define SORT(a) sort(a.begin(), a.end())
#define REV(a) reverse(a.begin(), a.end())

#define COND(p,t,f) ((p)?(t):(f))

#define PI 3.14159265

using namespace std;
typedef long long int lint;
typedef unsigned long long int ulint;



int main() {
  int T;
  cin >> T;
  FOR(t,T) {
    int r1,r2;
    int m1[4][4];
    int m2[4][4];
    cin >> r1;
    r1--;
    FOR(i,4) FOR(j,4) cin >> m1[i][j];
    cin >> r2;
    r2--;
    FOR(i,4) FOR(j,4) cin >> m2[i][j];
    set<int> s1;
    FOR(i,4) s1.insert(m1[r1][i]);
    int cnt = 0, num;
    FOR(i,4) {
      if (s1.find(m2[r2][i])!= s1.end()) {
	cnt++;
	num=m2[r2][i];
	//cerr << "N: " << num << endl;
      }
    }
    //cerr << cnt;
    cout << "Case #" << t+1 << ": ";
    if (cnt==1) cout << num << endl;
    if (cnt==0) cout << "Volunteer cheated!" << endl;
    if (cnt>1) cout << "Bad magician!" << endl;
    
  }
  
}