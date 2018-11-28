#include <bits/stdc++.h>
#define M 1000
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
		int n,x,sum=0,ctr=0;char s[M];
		scanf("%d%s",&n,s);
		for(int i=0;i<=n;i++)
		{
			x=s[i]-'0';
			if(i==0) {sum+=x; continue;}
			if(i>sum && x>0) { ctr+=i-sum; sum+=i+x;}
			else sum+=x;
		}
		printf("Case #%d: %d\n",j,ctr);
	}
	return 0;
}