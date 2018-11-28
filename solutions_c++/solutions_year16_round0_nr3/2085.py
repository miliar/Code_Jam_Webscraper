#define _CRT_SECURE_NO_WARNINGS
#include <cctype>
#include <climits>
#include <cmath>
#include <cstring>
#include <deque>
#include <fstream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <bitset>
#include <numeric>
#include <ratio>
#include <regex>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <valarray>

using namespace std;

#define sz(v) (int)v.size()
#define eps 1e-10
#define all(v) v.begin(), v.end() 
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define chk(a,k) ((bool)(a&(1<<(k))))
#define set0(a,k) (a&(~(1<<(k))))
#define set1(a,k) (a|(1<<(k)))
#define in(v, x) (find(all(v),x) != v.end()) 
#define re return
#define sum(v) accumulate(v.begin(),v.end(),(ld)0)
#define tr(v,it) for(auto it=v.begin();it != v.end();it++)
#define asrt(v) sort(v.begin(),v.end())
#define dsrt(v) sort(v.rbegin(),v.rend())
#define rev(v) reverse(v.begin(),v.end())
#define pi 3.1415926535897932384626433832795
#define MOD 1000000007
#define print(v) for (auto& i:v) cout<<i<<endl 
#define endl '\n'

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<string> vs;
typedef vector<vi> vvi;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<string> vs;
typedef vector<vi> vvi;

#define print "Case #"+to_string(t1)+": " 

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<string> vs;
typedef vector<vector<int>> vvi;

int rem[11];



bool divides(string s, int base, int x) {

	int rem=1,pow=base,res=0;
	for(int i=sz(s)-1; i>=0; i--) {
		if(s[i]=='1') res+=rem;
		res%=x;
		rem*=base;
		rem%=x;
	}
	if(res==0) re 1;
	re 0;
}



bool ok(string s) {
	vi v {2,3,5,7,11,13,17,19,23,29,31,37,39,41},res;
	for(int i=2; i<11; i++) {
		bool f=0;
		for(int j=0; j<sz(v); j++) {
			if(divides(s, i, v[j])) {
				res.push_back(v[j]);
				f=1;
				break;
			}
		}
		if(!f) re 0;
	}
	cout<<s<<" ";
	for(int i=0; i<sz(res); i++) {
		cout<<res[i]<<" ";
	}
	cout<<endl;
}

int main() {
	freopen("Data/in.txt", "r", stdin);
	freopen("Data/out.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t1=1; t1<=T; t1++) {
		ll N,J;
		cin>>N>>J;

		cout<<print<<endl;
		set<string> M;
		while(J>0) {
			string s="1";
			for(int i=2; i<N; i++) {
				int r=rand()%2;
				if(r==0) s+="0";
				else s+="1";
			}
			s+="1";

			if(M.find(s)!=M.end()) continue;
			M.insert(s);

			if(ok(s)) {
				J--;
			}

		}

	}
	getchar();
	return 0;
}
