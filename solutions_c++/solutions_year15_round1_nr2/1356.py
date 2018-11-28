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

ll gcd(ll a, ll b) { while(a) swap(a, b%=a); return b; }

int main()
{
  int _T; cin >> _T; // 1-100
  for (int _t=1; _t<=_T; ++_t) {
  	int B; cin >> B;
  	ll N; cin >> N; --N;
  	vector<int> M(B);
  	ll C = 1LL;
  	rep(i,B) {
  		int m; cin >> m;
  		M[i] = m;
  		ll g = gcd((ll)m, C);
  		C = C / g * m;
  	}
  	// cout << "C=" << C << endl;
  	priority_queue<pair<int,int> > pq;
  	ll mc = 0LL;
  	rep(i,B){
  		for (int t=0; t<C; t+=M[i]) {
  			pq.push(pair<int,int>(-t,-i));
  			mc += 1;
  		}
  	}
  	//cout << N << " " << mc << " " << N%mc << endl;
  	N %= mc;
  	int n=0, ans=-1;
 	while(!pq.empty()){
  		// int t = -pq.top().first;
  		int b = -pq.top().second;
  		pq.pop();
  		//cout << n << " " << b << endl;
  		if (n == N) { ans = b; break; }
  		++n;
  	}
 answer:
    cout << "Case #" << _t << ": " << (1+ans) << endl;
  }
}
