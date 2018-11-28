#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <deque>
#include <queue>
#include <bitset>
#include <stack>
#include <set>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iomanip> 
#include <ctime>
using namespace std;

#define sz size()
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define inf 1000000000
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define pi 2*acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second 

typedef vector<int> vint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii; 
const int INF=~(1<<31);
const double eps=1e-6;
 
const long double PI = 3.1415926535;
 
int main() {
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
  int T;
  cin>>T;
  FOR(t,1,T){
	  printf("Case #%d: ",t);
	int n,m;
	cin>>n>>m;
	vector<vint> a(n+2,vint(m+2,0));
	rep(i,n)rep(j,m)cin>>a[i][j];
	int fal=0;
	int x=0,y=0;
	rep(i,n)if((x&y)==0)rep(j,m){
		x=0;y=0;
		rep(k,n)if(k!=i && a[k][j]>a[i][j])x=1;
		rep(k,m)if(k!=j && a[i][k]>a[i][j])y=1;
		if(x&y){
			break;
		}
		
	}
		
		
	if(x&y)puts("NO"); else puts("YES");
  }
  return 0;
}
