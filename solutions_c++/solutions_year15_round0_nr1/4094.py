#include<iostream>
#include<algorithm>
using namespace std;

int a[1024];

char readchar(){
	char tmpchar=getchar();
	while(tmpchar==' ' || tmpchar=='\r' || tmpchar=='\n'){
		tmpchar=getchar();
	}
	return tmpchar;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;c++){
		int friends=0;
		int smax;
		scanf("%d",&smax);
		getchar();
		for(int i=0;i<=smax;i++) {
			char charin;
			charin=readchar();
			a[i]=charin-'0';
		}
		int accumulated = 0;
		for(int i=0;i<=smax;i++) {
			friends=max(friends,i-accumulated);
			accumulated+=a[i];
		}
		printf("Case #%d: %d\n",c,friends);
	}
	return 0;
}