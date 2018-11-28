#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define f(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define fiter(it,con) for(auto (it)=(con).begin(); (it)!=(con).end();++(it))
#define x first
#define y second

using namespace std;

typedef pair<int,int> pii;
typedef pair<long long, long long> pll;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<bool> vb;

int score(char a, char b) {
	if(a==b) return 10;
	return 5;
}

int ans(vector<vi>& memo, string& s, int f, int t) {
	//cerr<<f<<' '<<t<<endl;
	if(t<=f) return 0;
	if (memo[f][t]!= -1){
		//cerr<<"looukp\n";
		return memo[f][t];
	}
	int best = 0;
	for(int i=f+1;i<t;i+=2) {
		best= max(best,score(s[f],s[i])+ans(memo,s,f+1,i)+ans(memo,s,i+1,t));
	}
	memo[f][t]=best;
	//cerr<<"update\n";
	return best;
}

int main() {
	int t;
	cin>>t;
	f(cas,1,t+1) {
		string s;
		cin>>s;
		int n=s.length();
		vector< vector<int> > memo;
		memo = vector< vector<int> >(n);
		f(i,0,n) {
			memo[i] = vector<int>(n+1,-1);
		}
		cout<<"Case #"<<cas<<": "<<ans(memo,s,0,n);
		cout<<'\n';
	}
	return 0;
}
