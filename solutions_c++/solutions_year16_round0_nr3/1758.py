#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> P;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
vector<string> v;
string cal(int n,int a){
	string s="";
	rep(i,n){
		s+=('0'+(a%2));a/=2;
	}
	return s;
}
lint zyo(int n, int k){
	lint ret=1;
	for(int i=0;i<k;i++) ret*=n;return ret;
}
int main()
{
	int t,n,m;
	cin>>t;
	rep(i,t){
		cin>>n>>m;
		printf("Case #%d:\n",i+1);
		rep(j,m){
			string s="1";s+=cal(n/2-2,j);s+="1";
			cout<<s<<s;
			REP(k,2,11) cout<<' '<<zyo(k,n/2)+1;cout<<endl;
		}
	}
}
