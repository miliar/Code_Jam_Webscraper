#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef vector<long long> vll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define mset(arr,val)  memset(arr,val,sizeof(arr))
#define tr(i,c)  for(auto i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define forr(var,from,to) for(int var=(from);var<=(to);var++)
#define found(s,e)  ((s).find(e)!=(s).end())
#define remove_(c,val) (c).erase(remove((c).begin(),(c).end(),(val)),(c).end())
#define lastc(str) (*((str).end()-1))

//#include "cout11.h"

int main()
{
  int _T; cin >> _T; // 1-100
  for (int _t=1; _t<=_T; ++_t) {
  	int N; cin >> N;
  	vector<int> m(N);
  	rep(i,N) cin >> m[i];
  	//cout << m << endl;
  	int a1=0;
  	int dmax = 0;
  	rep(i,N-1){
  		if (m[i] <= m[i+1]) continue;
  		int d = m[i] - m[i+1];
  		a1 += d;
  		dmax = max(d,dmax);
  	}
  	int a2=0;
  	rep(i,N-1){
  		int d = min(dmax, m[i]);
  		a2 += d;
  	}

 answer:
    cout << "Case #" << _t << ": " << a1 << " " << a2 << endl;
  }
}
