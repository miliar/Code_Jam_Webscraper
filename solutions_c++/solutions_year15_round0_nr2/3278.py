#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<queue>

using namespace std;

#define reps(i,f,n) for(int i=f;i<int(n);i++)
#define rep(i,n) reps(i,0,n)
#define pb push_back

using namespace std;

int solve2(vector<int>& p, int T){
	
	int ret = 0;
	rep(i,p.size()){
		ret += (p[i]-1)/T;
	}
	return ret+T;
}

int solve(){
	int n;
	cin>>n;
	vector<int> p(n);
	rep(i,n)cin>>p[i];
	
	int inf = 1111111;
	int ret = inf;
	reps(i,1,1111){
		ret = min(ret, solve2(p, i));
	}
	return ret;
}


int main(){
	int t;
	cin>>t;
	
	rep(i,t){
		printf("Case #%d: %d\n",i+1, solve());
	}
}