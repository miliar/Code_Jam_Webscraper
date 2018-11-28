#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char s[1005];
int main(){
	int t,n,i;
	
	scanf("%d",&t);
	int ca=1;
	freopen("test.txt", "w", stdout);
	while(t--){
		scanf("%d %s",&n,s);
		int nowpeople = 0;
		int extra = 0;
		for(i=0;i<=n;i++){
			if(nowpeople >= i){
				nowpeople += s[i]-'0';
			}
			else{				
				extra += (i-nowpeople);
				nowpeople = i;
				nowpeople += s[i] - '0';
			}
		}
		printf("Case #%d: %d\n",ca++,extra);
	}
	return 0;
}