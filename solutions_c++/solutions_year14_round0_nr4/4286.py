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
	REP(q,t){
		vector<long double> naomi;
		vector<long double> ken;
		vector<long double> naomi1;
		vector<long double> ken1;
		int n;
		cin>>n;
		REP(i,n){
			long double t1;
			cin>>t1;
			naomi.PB(t1);
			ken1.PB(t1);
		}
		REP(i,n){
			long double t1;
			cin>>t1;
			ken.PB(t1);
			naomi1.PB(t1);
		}
		sort(ALL(naomi));
		sort(ALL(ken));
		reverse(ALL(naomi));
		reverse(ALL(ken));
		sort(ALL(naomi1));
		sort(ALL(ken1));
		reverse(ALL(naomi1));
		reverse(ALL(ken1));
		int result = 0;
		int result1 = 0;
		while(!naomi.empty()){
			if(naomi.back() < ken.back()){
				naomi.pop_back();
			} else{
				ken.pop_back();
				naomi.pop_back();
				result++;
			}
		}
		while(!naomi1.empty()){
			if(naomi1.back() < ken1.back()){
				naomi1.pop_back();
			} else{
				ken1.pop_back();
				naomi1.pop_back();
				result1++;
			}
		}
		cout<<"Case #"<<q+1<<": "<<result<<" "<<n -result1<<'\n';
	}
}

