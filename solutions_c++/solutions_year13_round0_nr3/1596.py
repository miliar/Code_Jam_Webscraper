
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<sstream>
#include<climits>
#include<vector>
#include<cstring>
#include<stack>

using namespace std;

#define REP(i,s,n)  for (int i=(s),_n=(n);i<=_n;i++)
#define FOR(i,s,n)  for (int i=(s),_n=(n);i<_n;i++)
#define REPD(i,e,s)  for (int i=(e),_s=(s);i>=_s;i--)
#define tr(container, it) \
	for (typeof(container.begin()) it=container.begin(); it!=container.end();it++)
#define PB push_back
#define MP make_pair

typedef long long LL;

LL ar[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,100000020000001,100220141022001,102012040210201,102234363432201,121000242000121,121242363242121,123212464212321,123456787654321};

int main() {
	int lim=47;
	int t;
	cin >> t;
	REP(tc,1,t) {
		LL a,b;
		cin >> a >> b;
		int ans=0;
		FOR(i,0,lim) if (ar[i]>=a && ar[i]<=b) ans++;
		cout << "Case #" << tc << ": " << ans << endl;
	}
	return 0;
}
