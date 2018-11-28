#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<map>

using namespace std;

#define reps(i,f,n) for(int i=f;i<int(n);i++)
#define rep(i,n) reps(i,0,n)

const int N = 11111;
const int X = 700;
int n,x;
int s[N];

int used[N];

void init(){
	cin>>n>>x;
	rep(i,n)cin>>s[i];
	rep(i,n)used[i]=0;
}

bool allEnd(){
	rep(i,n)if(used[i]==0)return false;
	return true;
}

int solve(){
	sort(s,s+n);
	
	int left=0;
	int right=n-1;
	
	int count = 0;
	while(1){
		if(left>right)break;
		if(s[left]+s[right]<=x){left++;right--;}
		else {right--;}
		count++;
	}
	return count;
}

int main(){
	int T;
	cin>>T;
	
	reps(t,1,T+1){
		init();
		printf("Case #%d: %d\n",t,solve());
	}
}


/*
1
5 5
2 2 1 3 2


*/