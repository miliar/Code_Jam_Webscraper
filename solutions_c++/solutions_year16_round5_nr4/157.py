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
map<string,int> ma;
int main()
{
	int t,n,l;string s;
	cin>>t;
	rep(i,t){
		printf("Case #%d: ",i+1);
		cin>>n>>l;
		ma.clear();
		rep(j,n){
			cin>>s;ma[s]=1;
		}
		cin>>s;
		if(ma[s]>0){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		if(l==1) cout<<"? 0"<<endl;
		else{
			string S="10?";
			rep(i,l+2) S+="01";
			string ret(l-1,'?');
			cout<<ret<<' '<<S<<endl;
		}
	}
}
