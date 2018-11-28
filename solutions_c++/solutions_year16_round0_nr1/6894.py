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
vector<int>_ans;


void solve(){
	int n;
	cin>>n;
	if(n == 0){
		 _ans._pb(-1);
		 return;
	}
	bool digits[10];
	rep(i,0,10){
		digits[i] = false;
	}
	int mul = 1;
	while(true){
		int m=mul*n;
		while(m!=0){
			digits[m%10]=true;
			m/=10;
		}
		bool flag = true;
		rep(i,0,10)flag= flag && digits[i];
		if(flag){
			_ans._pb(mul*n);
			break;
		}
		else mul++;
	}
}
void printAns(){
	int n= _ans.size();
	rep(i,0,n){
		if(_ans[i] != -1)
		printf("\nCase #%d: %d", i+1, _ans[i]);
		else 
		printf("\nCase #%d: INSOMNIA", i+1);
	}
}

int main(){
	int t;
	cin>>t;
	rep(i,0,t){
		solve();
	}
	printAns();

  return 0;
}

