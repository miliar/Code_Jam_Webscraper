#include<bits/stdc++.h>

#define LL long long
#define MP make_pair
#define PB push_back
#define MAXN 1000000
using namespace std;
int n,t;
int ans;
char in[2020];

int main(){
	scanf("%d",&t);
	for(int z=1;z<=t;z++){
		scanf("%s",in);
		n = strlen(in);
		printf("Case #%d: ",z);
		ans = 0;
		for(int i=1;i<n;i++){
			if(in[i]!=in[i-1])	ans++;
		}
		if(in[n-1]=='-')	ans++;
		printf("%d\n",ans);
	}
	return 0;
}