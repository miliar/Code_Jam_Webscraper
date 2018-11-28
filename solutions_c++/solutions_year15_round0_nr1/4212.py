#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	int n; scanf("%d",&n);
	for(int Case=1; Case<=n; ++Case){
		int t; scanf("%d",&t); getchar();
		char s[1010]; scanf("%s",s);
		int ans=0, now=s[0]-'0';
		for(int i=1; i<=t; ++i){
			if(s[i]!='0' && now<i){ ans+=i-now; now+=i-now; }
			now+=s[i]-'0';
		}
		printf("Case #%d: %d\n",Case,ans);
	}
	return 0;
}
