#include <bits/stdc++.h>
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define _mp make_pair
#define _pi pair<int,int>
#define _pb push_back
#define _vi vector<int>
#define _vvi vector<vector<int> >
#define _vpi vector<pair<int,int> >
#define _eb emplace_back
#define _mt make_tuple

#define what_is(x) cout << #x << " is " << x << endl
typedef long long int lli;
using namespace std;
_vi _ans;
int f[105][2];
void solve(){
	string s;
	cin>>s;
	if(s[0] == '+'){
		f[0][1] = 0;
		f[0][0] = 1;
	}
	else{
		f[0][1] = 1;
		f[0][0] = 0;
	}
	int n=s.length();
	rep(i,1,n){
		if(s[i] == '+'){
			f[i][1]= min(f[i-1][1], f[i-1][0]+2);
			f[i][0] = min(f[i-1][1]+1, f[i-1][0]+2);
		}
		else {
			f[i][0]= min(f[i-1][0], f[i-1][1]+2);
			f[i][1] = min(f[i-1][0]+1, f[i-1][1]+2);
		}
	}
	_ans._pb(f[n-1][1]);
}

void printAns(){
	int n= _ans.size();
	rep(i,0,n){
		printf("\nCase #%d: %d", i+1,_ans[i]);
	}
}
int main(){
 	int t; 
	cin>>t;
	rep(i,0,t)solve();
	printAns();
  return 0;
}

