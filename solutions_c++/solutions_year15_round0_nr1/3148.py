#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int num = 0;
	while(t--){
		int n;
		char s[1010];
		scanf("%d %s",&n,&s);
		int sum = 0;
		int ans = 0;
		for(int i = 0;i<=n;i++){
			if(sum<i){ans+=i-sum;sum+=i-sum;}
			sum +=(s[i]-'0');
		}
		printf("Case #%d: %d\n",++num,ans);
	}
} 