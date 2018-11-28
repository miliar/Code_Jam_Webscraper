#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
#define maxn 2010
int a[maxn];
char s[maxn];
int main(){
	int T,n;
	scanf("%d",&T);
	for (int _=1;_<=T;_++) {
		scanf("%d",&n);
		scanf("%s",s);
		for (int i=0;i<n;i++) a[i]=s[i]-'0';
		int sum=a[0],ans=0;
		for (int i=1;i<=n;i++) {
			if (sum<i) ans+=i-sum,sum=i;
			sum+=a[i];
		}
		printf("Case #%d: %d",_,ans);
		if (_!=T) printf("\n");
	}
	return 0;
}

