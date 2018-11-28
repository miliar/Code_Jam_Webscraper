#include <cmath>
#include <cstdio>
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

const int MAXN=100001;
const int INF=0x3f3f3f3f;
const double eps=1e-8;

long long n,p;

long long power2(int n){
	return 1LL<<n;
}

void init(){
	cin>>n>>p;
}

void solve(){
	long long temp,ret;
	if (p==power2(n)){
		cout<<power2(n)-1<<' ';
	} else{
		temp=p,ret=0;
		for (int i=n-1; i>=0; i--){
			temp-=power2(i);
			if (temp<=0){
				cout<<ret<<' ';
				break;
			}
			ret+=power2(n-i);
		}
	}

	ret=0; temp=power2(n-1);
	for (long long i=1; i*2<=p; i*=2) {
		ret+=temp; 
		temp/=2;
	}	
	cout<<ret<<endl;
}

int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int ca;
	cin>>ca;
	rep(i,0,ca){
		cout<<"Case #"<<i+1<<": ";
		init();
		solve();
	}
	return 0;
}

