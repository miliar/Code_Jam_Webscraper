#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

int n,s[1000];
int Z,test,res,now;

int f(int a, int cnt) {
	if ( cnt==n-1 ) {
		if ( a>s[cnt] ) return 0;
		return 1;
	}
	
	int sum=987654321;

	if ( a>s[cnt] ) sum=f(a+s[cnt],cnt+1);
	else {
		if ( a-1>0 ) sum=min(f(a,cnt+1),f(a+a-1,cnt))+1;
		else sum=f(a,cnt+1)+1;
	}
	return sum;
}

int main() {
	int i,j,k;
	freopen("A-small-attempt8.in","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&test);
	for ( Z=1; Z<=test; Z++ ) {
		res=0;
		scanf("%d %d",&now,&n);
		for ( i=0; i<n; i++ ) {
			scanf("%d",&s[i]);
		}
		sort(s,s+n);
		res=f(now,0);

		printf("Case #%d: %d\n",Z,res);
	}

}