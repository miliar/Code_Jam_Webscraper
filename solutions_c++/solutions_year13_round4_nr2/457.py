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
int n;
int cal2(lint p){
	int i;
	for(i=n-1;i>=0;i--){
		if(!(p&(1LL<<i))) break;
	}
	if(i<0) return n;
	for(int j=i;j>=0;j--){
		if((p&(1LL<<j))) return n-i;
	}
	return n-i-1;
}
lint cal(lint p){
	//cout<<p<<" "<<cal2(p)<<endl;
	return (1LL<<n)-(1LL<<cal2(p));
}
int main()
{
	int t;lint p;
	cin>>t;
	rep(i,t){
		cin>>n>>p;p=(1LL<<n)-p;
		//cout<<n<<' '<<p<<endl;
		if(p<1){
			cout<<"Case #"<<i+1<<": "<<(1LL<<n)-1<<" "<<(1LL<<n)-1<<endl;continue;
		}
		lint mi=cal(p),ma=(1LL<<n)-2-cal((1LL<<n)-p);
		cout<<"Case #"<<i+1<<": "<<ma<<" "<<mi<<endl;
	}
	return 0;
}
