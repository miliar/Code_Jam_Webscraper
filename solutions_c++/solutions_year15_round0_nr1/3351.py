#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
using namespace std;
#define INF 0x3f3f3f3f
char st[1050];
int main(){
	int cases,k;
	scanf("%d",&cases);
	for (int cas=1;cas<=cases;cas++){
		scanf("%d",&k);
		scanf("%s",st);
		int len=strlen(st);
		int sum=st[0]-'0';
		int ans=0;
		for (int i=1;i<=k;i++){
			if (sum>=i) sum+=st[i]-'0';
			else{
				ans+=i-sum;
				sum=i+st[i]-'0';
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}