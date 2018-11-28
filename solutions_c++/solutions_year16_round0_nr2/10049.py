#include <bits/stdc++.h>
#define isNum(c) c<='9' && c>='0'
#define islettre(c) c<='z' && c>='a'
#define isLETTRE(c) c<='Z' && c>='A'
#define MS0(x) memset(x,0,sizeof(x))
#define MS(x,s) memset(x,s,sizeof(x))
#define rep(i,n) for(i=0;i<n;i++)
#define repv(i,v) for(i=0;i<v.size();i++)
#define repa(i,a,n) for(i=a;i<n;i++)
#define all(c) c.begin(),c.end()
#define rall(c) c.rbegin(),c.rend()
#define NOT_VISITED 0
#define IS_VISITED 1
#define MOD 1000000009
#define INF 1000000009
#define COL 100002
#define trMap(c,i) for(map<char,int>::iterator i = (c).begin(); i != (c).end(); i++)
#define trSet(c,i) for(set< pair <int,char> >::iterator i = (c).begin(); i != (c).end(); i++)
#define PB(val) push_back(val)
#define MP(f,s) make_pair(f,s)
#define abs(i) (i<0)?-i:i
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector< ii > vii;

map<string, int> DP;

int allG(string s){
	int i;
	rep(i,s.size()){
		if(s[i] == '-') return 0;
	}
	return 1;
}

string rev(string s){
	string res = s;
	int i;
	rep(i,s.size()){
		if(s[i] == '-') res[i] = '+';
		else res[i] = '-';
	}
	reverse(all(res));
	return res;
}

int solve(string s){
	if(allG(s)) return 0;

	int & ret = DP[s];

	if(ret)
		return ret;


	int m1,m2;
	ret = MOD*2;
	int i,j;
	rep(i,s.size()){
		string r = s;
		string rv = s.substr(0,i+1);
		rv = rev(rv);
		repv(j,rv){
			r[j] = rv[j];
		}

		ret = min(ret,solve(r)+1);
	}
	if(s[s.size()-1] == '+') ret = min(ret,solve(s.substr(0,s.size()-1)));
	return ret;
}

int main(){
	int T,i,j,k;
	cin >> T;
	string s;
	rep(i,T){
		DP = map<string,int>();
		cin >> s;
		cout << "Case #" << (i+1) << ": " << solve(s) << endl; 
	}
}