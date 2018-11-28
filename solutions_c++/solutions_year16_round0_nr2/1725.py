#include <cstring>
#include <cstdio>
#include <iostream>
using namespace std;

char str[105];
int main(){
	int T,ca=1;
	scanf("%d",&T);
	while(T--){
		scanf("%s",str);
		int l=strlen(str);
		while(l>=1&&str[l-1]=='+') l--;
		if(l==0) {
			printf("Case #%d: %d\n",ca++,0);
			continue;
		}
		int i=1;
		int ans=1;
		while(i<l){
			if(str[i]!=str[i-1]) ans++;
			i++;
		}
		printf("Case #%d: %d\n",ca++,ans);
	}
}
