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
using namespace std;
typedef long long int lli;
void solve(int x){
	int Smax;
	cin>>Smax;
	string s;
	cin>>s;
	int ns,add;
	ns=add=0;
	ns=s[0]-'0';
	rep(i,1,Smax+1){
		if(ns>=i){
			ns+=s[i]-'0';
		}
		else{
			add+=i-ns;
			ns=i+s[i]-'0';
		}
	}
	printf("Case #%d: %d\n",x,add);
}
int main(){
	int t;
	cin>>t;
	rep(i,0,t)solve(i+1);
	return 0;
}

