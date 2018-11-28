#include <cctype>
#include <climits>
#include <cmath>
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>
#include <numeric>
#include <ratio>
#include <regex>
#include <string>
#include <tuple>
#include <utility>
#include <valarray>

using namespace std;

#define _CRT_SECURE_NO_WARNINGS
#define INF ULLONG_MAX
#define MIN LLONG_MIN
#define pi 3.1415926535897932384626433832795

#define sz(v) v.size()
#define pb(x) push_back(x)
#define re return
#define sum(v) accumulate(v.begin(),v.end(),0)
#define asrt(v) sort(v.begin(),v.end())
#define dsrt(v) sort(v.rbegin(),v.rend())
#define rev(v) reverse(v.begin(),v.end())
#define str to_string
#define print(v) for (auto& i:v) cout<<i<<endl
#define print "Case #"+to_string(t1)+": " 

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<string> vs;
typedef vector<vector<int>> vvi;

string prod(string s1,char  s2) {
	string s="";
	if(sz(s1)==2) {
		s+="-";
		string s3="";
		s3+=s1[1];
		s1=s3;
	}
	if(s1=="1") re s+s2;
	if(s1=="i"){
		if(s2=='1') re s+"i";
		if(s2=='i') re s+"-1";
		if(s2=='j') re s+"k";
		if(s2=='k') re s+"-j";
	}
	if(s1=="j"){
		if(s2=='1') re s+"j";
		if(s2=='i') re s+"-k";
		if(s2=='j') re s+"-1";
		if(s2=='k') re s+"i";
	}
	if(s1=="k"){
		if(s2=='1') re s+"k";
		if(s2=='i') re s+"j";
		if(s2=='j') re s+"-i";
		if(s2=='k') re s+"-1";
	}
}

string dp[10000];

int main() {
	freopen("Data/B.txt", "r", stdin);
	freopen("Data/B1.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t1=1; t1<=T; t1++) {
		int L,X;
		cin>>L>>X;
		string s;
		cin>>s;
		string o=s;
		for(int i=1; i<X; i++) {
			s+=o;
		}
		int n=sz(s);
		dp[0]=s[0];
		for(int i=1; i<n; i++) {
			string x=prod(dp[i-1], s[i]);
			if(sz(x)==3) {
				string cpy="";
				cpy+=x[2];
				x=cpy;
			}
			dp[i]=x;
		}
		if(dp[n-1]!="-1") {
			cout<<print<<"NO"<<endl;
		} else{
			bool f=false;
			for(int i=0; i<n; i++) {
				if(dp[i]=="i") {
					for(int j=i+1; j<=n; j++) {
						if(j==n) break;
						if(dp[j]=="k") {
							f=true;
						}
					}
				}
			}
			if(f) cout<<print<<"YES"<<endl;
			else cout<<print<<"NO"<<endl;
		}
	}
	getchar();
	return 0;
}
