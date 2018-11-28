#include <iostream>
#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

int dp(priority_queue<int> Q){
	if(Q.empty())
		return 0;
	int curr = Q.top();
	if(curr==1)
		return 1;
	int mn = 10000000;
	for(int i=2;i<=curr/2;++i){
		priority_queue<int> P = Q;
		P.pop();
		P.push(i);
		P.push(curr-i);
		mn = min(dp(P)+1,mn);
	}
	
	return min( mn,curr );
}

int main(){
	int T,D,P;
	cin >> T;
	for(int kase=1;kase<=T;kase++){
		cin>>D;
		priority_queue<int> Q;
		for (int i=0,v;i<D;++i){
			cin>>v;
			Q.push(v);
		}
		int res = dp(Q);
		/*
		while(!Q.empty()){
			int curr = Q.top();
			Q.pop();
			int prev;
			prev = Q.empty()?0 : Q.top();
			
			int mx = max((curr+1)/2,prev);
			Q.push(curr);
			if(mx+1 < curr){
				Q.pop();
				Q.push(curr/2);
				Q.push(curr - curr/2);
				res++;
			}else{
				res += curr;
				break;
			}
		}
		*/

		printf("Case #%d: %d\n",kase,res);
	}
	return 0;
}