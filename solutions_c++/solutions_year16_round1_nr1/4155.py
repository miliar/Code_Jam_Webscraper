#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int Maxn=1005;

char s[Maxn],ss[Maxn*2];

int T,front,rear,i,length,cas;

int main() {
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	while (T--) {
		cas++;
		scanf("%s",s);
		length=strlen(s);
		printf("Case #%d: ",cas);
		front=1000;
		rear=1001;
		ss[1000]=s[0];
		for (i=1;i<length;i++) {
			if (ss[front]<=s[i]) ss[--front]=s[i];
			else ss[rear++]=s[i];
		}
		for (i=front;i<rear;i++) printf("%c",ss[i]);
		printf("\n");
	}
	return 0;
}
