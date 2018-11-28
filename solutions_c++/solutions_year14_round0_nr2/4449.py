#include <set>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
#include <map>

int main(){
	int t;
	cin>>t;
	cout<<std::setprecision(7)<<std::fixed;
	REP(q,t){
		long double C,F,X;
		long double result = 1000000000;
		long double lastresult = 1000000001;
		cin>>C>>F>>X;
		long double income = 2;
		long double wasted = 0;
		while(true){
			result = min(result, wasted + X / income);
			if(result == lastresult) break;
			lastresult = result;
			wasted += C / income;
			income += F;
		}
		cout<<"Case #"<<q+1<<": "<<result<<'\n';
	}
}

