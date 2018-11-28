#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <utility>
#include <functional>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <deque>
 
using namespace std;
 
#define rep(i,n) REP(i,0,n)
#define REP(i,s,e) for(int i=(s); i<(int)(e); i++)
#define pb push_back
#define mp make_pair
#define all(r) r.begin(),r.end()
#define rall(r) r.rbegin(),r.rend()
#define fi first
#define se second
#define println(X) cout<<X<<endl;
#define DBG(X) cout<<#X<<" : "<<X<<endl;
 
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vl;
typedef vector<vl> vll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;


const int INF = 1e9;

double EPS = 1e-10;

int main(){
	int mCase;
	scanf("%d", &mCase);
	char c[150];
	int idx, ans;
	for(int Case = 1; Case <= mCase; Case++){
		scanf("%s", c);
		vector<int> v(strlen(c), 1);
		for(int i = (int)(v.size())-2; i>=0; i--){
			if(c[i+1]==c[i]){
				v[i]+=v[i+1];
			}
		}
		idx = v[0];
		ans = 0;
		while(idx < (int)v.size()){
			idx+=v[idx];
			ans++;
		}
		if(c[0]=='-' && ans%2==0) ans++;
		else if(c[0]=='+' && ans%2==1) ans++;
		printf("Case #%d: %d\n", Case, ans);
	}
}