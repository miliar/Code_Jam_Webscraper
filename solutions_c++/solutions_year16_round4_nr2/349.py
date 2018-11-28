#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:100000000000")
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
#include<complex>

using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it)) 
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define SQR(a) ((a)*(a))
typedef long long ll;
typedef unsigned long long  ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;



lld f2(vector<lld> &v){
	lld a[300][300]={0};
	a[0][0]=1;
	int n=v.size();
	FOR(i,1,n+1) FR(j,i+1){
		lld p=v[i-1];
		a[i][j] = p*(j>0?a[i-1][j-1]:0) + (1-p)*a[i-1][j];
	}
	return a[n][n/2];
}
int main(){
	freopen("a.in","r",stdin);	
	freopen("a.out","w",stdout);
	int tt;cin>>tt;
	FR(cas,tt){
		printf("Case #%d: ",cas+1);
		int n,k;
		cin>>n>>k;
		lld a[300];
		FR(i,n) cin>>a[i];
		lld maxi = 0;
		
		vector<lld> vv;
		FR(i,n) vv.push_back(a[i]);
		sort(ALL(vv));
		FR(i,n)vv.push_back(vv[i]);
		FR(i,vv.size()-k){
			vector<lld> v;
			FR(j,k) v.push_back(vv[i+j]);
			maxi=max(maxi,f2(v));
		}

		cout<<fixed<<setprecision(9)<<maxi<<endl;
	}
}