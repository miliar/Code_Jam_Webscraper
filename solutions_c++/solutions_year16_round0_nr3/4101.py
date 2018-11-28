#include <bits/stdc++.h>
#define maxn 1009
using namespace std;
int a[maxn],b[maxn];
int prime(long long x){
	for(int i=2;1LL*i*i<=x;i++)
		if(x%i==0)
			return i;
	return 0;
}
int check(int x){
	long long ans=0;
	for(int i=0;i<16;i++)
		ans=ans*x+a[i];
	int res=prime(ans);
	if(res==0)
		return -1;
	else
		return res;
}
int main(){
	freopen("A.out","w",stdout);
	int cnt=0;
	puts("Case #1:");
	for(int i=0;i<1<<14;i++){
		a[0]=1;
		for(int j=0;j<14;j++){
			if(i&(1<<j))
				a[j+1]=1;
			else
				a[j+1]=0;
		}
		a[15]=1;
		bool ok=1;
		for(int j=2;j<=10;j++){
			b[j]=check(j);
			if(b[j]==-1){
				ok=0;
				break;
			}
		}
		if(ok){
			for(int j=0;j<16;j++)
				printf("%d",a[j]);
			for(int j=2;j<=10;j++){
				printf(" %d",b[j]);
			}
			puts("");
			cnt++;
			if(cnt==50)
				return 0;
		}
	}
}