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

bool isEq(lld a,lld b){
	return fabs(a-b)<1e-10;
}
bool ss1[10000],ss2[10000];
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;cin>>t;FR(cas,t){
		printf("Case #%d: ",cas+1);
		int n;cin>>n;
		vector<int> v[22];
		map<string,int> mp;mp.clear();
		int count=0;
		cin.get();
		FR(i,n){
			v[i].clear();
			string s;
			getline(cin,s);
			stringstream ss(s);
			while(ss>>s){
				if(mp.find(s)==mp.end())mp[s]=count++;
				v[i].push_back(mp[s]);
			}
		}
		ll res=1LL<<60;
		FR(t,1<<(n-2)){
			int mask = (t<<2) + 2;		
			CLR(ss1,false);
			CLR(ss2,false);
			FR(i,n){
				if(mask&(1<<i)){
					FR(j,v[i].size()) ss2[v[i][j]]=true;
				}else{
					FR(j,v[i].size()) ss1[v[i][j]]=true;
				}
			}
			ll sum=0;
			FR(i,10000) if(ss1[i]&&ss2[i]) sum++;
			res=min(res,sum);
		}
		cout<<res<<endl;
	}
}