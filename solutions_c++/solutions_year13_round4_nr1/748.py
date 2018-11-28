#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <list>
#include <set>
#include <numeric>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#define FOR(i, b, e) for (typeof(b) i = (b); i != (e); ++i)
#define VAR(a,b) typeof(b) a=b
#define dout //cout
using namespace std;
typedef long long LL;
typedef pair<LL, LL> P;
const LL mod=1000002013;
LL N;
int M;
LL cost(LL o, LL e){
	LL d=e-o;
	LL ret=d*N;
	ret%=mod;
	ret+=mod-(d*(d+1)/2%mod);
	return ret%mod;
}
void run(int Case)
{
	cin >> N >> M;
	vector<P> os;
	vector<P> oe;
	LL ret=0;
	FOR(i,0,M){
		int o, e, p;
		cin >> o>>e>>p;
		os.push_back(P(o,p));
		oe.push_back(P(e,p));
		//cout << o << ", " << e << ", " << cost(o,e) << endl;
		ret+=(cost(o,e)*p)%mod;
		ret%=mod;
	}
	//cout << "###" << ret << endl;

	sort(os.begin(),os.end());
	sort(oe.begin(),oe.end());

	int is=0,ie=0;
	vector<P> ss;
	while(ie<oe.size()){
		if(is<os.size()&&os[is].first<=oe[ie].first){
			//cout << os[is].first << ": " << os[is].second << endl;
			ss.push_back(os[is]);
			is++;
		}
		else
		{
			LL rem=oe[ie].second;
			LL e=oe[ie].first;
			ie++;
			//cout << "abc " << endl;
			while(rem){
				//cout << rem << endl;
				P b=ss.back();
				ss.pop_back();
				if(b.second>rem){
					//cout << "aaa " << b.second-rem << endl;
					ss.push_back(P(b.first,b.second-rem));
				}
				//cout << b.first << " " << e << " " << min(rem,b.second) << endl; 
				LL c=cost(b.first,e);
				c*=min(rem,b.second);
				c%=mod;
				ret+=mod-c;
				ret%=mod;
				rem=max(0LL,rem-b.second);
			}
		}
	}

	cout << "Case #" << Case << ": " << ret << endl;

}

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;t++) {
		run(t);
	}
}
