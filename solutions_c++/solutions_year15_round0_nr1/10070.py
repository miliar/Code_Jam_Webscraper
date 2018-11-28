#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t,m;
	cin>>t;
	m = t;
	while(t--){
		int n,i;
		cin>>n;
		char a[n+1];
		scanf("%s",a);
		int ct = a[0]-'0',ans=0;
		for(i=1;i<n+1;i++){
			if(a[i] == '0'){
				continue;
			}
			if(i > ct){
				ans += i-ct;
				ct += i-ct;
			}
			ct += a[i]-'0';
		}
		printf("Case #%d: %d\n",m-t,ans);
	}
	return 0;
}