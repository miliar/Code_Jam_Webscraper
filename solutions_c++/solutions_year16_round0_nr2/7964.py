#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue> 

using namespace std;

#define MP make_pair
#define PB push_back
#define MOD 1000000007
#define INF 1000000000

int main(){
	int t,tt;
	cin >> t;
	tt=t;
	while(t--){
		string s;
		cin >> s;
		printf("Case #%d: ",tt-t);
		int i,n,ans=0;
		n=s.size();
		for(i=0;i<n-1;i++){
			if(s[i]!=s[i+1]){
				ans++;
				if(s[i] == '-' && s[i+1] == '+'){
				//	ans++;
				}
				else {
				//	ans += 2;
				}
			}
		}
		if(s[n-1]=='-')ans++;
		cout << ans << endl;
	}
	return 0;
}
