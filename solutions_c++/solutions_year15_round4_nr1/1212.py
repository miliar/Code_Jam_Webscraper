#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:10000000000")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it)) 
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define INF 1e8
#define EPS 1e-8
#define MOD 1000000007
#define SQR(a) ((a)*(a))
typedef long long  ll;
typedef unsigned long long  ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;

char a[110][110];
int n,m;
int check(){
	int sum=0;
	map<char,PII> mp;
	mp['v']=PII(1,0);
	mp['^']=PII(-1,0);
	mp['>']=PII(0,1);
	mp['<']=PII(0,-1);

	FR(i,n)FR(j,m) if(a[i][j]!='.'){
		PII now(i,j);
		PII dir=mp[a[i][j]];
		now.first+=dir.first;
		now.second+=dir.second;
		int c=0;
		while(now.first >=0 && now.first<n && now.second>=0 && now.second<m){
			if(a[now.first][now.second]!='.') c++;
			now.first+=dir.first;
			now.second+=dir.second;
		}
		if(c!=0) continue;
		c=0;
		FR(q,n) if(a[q][j]!='.') c++;
		FR(q,m) if(a[i][q]!='.') c++;
		if(c<=2) return -1;
		sum++;
	}
	return sum;
}
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;cin>>t;FR(cas,t){
		printf("Case #%d: ",cas+1);
		cin>>n>>m;
		FR(i,n) cin>>a[i];
		int ret=check();
		if(ret<0) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ret<<endl;

	}		
}