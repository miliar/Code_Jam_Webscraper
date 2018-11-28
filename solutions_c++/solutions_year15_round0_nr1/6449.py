#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef long long ll;


int main() {
	freopen( "in.txt", "r" , stdin);
	freopen( "out.txt", "w" , stdout);

	int t,n,i,j,cas = 1;
	cin>>t;
	while(t--) {
		string s;
		cin>>n>>s;
		int res = 0;
		int tot = 0;
		for(i = 0;i <=n;i ++) {
			int tp = s[i]-'0';
			if (tot < i) {
				res += i-tot;
				tot = i;
			}
			tot += tp;
		}
		printf("Case #%d: %d\n",cas++,res);
	}


}

