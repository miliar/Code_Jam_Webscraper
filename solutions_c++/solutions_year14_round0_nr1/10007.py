#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include<map>
#define MOD 1000000009
using namespace std;

#define gc getchar_unlocked

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    bool neg = false;
    for(;(c<48 || c>57);){
    	if(c == 45)
    		neg = true;
    	c = gc();
    }
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
	if(neg == true)x=-1*x;
}

inline int mod(int a, int b)
{ 
	if(a >= b)
		return a%b;
	if(a < 0)
		return (a%b+b)%b;
	else 
		return a;
}

int main() {
	
	int t;
	scanint(t);
	while(t--){
		int n,q;
		scanint(n);
		scanint(q);
		vector<int>v(n);
	
		for(int i=0;i<n;++i)
			scanint(v[i]);
		
		for(int i=0;i<q; ++i){
			int m;
			scanint(m);
			map<int,int> cnt;
			for(int i = 0; i<n; ++i){
				cnt[mod(v[i],m)]++;
			}
			vector<int>a;
			for(map<int,int>::iterator it = cnt.begin(); it!=cnt.end();++it){
				a.push_back(it->first);
			}
			n=a.size();
			int dp[2][m];
			memset(dp,0,sizeof(dp));
			//for i = 0, not choosing
			dp[0][0] = 1;
			// for i = 0, choosing
			dp[0][mod(a[0],m)] += cnt[a[0]];
			
			for(int i = 1; i < n ; ++i){
				
				// not choosing loop
				for(int j=0;j<m; ++j){
					dp[i&1][j] = dp[(i-1)&1][j]; 
				}
				
				//choosing loop
				for(int j=0;j<m;++j){
					int newval = (j+mod(a[i],m))%m;
					dp[i&1][newval] += (dp[(i-1)&1][j] * cnt[a[i]]);
					dp[i&1][j] = mod(dp[i&1][j], MOD);
				}
			}
			
			printf("%d\n",dp[(n-1)&1][0]);
		}
	}
	return 0;
}