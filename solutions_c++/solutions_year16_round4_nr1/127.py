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
int out[(1<<12)+10];
int a[5];string str="RPS";
int n;
string cal(void){
	rep(i,n){
		int r=(a[0]+a[2]-a[1])/2;
		int p=(a[0]+a[1]-a[2])/2;
		int s=(a[1]+a[2]-a[0])/2;
		if(r<0 || p<0 || s<0) return "IMPOSSIBLE";
		a[0]=r;a[1]=p;a[2]=s;
		//rep(j,3) cout<<a[j]<<' ';cout<<endl;
	}
	rep(i,3){
		if(a[i]>0) out[0]=i;
	}
	//cout<<out[0]<<endl;
	rep(i,n) rep(j,(1<<i)){
		out[(j<<(n-i))+(1<<(n-i-1))]=(out[(j<<(n-i))]+2)%3;
	}
	string ret="";
	rep(i,(1<<n)) ret+=str[out[i]];
	rep(i,n) rep(j,(1<<(n-i-1))){
		string mae=ret.substr(j<<(i+1),(1<<i)),ato=ret.substr((j<<(i+1))+(1<<i),(1<<i));
		if(mae>ato){
			rep(k,(1<<i)) swap(ret[(j<<(i+1))+k],ret[(j<<(i+1))+(1<<i)+k]);
		}
	}
	return ret;
}
int main()
{
	int t;
	cin>>t;
	rep(i,t){
		cin>>n>>a[0]>>a[1]>>a[2];
		cout<<"Case #"<<i+1<<": "<<cal()<<endl;
	}
}
