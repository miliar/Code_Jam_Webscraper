#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

using namespace std;
typedef long long ll;

const int oo = 10000;
const int N = 1000;

int dp[N + 1][N + 1],arr[N];
int main(){
	int T,tmp,n;
	cin>>T;
	
	/*
	for(int i = 1;i <= N;i++)
		for(int j = 0;j <= N;j++)
			dp[i][j] = (j < i ? oo: 0);
	for(int i = 0;i <= N;i++)
		dp[0][i] = 0;
	/*
	for(int i = 1;i <= N;i++){
		cout<<"I: "<<i<<"\n";
		for(int k = 1;k <= i;k++){
			// no exchange
			dp[i][k] = dp[i - 1][k - 1]; // decrease
		
			// exchange
			for(int r1 = 1;r1 + r1 < i;r1++){
			int r2 = i - r1;
			for(int z = 0;z <= k;z++){
				int time = k - dp[r1][z];
				if(time >= 0)
				dp[i][k] = min(dp[i][k],dp[r1][z] + dp[r2][time] + 1);
				
				time = k - dp[r2][z];
				if(time >= 0)
				dp[i][k] = min(dp[i][k],dp[r1][time] + dp[r2][z] + 1);
			}
			}
		}
	}	
	*/
	FOR(tt,T){
		cin>>n;
		
		FOR(i,n){
			cin>>arr[i];
		}
			
		int bans = oo;
		for(int time = 1;time <= N;time++){
			int exc = 0;
			FOR(i,n){
				int tmp = arr[i];
				while(tmp > time){
					tmp -= time;
					exc++;
				}
			}
			//FOR(i,n)
			//	exc += dp[arr[i]][time];
			bans = min(bans,time + exc);
		}
		cout<<"Case #"<<tt + 1<<": "<<bans<<"\n";
	}
	return 0;
}
