#include<iostream>
#include<cstdio>
using namespace std;
int t,n;
bool hash[11];
int main(){
	freopen("skj.in", "r", stdin);
	freopen("skj.out", "w", stdout);
	scanf("%d",&t);
	int cas=0;
	while (t--){
		printf("Case #%d: ",++cas);
		scanf("%d",&n);
		if (n==0){
			printf("INSOMNIA\n");
			continue;
		}
		for (int i=0;i<10;i++)
			hash[i]=0;
		int cnt=0;
		long long tot=0;
		while (cnt<10){
			tot+=(long long)n;
			int temp = tot;
			while (temp>0){
				if (!hash[temp%10]) cnt++;
				hash[temp%10] = 1;
				temp/=10;
			}
		}
		printf("%I64d\n",tot);
	}
} 
