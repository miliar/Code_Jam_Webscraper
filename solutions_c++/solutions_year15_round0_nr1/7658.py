#include<bits/stdc++.h>
using namespace std;

#define lli long long
#define pb push_back

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int t,n;
	string s;
	scanf("%d",&t);
	int temp = t;
	while(t--){
		cin>>n>>s;
		int ans = 0;
		int total = 0;
		for(int i=0;i<=n;i++){
			if(total>=i){
				total += s[i]-'0';
				continue;
			}
			int temp = abs(i-total);
			total += temp;
			ans += temp;
			total += s[i]-'0';
		}
		printf("Case #%d: %d\n",temp-t,ans);
	}
}
