#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()
#define clr(X) memset(X,0,sizeof(X));
#define xx first
#define yy second
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;

bool valid(vector<int> P, int n) {
	for(int i=0;i<sz(P);i++) 
		if(2*P[i] > n) return false;
	return true;
}

vector<string> solve(vector<int> P, int n) {
	/*
  printf("AQUI %d: ",n);
	for(int i=0;i<sz(P);i++)
		cout << P[i] << " ";
	cout << endl;
  */ 
	vector<string> ret;
	if(n==0) { 
		return ret;
	}
	if(!valid(P,n)) {
		ret.pb("IMPOSSIBLE");
		return ret;
	}
	for(int i=0;i<sz(P); i++) {
		if(P[i]==0) continue;
		P[i]--;
		vector<string> child = solve(P,n-1);
		P[i]++;
		if(sz(child)>0 && child[0] == "IMPOSSIBLE") {
			continue;
		}
		string s = "";
		s += 'A' + i;
		ret = child;
		ret.pb(s); 
		return ret;
	}
	
	for(int i=0;i<sz(P); i++) {
		for(int j=i; j< sz(P); j++) {
		  if(P[i]==0 || P[j]==0) continue;
		  if(i==j && P[i] == 1) continue;
			P[i]--;
			P[j]--;
		  vector<string> child = solve(P,n-2);
		  P[i]++;
			P[j]++;
		  if(sz(child)>0 && child[0] == "IMPOSSIBLE") {
			  continue;
		  }
			string s = "";
		  s += 'A' + i;
			s += 'A' + j;
			ret = child;
			ret.pb(s);
			return ret;
		}
	}
	ret.pb("IMPOSSIBLE");
	return ret;
}

int main(){
	int T;
	scanf("%d", &T);
	for(int caso=1;caso<=T;caso++) {
		int n;
		cin >> n;
		vector<int> P;
		int s = 0;
		for(int i=0;i<n;i++) {
			int x;
			cin >> x;
			s += x;
			P.pb(x);
		}
		vector<string> v = solve(P,s);
		printf("Case #%d:", caso);
		for(int i=sz(v)-1;i>=0;i--)
			cout << " " << v[i];
		cout << endl;
	}
	return 0;
}
