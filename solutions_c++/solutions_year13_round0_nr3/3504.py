#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

#define rep(i,st,ed) for (int i=st; i<ed; i++)
#define foreach(it,s) for (__typeof(s.begin()) it=s.begin(); it!=s.end(); ++it)

const int MAXN=128;
const int INF=0x3f3f3f3f;
const double eps=1e-8;

int ca;
long long a,b;
vector<long long> value;

bool check(long long value){
	string ret="";
	while (value){
		ret+='0'+value%10;
		value/=10;
	}
	rep(i,0,ret.size()/2) if (ret[i]!=ret[ret.size()-i-1]) return false;
	return true;
}

void prepare(){
	rep(i,1,MAXN) if (check(i) && check(1LL*i*i)) value.push_back(1LL*i*i);
	cout<<value.size()<<endl;
}

void init(){
	cin>>a>>b;
}

int getsum(long long num){
	vector<long long>::iterator iter=lower_bound(value.begin(),value.end(),num);
	if (iter==value.end()) return value.size();
	if (*iter>num) --iter;
	return distance(value.begin(),iter)+1;
}

void solve(){
	cout<<getsum(b)-getsum(a-1)<<endl;
}

int main(){
	freopen("A.out","w",stdout);
	prepare();
	cin>>ca;
	rep(i,0,ca){
		cout<<"Case #"<<i+1<<": ";
		init();
		solve();
	}
	return 0;
}
