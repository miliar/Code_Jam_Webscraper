#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <queue>
#include <cstring>
#include <string>
#include <complex>
#include <unordered_map>
#include <valarray>

#define vi vector<int>
#define vpii vector< pair<int,int> >
#define pii pair<int,int>
#define mp(x,y) make_pair(x,y)
#define all(x) (x).begin(),(x).end()
#define FOREACH(it,x) for (auto it = (x).begin(); it!=(x).end(); ++it) 
#define sz(x) (int)(x).size()
#define FOR(i,n) for (ll i = 0; i < ll(n); i++)
#define ROF(i,n) for (ll i = ((ll)n-1); i >= 0; i--)
#define FOR1(i,n) for (ll i = 1; i < ll(n); i++)
#define REP(i,a,b) for (ll i = a; i < ll(b); i++)
#define READ(a) int a; scanf("%d", &a);
#define READV(v,n) vi v(n);FOR(i,n){scanf("%d", &v[i]);}
#define WRITE(v) FOR(i,sz(v))cout<<v[i]<<" ";
#define gmin(a,b) { if (b < a) a = b; }
#define gmax(a,b) { if (b > a) a = b; }
#define pb push_back
#define ff first
#define ss second
#define oo ((1LL<<62)+((1LL<<31)-1))
#define MOD 1000000007ll
const double PI = std::atan(1.0)*4;

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

void so(string &a){
	if(a.length()==1){
		return;
	}
	string b = a.substr(0, a.length()/2);
	string c = a.substr(a.length()/2);
	so(b); so(c);
	if(b>c) swap(b,c);
	a = b+c;
}

int main(int argc, char *argv[]){
	READ(T);
	FOR(t,T){
		READ(n);
		vi v(3);
		cin>>v[0]>>v[1]>>v[2];
		FOR(i, 3){
			vector<int> w, tmp;
			w.pb(i);

			FOR(z, n){
				tmp.clear();
				FOR(i, sz(w)){
					tmp.pb(w[i]);
					tmp.pb((w[i]+2) % 3);
				}
				w=tmp;
			}

			vi v2(3,0);
			FOR(i, sz(w)){
				v2[w[i]]++;
			}
			if(v[0]==v2[0] && v[1]==v2[1] && v[2]==v2[2]){
				cout<<"Case #"<<(t+1)<<": ";
				stringstream ss;
				FOR(i, sz(w)){
					if(w[i]==0) ss<<"R";
					if(w[i]==1) ss<<"P";
					if(w[i]==2) ss<<"S";
				}
				string s = ss.str();
				so(s);
				cout<<s<<endl;
				goto next;
			}
		}
		cout<<"Case #"<<(t+1)<<": IMPOSSIBLE"<<endl;
		next: continue;
	}
	return 0;
}