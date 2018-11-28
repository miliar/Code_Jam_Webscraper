#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include<map>
#include<set>
#include<queue>
#include<deque>

using namespace std;

#define reps(i,f,n) for(int i=f;i<int(n);i++)
#define rep(i,n) reps(i,0,n)
#define pb push_back

int solve(){
	int n;
	string s;
	cin>>n>>s;
	
	int ret = 0;
	
	int cnt = 0;
	rep(i,s.size()){
		if(s[i]=='0')continue;
		
		int num = s[i]-'0';
		if(cnt<i){
			int p = i-cnt;
			cnt += p;
			ret += p;
		}
		
		cnt += num;
	}
	
	return ret;
}


int main(){
	int t;
	cin>>t;
	
	rep(i,t){
		printf("Case #%d: %d\n", i+1, solve());
	}
}