#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

char st[105];
int main(){
	int cases;
	scanf("%d",&cases);
	for (int cas=1;cas<=cases;cas++){
		scanf("%s",st);
		int len=strlen(st);
		int ans=0;
		if (st[len-1]=='+') ans=0;
		else ans=1;
		for (int i=len-2;i>=0;i--)
			if (st[i]!=st[i+1]) ans++;
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
