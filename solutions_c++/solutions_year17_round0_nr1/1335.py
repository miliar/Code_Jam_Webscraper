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
#include<cassert>
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
int ma[1919];
int main()
{
	int t,n,k;string s;
	cin>>t;
	rep(i,t){
		cin>>s>>k;n=s.size();
		rep(j,n){
			if(s[j]=='+') ma[j]=1;else ma[j]=0;
		}
		int ret=0,f=0;
		rep(j,n-k+1){
			if(ma[j]<1){
				rep(K,k) ma[j+K]=1-ma[j+K];ret++;
			}
		}
		REP(j,1,k){
			if(ma[n-j]<1) f=1;
		}
		printf("Case #%d: ",i+1);
		if(f<1) cout<<ret<<endl;else cout<<"IMPOSSIBLE"<<endl;
	}
}
