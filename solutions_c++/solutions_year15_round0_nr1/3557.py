#include <bits/stdc++.h>
using namespace std;

int t;
int mx;
string s;
int main(){
	freopen("in.in","rt",stdin);
	freopen("in.out","wt",stdout);
	cin>>t;
	int cs = 0;
	while(t--){
		cin>>mx>>s;
		int sum = 0;
		int ans = 0;
		for(int i=0;i<int(s.size());i++){
			int d = s[i]-'0';
			if(i >= sum){
				ans += i-sum;
				sum += i-sum;
			}
			sum += d;
		}
		printf("Case #%d: %d\n",++cs,ans);
	}


}
