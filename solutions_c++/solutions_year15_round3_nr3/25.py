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

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int cas;cin>>cas;
	FR(mycas,cas){
		printf("Case #%d: ",mycas+1);
		ll c,d,v;
		cin>>c>>d>>v;
		ll a[1000];
		FR(i,d) cin>>a[i];a[d]=1LL<<50;
		ll sum=0;
		ll req=0;
		int ind=0;
		while(sum<v){
			if(a[ind]<=sum+1){
				sum+=a[ind]*c;
				ind++;
			}else{
				sum+=(sum+1)*c;
				req++;
			}
		}
		cout<<req<<endl;
	}

}